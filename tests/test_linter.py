
import os
import unittest
from unittest.mock import MagicMock, patch

from aider.linter import Linter, LintResult


class TestLinter(unittest.TestCase):
    @patch('aider.linter.subprocess.Popen')
    def test_run_cmd(self, mock_popen):
        linter = Linter(root='/path/to/repo')
        cmd = 'flake8'
        rel_fname = 'test.py'
        code = 'print("Hello, world!")'
        
        mock_process = MagicMock()
        mock_process.communicate.return_value = (b'Some error message\n', None)
        mock_process.returncode = 1
        mock_popen.return_value = mock_process
        
        result = linter.run_cmd(cmd, rel_fname, code)
        
        self.assertIsInstance(result, LintResult)
        self.assertIn('## Running: flake8 test.py', result.text)
        self.assertIn('Some error message', result.text)
        self.assertEqual(result.lines, [])  

    @patch('aider.linter.Linter.run_cmd')
    @patch('aider.linter.basic_lint')
    @patch('aider.linter.lint_python_compile')
    def test_py_lint(self, mock_lint_python_compile, mock_basic_lint, mock_run_cmd):
        linter = Linter(root='/path/to/repo')
        fname = 'test.py'
        rel_fname = 'test.py'
        code = 'print("Hello, world!")'
        
        mock_basic_lint.return_value = LintResult(text='Basic lint error', lines=[1])
        
        mock_lint_python_compile.return_value = LintResult(text='Compile error', lines=[2])
        
        mock_run_cmd.return_value = LintResult(text='Flake8 error', lines=[3])
        
        result = linter.py_lint(fname, rel_fname, code)
        
        self.assertIsInstance(result, LintResult)
        self.assertIn('Basic lint error', result.text)
        self.assertIn('Compile error', result.text)
        self.assertIn('Flake8 error', result.text)
        self.assertEqual(result.lines, {1, 2, 3})
        
        mock_basic_lint.assert_called_once_with(rel_fname, code)
        mock_lint_python_compile.assert_called_once_with(fname, code)
        mock_run_cmd.assert_called_once_with('flake8 --select=E9,F821,F823,F831,F406,F407,F701,F702,F704,F706 --show-source --isolated', rel_fname, code)

if __name__ == '__main__':
    unittest.main()


