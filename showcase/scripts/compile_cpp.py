"""Compile original C++ fences or explicitly recorded snippet harnesses. Never execute."""
import os,re,shutil,subprocess,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
FENCE=re.compile(r'^```(?:cpp|c\+\+|cxx|cc)[ \t]*\r?\n(.*?)^```[ \t]*\r?$',re.M|re.S|re.I)
MAIN=re.compile(r'\b(?:main|wmain)\s*\(')

def wrap_statements(code):
    # Only hoist unconditional includes. Leave all API names and headers unchanged.
    if re.search(r'^\s*#\s*(?:if|else|endif|define|undef)',code,re.M):
        return None
    includes=[]; body=[]
    for line in code.splitlines():
        (includes if re.match(r'^\s*#\s*include\b',line) else body).append(line)
    return '\n'.join(includes)+'\nint main() {\n'+'\n'.join('    '+line for line in body)+'\n    return 0;\n}\n'

def candidates(code, context=None):
    yield 'original',code
    if MAIN.search(code):return
    # Allows translation units containing helper functions/classes but no entry point.
    yield 'empty_main',code+'\nint main() { return 0; }\n'
    wrapped=wrap_statements(code)
    if wrapped:yield 'statement_main',wrapped
    if context and not re.search(r'^\s*#',code,re.M):
        combined=wrap_statements(context+'\n'+code)
        if combined:yield 'shared_context_main',combined

def compile_answer(answer, packages, timeout=180):
    blocks=FENCE.findall(answer)
    result={'status':'no_code','runtime_executed':False,'sdk_version':'26.9.0','blocks':[]}
    if not blocks:return result
    if os.name!='nt' or not packages or not Path(packages).is_dir():
        return dict(result,status='unavailable',reason='Windows C++ Build Tools and restored SDK packages are required.')
    shell=shutil.which('pwsh') or shutil.which('powershell')
    if not shell:return dict(result,status='unavailable',reason='PowerShell not found.')
    context=None
    for index,code in enumerate(blocks,1):
        attempts=[];passed=None
        with tempfile.TemporaryDirectory(prefix='words-cpp-build-') as tmp:
            d=Path(tmp)/"build-project"
            d.mkdir()
            source_dir=Path(tmp)/"src"
            source_dir.mkdir()
            for name in ('WordsCppExamples.vcxproj','build.ps1'):
                shutil.copyfile(ROOT/'examples'/'build-project'/name,d/name)
            for strategy,source in candidates(code,context):
                (source_dir/'main.cpp').write_text(source,encoding='utf-8')
                try:
                    proc=subprocess.run([shell,'-NoProfile','-ExecutionPolicy','Bypass','-File',str(d/'build.ps1'),'-PackagesDirectory',str(Path(packages).resolve())],cwd=d,capture_output=True,text=True,errors='replace',timeout=timeout)
                    status='passed' if proc.returncode==0 else 'failed'
                    diagnostics=(proc.stdout+'\n'+proc.stderr)[-8000:]
                except subprocess.TimeoutExpired:
                    status='timeout';diagnostics='Build exceeded timeout.'
                attempts.append({'strategy':strategy,'status':status,'diagnostics':diagnostics})
                if status=='passed':
                    passed={'strategy':strategy,'compiled_source':source};break
        item={'block':index,'status':'passed' if passed else 'failed','original_source':code,'attempts':attempts,'diagnostics':attempts[-1]['diagnostics']}
        if passed:
            item.update(passed)
            if passed['strategy']=='statement_main':context=code
            elif passed['strategy']=='shared_context_main':context=context+'\n'+code
        else:
            item['note']='No tested harness compiled. Review diagnostics: an incomplete fragment is not proof of an invalid API.'
        result['blocks'].append(item)
    result['status']='passed' if all(x['status']=='passed' for x in result['blocks']) else 'failed'
    return result
