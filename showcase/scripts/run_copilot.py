"""Generate or replay C++ answers, optionally compile, and write honest reports."""
import argparse,json,re,shutil,subprocess,tempfile,time,uuid
from pathlib import Path
from compile_cpp import compile_answer,FENCE,MAIN
from copilot_results import extract
from repair_cpp import compiler_feedback,sdk_header_context,repair_prompt
ROOT=Path(__file__).resolve().parents[2]
PROGRAM_REQUIREMENTS = """
Answer using the configured Aspose.Words C++ MCP tools and cite online sources.
For a coding question, return a complete standalone C++17 program in one cpp
fence, including verified SDK headers and int main(). Put executable statements
inside main() and helper classes/functions outside it. Do not return disconnected
continuation fragments or alternative snippet fences. Include all declarations
needed to compile against Aspose.Words for C++ 26.9.0; do not invent headers/APIs.
Create sample input documents where practical; otherwise explain required inputs,
licenses, credentials and external services. For a purely conceptual or unsupported
scenario, explain it without a code fence. Do not claim compilation or runtime
execution: a separate runner records actual verification results.
"""

def generation_prompt(question):
    rules='\n'.join((ROOT/'examples'/name).read_text(encoding='utf-8') for name in ('cpp-build-rules.instructions.md','error-correction.md'))
    return question+'\n\n'+PROGRAM_REQUIREMENTS+'\n'+rules

def missing_entry_points(answer):
    return [i for i,code in enumerate(FENCE.findall(answer),1) if not MAIN.search(code)]

def showcase_answer(record):
    """Display the tested complete source, never an unlabelled partial program."""
    blocks={b['block']:b for b in record['verification'].get('blocks',[])}
    index=0
    def render(match):
        nonlocal index
        index+=1
        block=blocks.get(index,{})
        source=block.get('compiled_source',match.group(1))
        if not MAIN.search(source):
            return ('**Incomplete code block '+str(index)+': missing main().** '
                    'The original fragment is preserved in results.json; it is not presented as a runnable program.')
        note=''
        if block.get('strategy') not in (None,'original'):
            note=('Compilation harness: `'+block['strategy']+'`. '
                  'The original response is preserved in results.json.\n\n')
        return note+'```cpp\n'+source.rstrip()+'\n```'
    return FENCE.sub(render,record['answer'])

def select(cases, query_id=None, all_cases=False):
    found=[c for c in cases if not query_id or c['query_id']==query_id]
    if not found:raise ValueError('No matching question.')
    return found if all_cases or query_id else found[:1]
