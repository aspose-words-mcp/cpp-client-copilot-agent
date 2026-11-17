import tempfile,unittest
from pathlib import Path
from compile_cpp import FENCE,compile_answer
from run_copilot import select,reports
class ShowcaseTests(unittest.TestCase):
    def test_fences_preserve_code(self):
        self.assertEqual(FENCE.findall('```cpp\n#include <x.h>\nint main(){}\n```'),['#include <x.h>\nint main(){}\n'])
        self.assertEqual(FENCE.findall('```csharp\ncode\n```'),[])
    def test_no_code_not_pass(self):
        self.assertEqual(compile_answer('Explanation',None)['status'],'no_code')
    def test_missing_sdk_not_pass(self):
        self.assertEqual(compile_answer('```cpp\nint main(){}\n```',None)['status'],'unavailable')
    def test_selection(self):
        cases=[{'query_id':'a'},{'query_id':'b'}]
        self.assertEqual(select(cases),cases[:1]);self.assertEqual(select(cases,'b'),cases[1:])
        with self.assertRaises(ValueError):select(cases,'missing')
    def test_reports_truthful(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);reports(p,[{'query_id':'a','question':'Q','origin':'saved-answer','generation':'completed','answer':'A','verification':{'status':'no_code'}}])
            self.assertIn('Not checked',(p/'showcase.md').read_text());self.assertIn('no_code',(p/'metrics.md').read_text())
if __name__=='__main__':unittest.main()
