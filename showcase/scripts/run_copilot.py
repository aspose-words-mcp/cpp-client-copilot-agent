"""Generate or replay C++ answers, optionally compile, and write honest reports."""
import argparse,json,re,shutil,subprocess,tempfile,time,uuid
from pathlib import Path
from compile_cpp import compile_answer
from copilot_results import extract
ROOT=Path(__file__).resolve().parents[2]
def select(cases, query_id=None, all_cases=False):
    found=[c for c in cases if not query_id or c['query_id']==query_id]
    if not found:raise ValueError('No matching question.')
    return found if all_cases or query_id else found[:1]
def reports(folder, records):
    text=['# C++ answer showcase','','Runtime execution: **Not checked**. Replayed answers are not live Copilot generations.','']
    metrics=['# Run metrics','','| Question | Origin | Generation | Compilation | Models |','| --- | --- | --- | --- | --- |']
    for r in records:
        text += ['## '+r['query_id'],'',r['question'],'', 'Origin: '+r['origin']+'. Compilation: '+r['verification']['status']+'.','',r['answer'],'']
        metrics.append('| '+' | '.join([r['query_id'],r['origin'],r['generation'],r['verification']['status'],', '.join(r.get('models',[])) or 'unknown'])+' |')
    (folder/'showcase.md').write_text('\n'.join(text),encoding='utf-8')
    (folder/'metrics.md').write_text('\n'.join(metrics)+'\n',encoding='utf-8')
    (folder/'results.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run',required=True);p.add_argument('--query-id');p.add_argument('--all',action='store_true');p.add_argument('--dry-run',action='store_true')
    p.add_argument('--answer-file',type=Path);p.add_argument('--verify-code',action='store_true');p.add_argument('--packages',type=Path)
    p.add_argument('--model',default='auto');p.add_argument('--timeout',type=int,default=300);p.add_argument('--build-timeout',type=int,default=180)
    a=p.parse_args()
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
                    command=[binary,'-C',str(workspace),'--trust-folder','--agent','aspose-words-cpp-mcp','--model',a.model,'--name',str(uuid.uuid4()),'--no-ask-user','--no-auto-update','--disable-builtin-mcps','--disable-mcp-server','ide','--additional-mcp-config',json.dumps({'mcpServers':{'words-cpp':server}}),'--allow-tool=words-cpp','--deny-tool=write','--deny-tool=shell','--output-format','json','-p',case['question']]
                    proc=subprocess.run(command,cwd=workspace,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=a.timeout)
                    events=workspace/'events.jsonl';events.write_text(proc.stdout,encoding='utf-8');parsed=extract(events)
                    answer=parsed['recorded_answer_markdown'];record['models']=parsed['resolved_models'];record['warnings']=parsed['warnings']
                    evidence=any(t.get('server')=='words-cpp' and t.get('success') is True for t in parsed['tools'])
                    if proc.returncode or not answer or not evidence:
                        record['generation']='failed';record['diagnostics']=proc.stderr[-4000:];failed=True
            record['answer']=answer
            record['verification']=compile_answer(answer,a.packages,a.build_timeout) if a.verify_code and record['generation']=='completed' else {'status':'not_checked','runtime_executed':False}
            if record['verification']['status'] in ('failed','unavailable','timeout'):failed=True
        except (OSError,subprocess.TimeoutExpired) as e:
            record.update(generation='failed',answer='',error=str(e),verification={'status':'not_checked','runtime_executed':False});failed=True
        records.append(record);reports(folder,records)
        if record['generation']=='failed':break
    print(folder)
    if failed:raise SystemExit(1)
if __name__=='__main__':main()