def reports(folder, records):
    text=['# C++ answer showcase','','Runtime execution: **Not checked**. Replayed answers are not live Copilot generations.','']
    metrics=['# Run metrics','','| Question | Origin | Generation | Compilation | Models |','| --- | --- | --- | --- | --- |']
    counts={status:sum(r['verification']['status']==status for r in records) for status in sorted({r['verification']['status'] for r in records})}
    summary='; '.join(str(count)+' '+status for status,count in counts.items())
    metrics[2:2]=['Compilation results: '+summary+'.', '', 'Passed means compiled and linked, including a recorded harness where needed. Failed means no tested compilation unit succeeded; it does not establish that an incomplete fragment has invalid APIs. Runtime execution: **Not checked**.', '']
    for r in records:
        text += ['## '+r['query_id'],'',r['question'],'', 'Origin: '+r['origin']+'. Compilation: '+r['verification']['status']+'.','',showcase_answer(r),'']
        if r.get('repairs'):text += ['Compiler-feedback repair requests: '+str(len(r['repairs']))+'. See repair-log.md and results.json for attempt history.', '']
        if r.get('format_issues'):text += ['Format warnings: '+'; '.join(r['format_issues']), '']
        metrics.append('| '+' | '.join([r['query_id'],r['origin'],r['generation'],r['verification']['status'],', '.join(r.get('models',[])) or 'unknown'])+' |')
    (folder/'showcase.md').write_text('\n'.join(text),encoding='utf-8')
    (folder/'metrics.md').write_text('\n'.join(metrics)+'\n',encoding='utf-8')
    repair_log=['# Compiler repair log','','Copilot receives prior generated answers, path-redacted compiler errors and SDK-relative header names. Programs are not executed. Raw diagnostics stay in results.json.','']
    for r in records:
        if r.get('repairs'):
            repair_log += ['## '+r['query_id'],'','Final generation: '+r['generation']+'. Compilation: '+r['verification']['status']+'.','']
        for attempt in r.get('repairs',[]):
            repair_log += ['### Repair request '+str(attempt['number']),'','```text',attempt['feedback'],'```','',attempt['sdk_headers'],'']
    (folder/'repair-log.md').write_text('\n'.join(repair_log),encoding='utf-8')
    (folder/'results.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run',required=True);p.add_argument('--query-id');p.add_argument('--all',action='store_true');p.add_argument('--dry-run',action='store_true')
    p.add_argument('--answer-file',type=Path);p.add_argument('--verify-code',action='store_true');p.add_argument('--packages',type=Path)
    p.add_argument('--repair-attempts',type=int,default=2,help='Compiler-feedback repairs per answer, 0 disables.')
    p.add_argument('--model',default='auto');p.add_argument('--timeout',type=int,default=300);p.add_argument('--build-timeout',type=int,default=180)
    a=p.parse_args()
    if not 0 <= a.repair_attempts <= 5:p.error('--repair-attempts must be between 0 and 5.')
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]*',a.run):p.error('Use a simple run name; paths are not allowed.')
    try:cases=select(json.loads((ROOT/'showcase/inputs/questions.json').read_text())['cases'],a.query_id,a.all)
    except ValueError as e:p.error(str(e))
    if a.answer_file and len(cases)!=1:p.error('--answer-file requires one selected question.')
    if a.dry_run:print(json.dumps(cases,indent=2));return
    folder=ROOT/'showcase/runs'/a.run
    if folder.exists():p.error('Run already exists; choose a new name to preserve previous results.')
    binary=None;server=None
    if not a.answer_file:
        binary=shutil.which('copilot')
        if not binary:p.error('Copilot CLI not found. Install/authenticate it, or use --answer-file.')
        server=json.loads((ROOT/'.vscode/mcp.json').read_text())['servers']['words-cpp']
        if 'YOUR_MCP_HOST' in server['url']:p.error('Configure the MCP endpoint first.')
    folder.mkdir(parents=True);records=[];failed=False
    for case in cases:
        record=dict(case,origin='saved-answer' if a.answer_file else 'copilot-cli',models=[],generation='completed')
        try:
            if a.answer_file:answer=a.answer_file.read_text(encoding='utf-8')
            else:
                with tempfile.TemporaryDirectory(prefix='words-cpp-session-') as tmp:
                    workspace=Path(tmp)
                    shutil.copytree(ROOT/'.github',workspace/'.github')
                    command=[binary,'-C',str(workspace),'--trust-folder','--agent','aspose-words-cpp-mcp','--model',a.model,'--name',str(uuid.uuid4()),'--no-ask-user','--no-auto-update','--disable-builtin-mcps','--disable-mcp-server','ide','--additional-mcp-config',json.dumps({'mcpServers':{'words-cpp':server}}),'--allow-tool=words-cpp','--deny-tool=write','--deny-tool=shell','--output-format','json','-p',generation_prompt(case['question'])+sdk_header_context(a.packages)]
                    record['generation_attempts']=[]
                    repairs=0;format_retries=0
                    while True:
                        proc=subprocess.run(command,cwd=workspace,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=a.timeout)
                        events=workspace/'events.jsonl';events.write_text(proc.stdout,encoding='utf-8');parsed=extract(events)
                        answer=parsed['recorded_answer_markdown'];record['models']=parsed['resolved_models'];record['warnings']=parsed['warnings']
                        evidence=any(t.get('server')=='words-cpp' and t.get('success') is True for t in parsed['tools'])
                        verification=compile_answer(answer,a.packages,a.build_timeout) if a.verify_code and not proc.returncode and answer and evidence else {'status':'not_checked','runtime_executed':False}
                        record['verification']=verification
                        record['answer']=answer
                        record['generation_attempts'].append({'answer':answer,'models':parsed['resolved_models'],'missing_main_blocks':missing_entry_points(answer),'verification':verification,'mcp_evidence':evidence})
                        if proc.returncode or not answer or not evidence:break
                        if verification['status']=='failed' and compiler_feedback(verification) and repairs < a.repair_attempts:
                            repairs+=1
                            feedback=compiler_feedback(verification)
                            record.setdefault('repairs',[]).append({'number':repairs,'feedback':feedback,'sdk_headers':sdk_header_context(a.packages,answer,feedback)})
                            command[-1]=repair_prompt(generation_prompt(case['question']),answer,verification,a.packages)
                            continue
                        if missing_entry_points(answer) and format_retries < 1:
                            format_retries+=1
                            command[-1]=generation_prompt(case['question'])+sdk_header_context(a.packages,answer)+'\nReturn one complete standalone program with main(), not snippets.'
                            continue
                        break
                    evidence=any(t.get('server')=='words-cpp' and t.get('success') is True for t in parsed['tools'])
                    if proc.returncode or not answer or not evidence:
                        record['generation']='failed';record['diagnostics']=proc.stderr[-4000:];failed=True
            record['format_issues']=['Block '+str(i)+' is missing main().' for i in missing_entry_points(answer)]
            record['answer']=answer
            if a.answer_file:
                record['verification']=compile_answer(answer,a.packages,a.build_timeout) if a.verify_code else {'status':'not_checked','runtime_executed':False}
            if record['verification']['status'] in ('failed','unavailable','timeout'):failed=True
        except (OSError,subprocess.TimeoutExpired) as e:
            record.update(generation='failed',error=type(e).__name__+': generation/build process failed or timed out');record.setdefault('answer','');record.setdefault('verification',{'status':'not_checked','runtime_executed':False});failed=True
        records.append(record);reports(folder,records)
        print(case['query_id']+': '+record['generation']+' / '+record['verification']['status'],flush=True)
    print(folder)
    if failed:raise SystemExit(1)
if __name__=='__main__':main()
