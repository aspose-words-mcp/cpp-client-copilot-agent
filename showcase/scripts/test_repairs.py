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
            result=sdk_header_context(tmp)
            self.assertIn('Aspose.Words.Cpp/Document.h',result)
            self.assertNotIn(tmp,result)
            self.assertNotIn('Range.h',result)
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
if __name__=='__main__':unittest.main()
