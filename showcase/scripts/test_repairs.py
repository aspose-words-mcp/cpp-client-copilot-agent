import json,sys,tempfile,unittest,subprocess
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import run_copilot as runner
from repair_cpp import redact_paths,compiler_feedback,sdk_header_context

class RepairTests(unittest.TestCase):
    def test_redacted_feedback(self):
        v={'blocks':[{'status':'failed','diagnostics':r"C:\Users\private\main.cpp(2): fatal error C1083: Cannot open include file: 'bad.h' [D:\private\build.vcxproj]"}]}
        result=compiler_feedback(v)
        self.assertIn('C1083',result)
        self.assertNotIn('private',result)
        self.assertNotIn('D:',result)
        self.assertNotIn('private',redact_paths('file="C:\\Users\\private\\x.cpp"'))
    def test_header_inventory(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'Aspose.Words.Cpp.26.9.0/build/native/include'
            h=root/'Aspose.Words.Cpp/Document.h';h.parent.mkdir(parents=True);h.write_text('')
            (h.parent/'Watermark.h').write_text('')
            result=sdk_header_context(tmp)
            self.assertIn('Aspose.Words.Cpp/Document.h',result)
            self.assertNotIn(tmp,result)
            self.assertNotIn('Range.h',result)
            self.assertNotIn('Watermark.h',sdk_header_context(tmp,'Use Watermark.'))
            self.assertIn('Aspose.Words.Cpp/Watermark.h',sdk_header_context(tmp,'Use Watermark.',include_symbols=True))
            self.assertNotIn('Watermark.h',sdk_header_context(tmp,'Use WatermarkOptions.',include_symbols=True))
    def run_fake(self,first_status='failed',timeout=False):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for d in ('examples','.github','.vscode','showcase/inputs'): (root/d).mkdir(parents=True,exist_ok=True)
            for n in ('cpp-build-rules.instructions.md','error-correction.md'): (root/'examples'/n).write_text('Rules')
            (root/'.vscode/mcp.json').write_text(json.dumps({'servers':{'words-cpp':{'url':'http://localhost/test'}}}))
            cases=[{'query_id':'one','question':'Q'}]
            if timeout:cases.append({'query_id':'two','question':'Q2'})
            (root/'showcase/inputs/questions.json').write_text(json.dumps({'cases':cases}))
            parsed={'recorded_answer_markdown':'```cpp\nint main(){}\n```','resolved_models':['test'],'warnings':[],'tools':[{'server':'words-cpp','success':True}]}
            fail={'status':first_status,'blocks':[{'block':1,'status':first_status,'diagnostics':'main.cpp: error C2027: undefined type'}]}
            passed={'status':'passed','blocks':[]}
            calls=[subprocess.TimeoutExpired('fake',1),SimpleNamespace(stdout='',stderr='',returncode=0),SimpleNamespace(stdout='',stderr='',returncode=0)] if timeout else [SimpleNamespace(stdout='',stderr='',returncode=0)]*4
            verifies=[passed,passed] if timeout else [fail,passed]
            argv=['run','--run','test','--all','--verify-code','--repair-attempts','1']
            with patch.object(runner,'ROOT',root),patch.object(sys,'argv',argv),patch.object(runner.shutil,'which',return_value='fake'),patch.object(runner.subprocess,'run',side_effect=calls) as generate,patch.object(runner,'extract',return_value=parsed),patch.object(runner,'compile_answer',side_effect=verifies) as compile_mock,patch.object(runner.time,'sleep'):
                runner.main()
            records=json.loads((root/'showcase/runs/test/results.json').read_text())
            return records,generate.call_count,compile_mock.call_count
    def test_repair_preserves_attempts(self):
        records,calls,builds=self.run_fake()
        self.assertEqual((calls,builds),(2,2))
        self.assertEqual(records[0]['verification']['status'],'passed')
        self.assertEqual(records[0]['generation_attempts'][0]['verification']['status'],'failed')
        self.assertEqual(len(records[0]['repairs']),1)
    def test_timeout_continues_next_question(self):
        records,calls,builds=self.run_fake(timeout=True)
        self.assertEqual(len(records),2)
        self.assertEqual((calls,builds),(3,2))
        self.assertEqual(records[0]['generation'],'completed')
        self.assertEqual(records[0]['generation_attempts'][0]['error'],'timeout')
        self.assertEqual(records[0]['verification']['status'],'passed')
        self.assertEqual(records[1]['verification']['status'],'passed')

    def test_retries_when_no_successful_mcp_response(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for d in ('examples','.github','.vscode','showcase/inputs'): (root/d).mkdir(parents=True,exist_ok=True)
            for n in ('cpp-build-rules.instructions.md','error-correction.md'): (root/'examples'/n).write_text('Rules')
            (root/'.vscode/mcp.json').write_text(json.dumps({'servers':{'words-cpp':{'url':'http://localhost/test'}}}))
            (root/'showcase/inputs/questions.json').write_text(json.dumps({'cases':[{'query_id':'one','question':'Q'}]}))
            empty={'recorded_answer_markdown':'','resolved_models':[],'warnings':['No final assistant answer found.'],'tools':[]}
            valid={'recorded_answer_markdown':'```cpp\nint main(){}\n```','resolved_models':['test'],'warnings':[],'tools':[{'server':'words-cpp','success':True}]}
            results=[empty,valid]
            with patch.object(runner,'ROOT',root),patch.object(sys,'argv',['run','--run','test']),patch.object(runner.shutil,'which',return_value='fake'),patch.object(runner.subprocess,'run',side_effect=[SimpleNamespace(stdout='',stderr='',returncode=0)]*2) as generate,patch.object(runner,'extract',side_effect=results),patch.object(runner.time,'sleep'):
                runner.main()
            records=json.loads((root/'showcase/runs/test/results.json').read_text())
            self.assertEqual(generate.call_count,2)
            self.assertEqual(records[0]['generation'],'completed')
            self.assertIn('No final assistant answer',records[0]['generation_attempts'][0]['retry_reason'])
            self.assertTrue(records[0]['generation_attempts'][1]['mcp_evidence'])

    def test_retry_limit_preserves_failed_attempts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for d in ('examples','.github','.vscode','showcase/inputs'): (root/d).mkdir(parents=True,exist_ok=True)
            for n in ('cpp-build-rules.instructions.md','error-correction.md'): (root/'examples'/n).write_text('Rules')
            (root/'.vscode/mcp.json').write_text(json.dumps({'servers':{'words-cpp':{'url':'http://localhost/test'}}}))
            (root/'showcase/inputs/questions.json').write_text(json.dumps({'cases':[{'query_id':'one','question':'Q'}]}))
            empty={'recorded_answer_markdown':'','resolved_models':[],'warnings':['No final assistant answer found.'],'tools':[]}
            with patch.object(runner,'ROOT',root),patch.object(sys,'argv',['run','--run','test','--generation-retries','0']),patch.object(runner.shutil,'which',return_value='fake'),patch.object(runner.subprocess,'run',return_value=SimpleNamespace(stdout='',stderr='',returncode=0)),patch.object(runner,'extract',return_value=empty):
                with self.assertRaises(SystemExit):runner.main()
            records=json.loads((root/'showcase/runs/test/results.json').read_text())
            self.assertEqual(records[0]['generation'],'failed')
            self.assertEqual(len(records[0]['generation_attempts']),1)
            self.assertIn('No final assistant answer',records[0]['generation_attempts'][0]['retry_reason'])

    def run_no_code_case(self,example_required,answers,retries=2,verify=True,processes=None,with_sdk=False,compile_statuses=None):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for d in ('examples','.github','.vscode','showcase/inputs'): (root/d).mkdir(parents=True,exist_ok=True)
            for n in ('cpp-build-rules.instructions.md','error-correction.md'): (root/'examples'/n).write_text('Rules')
            (root/'.vscode/mcp.json').write_text(json.dumps({'servers':{'words-cpp':{'url':'http://localhost/test'}}}))
            case={'query_id':'one','question':'Q'}
            if example_required:case['example_required']=True
            (root/'showcase/inputs/questions.json').write_text(json.dumps({'cases':[case]}))
            parsed=[{'recorded_answer_markdown':answer,'resolved_models':['test'],'warnings':[],'tools':[{'server':'words-cpp','success':True}]} for answer in answers]
            calls=processes or [SimpleNamespace(stdout='',stderr='',returncode=0)]*len(answers)
            calls=iter(calls);commands=[]
            argv=['run','--run','test','--generation-retries',str(retries)]
            if verify:argv.append('--verify-code')
            if with_sdk:
                header=root/'packages/Aspose.Words.Cpp.26.9.0/build/native/include/Aspose.Words.Cpp/Watermark.h'
                header.parent.mkdir(parents=True);header.write_text('')
                argv.extend(['--packages',str(root/'packages')])
            statuses=iter(compile_statuses) if compile_statuses else None
            def fake_compile(answer,packages,timeout):
                status=next(statuses) if statuses else ('passed' if runner.FENCE.search(answer) else 'no_code')
                blocks=[{'block':1,'status':'failed','diagnostics':'error C2027: undefined type'}] if status=='failed' else []
                return {'status':status,'blocks':blocks,'runtime_executed':False}
            def fake_run(command,**kwargs):
                commands.append(command[:])
                result=next(calls)
                if isinstance(result,Exception):raise result
                return result
            with patch.object(runner,'ROOT',root),patch.object(sys,'argv',argv),patch.object(runner.shutil,'which',return_value='fake'),patch.object(runner.subprocess,'run',side_effect=fake_run),patch.object(runner,'extract',side_effect=parsed),patch.object(runner,'compile_answer',side_effect=fake_compile) as compile_mock,patch.object(runner.time,'sleep'):
                runner.main()
            return (json.loads((root/'showcase/runs/test/results.json').read_text())[0],
                    commands,compile_mock.call_count,
                    (root/'showcase/runs/test/showcase.md').read_text())

    def test_no_code_retry_then_compiles(self):
        code='```cpp\nint main(){}\n```'
        record,calls,builds,report=self.run_no_code_case(True,['Use Watermark.',code],with_sdk=True)
        self.assertEqual((len(calls),builds),(2,2))
        self.assertEqual(record['verification']['status'],'passed')
        self.assertEqual(record['answer'],code)
        self.assertEqual(record['generation_attempts'][0]['verification']['status'],'no_code')
        self.assertIn('no recognized C++ code fence',record['generation_attempts'][0]['retry_reason'])
        self.assertIn('previous response contained no C++ example',calls[1][-1])
        self.assertNotIn('Aspose.Words.Cpp/Watermark.h',calls[0][-1])
        self.assertIn('Aspose.Words.Cpp/Watermark.h',calls[1][-1])
        self.assertNotEqual(calls[0][calls[0].index('--name')+1],calls[1][calls[1].index('--name')+1])
        self.assertNotIn('Example warning:',report)

    def test_no_code_retry_uses_compiler_repair(self):
        broken='```cpp\nint main(){ broken(); }\n```'
        fixed='```cpp\nint main(){ return 0; }\n```'
        record,calls,builds,_=self.run_no_code_case(True,['No code',broken,fixed],compile_statuses=['no_code','failed','passed'])
        self.assertEqual((len(calls),builds),(3,3))
        self.assertEqual(record['answer'],fixed)
        self.assertEqual(record['verification']['status'],'passed')
        self.assertEqual(len(record['repairs']),1)
        self.assertIn('error C2027',calls[2][-1])

    def test_no_code_retry_without_compile(self):
        record,calls,builds,_=self.run_no_code_case(True,['No code','```cpp\nint main(){}\n```'],verify=False)
        self.assertEqual((len(calls),builds),(2,0))
        self.assertEqual(record['verification']['status'],'not_checked')

    def test_unmarked_no_code_does_not_retry(self):
        record,calls,_,_=self.run_no_code_case(False,['Conceptual answer'])
        self.assertEqual(len(calls),1)
        self.assertEqual(record['verification']['status'],'no_code')
        self.assertNotIn('example_warning',record)

    def test_marked_existing_code_does_not_retry(self):
        code='```cpp\nint main(){}\n```'
        record,calls,_,_=self.run_no_code_case(True,[code])
        self.assertEqual(len(calls),1)
        self.assertEqual(record['answer'],code)

    def test_no_code_limit_preserves_first_answer(self):
        record,calls,_,report=self.run_no_code_case(True,['First explanation','Second explanation','Third explanation'])
        self.assertEqual(len(calls),3)
        self.assertEqual(record['generation'],'completed')
        self.assertEqual(record['answer'],'First explanation')
        self.assertEqual(record['verification']['status'],'no_code')
        self.assertEqual(len(record['generation_attempts']),3)
        self.assertIn('Example warning:',report)

    def test_no_code_with_retries_disabled(self):
        record,calls,_,_=self.run_no_code_case(True,['No code'],retries=0)
        self.assertEqual(len(calls),1)
        self.assertIn('example_warning',record)

    def test_no_code_then_timeout_preserves_answer(self):
        processes=[SimpleNamespace(stdout='',stderr='',returncode=0),subprocess.TimeoutExpired('fake',1)]
        record,calls,_,_=self.run_no_code_case(True,['Original explanation'],retries=1,processes=processes)
        self.assertEqual(len(calls),2)
        self.assertEqual(record['answer'],'Original explanation')
        self.assertEqual(record['generation'],'completed')
        self.assertEqual(record['generation_attempts'][1]['error'],'timeout')
        self.assertIn('example_warning',record)

    def test_saved_no_code_answer_is_not_regenerated(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'showcase/inputs').mkdir(parents=True)
            (root/'showcase/inputs/questions.json').write_text(json.dumps({'cases':[{'query_id':'one','question':'Q','example_required':True}]}))
            answer=root/'answer.md';answer.write_text('Saved explanation')
            argv=['run','--run','test','--answer-file',str(answer),'--verify-code']
            with patch.object(runner,'ROOT',root),patch.object(sys,'argv',argv),patch.object(runner.subprocess,'run') as generate:
                runner.main()
            record=json.loads((root/'showcase/runs/test/results.json').read_text())[0]
            generate.assert_not_called()
            self.assertEqual(record['answer'],'Saved explanation')
            self.assertEqual(record['verification']['status'],'no_code')
            self.assertNotIn('example_warning',record)
if __name__=='__main__':unittest.main()
