"""Recompile saved answers without calling Copilot or MCP; retain previous reports."""
import argparse,json,shutil,datetime
from concurrent.futures import ThreadPoolExecutor,as_completed
from pathlib import Path
from compile_cpp import compile_answer
from run_copilot import reports,ROOT

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run',required=True);p.add_argument('--packages',type=Path,required=True)
    p.add_argument('--workers',type=int,default=2);p.add_argument('--build-timeout',type=int,default=180)
    a=p.parse_args()
    folder=(ROOT/'showcase/runs'/a.run).resolve()
    if folder.parent != (ROOT/'showcase/runs').resolve():p.error('Use a run folder name.')
    records=json.loads((folder/'results.json').read_text(encoding='utf-8'))
    backup=folder/('before-recheck-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f'))
    backup.mkdir()
    for name in ('results.json','showcase.md','metrics.md'):
        if (folder/name).exists():shutil.copy2(folder/name,backup/name)
    with ThreadPoolExecutor(max_workers=max(1,min(a.workers,4))) as pool:
        jobs={pool.submit(compile_answer,r['answer'],a.packages,a.build_timeout):r for r in records if r.get('generation')=='completed'}
        for job in as_completed(jobs):
            r=jobs[job];r['verification']=job.result()
            r['compilation_rechecked_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
            reports(folder,records)
            print(r['query_id']+': '+r['verification']['status'],flush=True)
    reports(folder,records)
if __name__=='__main__':main()
