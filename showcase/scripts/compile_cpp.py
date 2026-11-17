"""Compile independent verbatim C++ fences without executing programs."""
import os,re,shutil,subprocess,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
FENCE=re.compile(r'^```(?:cpp|c\+\+|cxx|cc)[ \t]*\r?\n(.*?)^```[ \t]*\r?$',re.M|re.S|re.I)
def compile_answer(answer, packages, timeout=180):
    blocks=FENCE.findall(answer)
    result={'status':'no_code','runtime_executed':False,'sdk_version':'26.9.0','blocks':[]}
    if not blocks:return result
    if os.name!='nt' or not packages or not Path(packages).is_dir():
        return dict(result,status='unavailable',reason='Windows C++ Build Tools and restored SDK packages are required.')
    shell=shutil.which('pwsh') or shutil.which('powershell')
    if not shell:return dict(result,status='unavailable',reason='PowerShell not found.')
    for index,code in enumerate(blocks,1):
        with tempfile.TemporaryDirectory(prefix='words-cpp-build-') as tmp:
            d=Path(tmp)
            for name in ('WordsCppExamples.vcxproj','build.ps1'):
                shutil.copyfile(ROOT/'examples'/name,d/name)
            (d/'main.cpp').write_text(code,encoding='utf-8')
            try:
                proc=subprocess.run([shell,'-NoProfile','-File',str(d/'build.ps1'),'-PackagesDirectory',str(Path(packages).resolve())],cwd=d,capture_output=True,text=True,errors='replace',timeout=timeout)
                status='passed' if proc.returncode==0 else 'failed'
                diagnostics=(proc.stdout+'\n'+proc.stderr)[-8000:]
            except subprocess.TimeoutExpired:
                status='timeout';diagnostics='Build exceeded timeout.'
            result['blocks'].append({'block':index,'status':status,'diagnostics':diagnostics})
    result['status']='passed' if all(x['status']=='passed' for x in result['blocks']) else 'failed'
    return result
