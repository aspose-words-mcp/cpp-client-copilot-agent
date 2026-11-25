import tempfile,unittest
from pathlib import Path
from compile_cpp import FENCE,compile_answer,candidates,wrap_statements
from run_copilot import select,reports,generation_prompt,showcase_answer,missing_entry_points
class ShowcaseTests(unittest.TestCase):
    def test_fences_preserve_code(self):
        self.assertEqual(FENCE.findall('```cpp\n#include <x.h>\nint main(){}\n```'),['#include <x.h>\nint main(){}\n'])
        self.assertEqual(FENCE.findall('```csharp\ncode\n```'),[])
    def test_no_code_not_pass(self):
        self.assertEqual(compile_answer('Explanation',None)['status'],'no_code')
    def test_missing_sdk_not_pass(self):
        self.assertEqual(compile_answer('```cpp\nint main(){}\n```',None)['status'],'unavailable')
    def test_main_unchanged(self):
        code='int main() { return 0; }'
        self.assertEqual(list(candidates(code)),[('original',code)])
    def test_statement_wrapper(self):
        source=wrap_statements('#include <bad-header.h>\nthing->Save();')
        self.assertTrue(source.startswith('#include <bad-header.h>\nint main()'))
        self.assertIn('thing->Save();',source)
    def test_context_recorded(self):
        options=dict(candidates('doc->Save();','auto doc = make_doc();'))
        self.assertIn('auto doc = make_doc();',options['shared_context_main'])
        self.assertIn('doc->Save();',options['shared_context_main'])
    def test_conditional_not_hoisted(self):
        self.assertIsNone(wrap_statements('#if X\n#include <x>\n#endif'))
    def test_prompt_requests_complete_program(self):
        self.assertIn('int main()',generation_prompt('Convert a document'))
    def test_report_uses_tested_program(self):
        record={'answer':'```cpp\ndoc->Save();\n```','verification':{'blocks':[{'block':1,'strategy':'statement_main','compiled_source':'int main() { doc->Save(); }'}]}}
        rendered=showcase_answer(record)
        self.assertEqual(len(FENCE.findall(rendered)),1)
        self.assertIn('int main()',rendered)
        self.assertIn('Compilation harness',rendered)
    def test_report_flags_unwrapped_fragment(self):
        record={'answer':'```cpp\ndoc->Save();\n```','verification':{}}
        self.assertEqual(FENCE.findall(showcase_answer(record)),[])
        self.assertIn('Incomplete code block',showcase_answer(record))
        self.assertEqual(missing_entry_points(record['answer']),[1])
    def test_selection(self):
        cases=[{'query_id':'a'},{'query_id':'b'}]
        self.assertEqual(select(cases),cases[:1]);self.assertEqual(select(cases,'b'),cases[1:])
        with self.assertRaises(ValueError):select(cases,'missing')
    def test_reports_truthful(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);reports(p,[{'query_id':'a','question':'Q','origin':'saved-answer','generation':'completed','answer':'A','verification':{'status':'no_code'}}])
            text=(p/'showcase.md').read_text()
            self.assertIn('Not checked',text);self.assertIn('Replayed answers are not live Copilot generations.',text)
            self.assertIn('no_code',(p/'metrics.md').read_text())
            records=[{'query_id':'a','question':'Q','origin':'copilot-cli','generation':'completed','answer':'A','verification':{'status':'passed'}}]
            reports(p,records)
            self.assertIn('Answers were generated in Copilot CLI sessions.',(p/'showcase.md').read_text())
            records.append({'query_id':'b','question':'Q2','origin':'saved-answer','generation':'completed','answer':'B','verification':{'status':'no_code'}})
            reports(p,records)
            self.assertIn('Generation origin is listed per question',(p/'showcase.md').read_text())
if __name__=='__main__':unittest.main()
