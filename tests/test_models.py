import unittest
from unittest.mock import patch
from aider.models import Model
from aider.models import validate_variables
from aider.models import branch_coverage


class TestModels(unittest.TestCase):
    def test_max_context_tokens(self):
        model = Model("gpt-3.5-turbo")
        self.assertEqual(model.info["max_input_tokens"], 16385)

        model = Model("gpt-3.5-turbo-16k")
        self.assertEqual(model.info["max_input_tokens"], 16385)

        model = Model("gpt-3.5-turbo-1106")
        self.assertEqual(model.info["max_input_tokens"], 16385)

        model = Model("gpt-4")
        self.assertEqual(model.info["max_input_tokens"], 8 * 1024)

        model = Model("gpt-4-32k")
        self.assertEqual(model.info["max_input_tokens"], 32 * 1024)

        model = Model("gpt-4-0613")
        self.assertEqual(model.info["max_input_tokens"], 8 * 1024)

    def test_get_weak_model_1(self):
        model = Model("gpt-4", weak_model = "gpt-3.5-turbo")
        for branch, hit in branch_coverage.items():
             print(f"{branch} was {'hit' if hit else 'not hit'}")
        self.assertTrue(branch_coverage['weak model 1'])
    
    def test_token_count_branch(self):
        model = Model("gpt-3.5-turbo")
        
        # Save the original tokenizer method
        original_tokenizer = model.tokenizer

        # Temporarily remove the tokenizer method to hit the branch
        model.tokenizer = None

        # Call token_count to hit the branch
        model.token_count("test message")

        # Check if the branch was hit
        self.assertTrue(branch_coverage['tokenizer_branch_hit'])

        # Restore the original tokenizer method
        model.tokenizer = original_tokenizer



class TestModelsValidateVariables(unittest.TestCase):

    def test_validate_variables_all_present(self):
        with patch('aider.models.os.environ', {'var1', 'var2'}):
            branch_coverage["val_var_branch_1"] = False
            branch_coverage["val_var_branch_2"] = False
            res = validate_variables(['var1', 'var2'])
            for branch, hit in branch_coverage.items():
                print(f"{branch} was {'hit' if hit else 'not hit'}")
            self.assertTrue(res['keys_in_environment'])
            self.assertEqual(res['missing_keys'], [])


    def test_validate_variables_one_missing(self):
        with patch('aider.models.os.environ', {'var1'}):
            branch_coverage["val_var_branch_1"] = False
            branch_coverage["val_var_branch_2"] = False
            res = validate_variables(['var1', 'var2'])
            for branch, hit in branch_coverage.items():
                print(f"{branch} was {'hit' if hit else 'not hit'}") 
            self.assertFalse(res['keys_in_environment'])
            self.assertEqual(res['missing_keys'], ['var2'])

    
    def test_validate_variables_all_missing(self):
        with patch('aider.models.os.environ', {}):
            branch_coverage["val_var_branch_1"] = False
            branch_coverage["val_var_branch_2"] = False
            res = validate_variables(['var1', 'var2'])
            for branch, hit in branch_coverage.items():
                print(f"{branch} was {'hit' if hit else 'not hit'}")
            self.assertFalse(res['keys_in_environment'])
            self.assertEqual(res['missing_keys'], ['var1', 'var2'])



class TestModelConfigureSettings(unittest.TestCase):
    
    def setUp(self):
        self.model = Model("dummy_model")

    def test_configure_model_settings_llama3_70b(self):
        self.model.configure_model_settings("llama-3-70b")
        for branch, hit in branch_coverage.items():
            print(f"{branch} was {'hit' if hit else 'not hit'}")
        self.assertEqual(self.model.edit_format, "diff")
        self.assertTrue(self.model.use_repo_map)
        self.assertTrue(self.model.send_undo_reply)
        self.assertTrue(self.model.examples_as_sys_msg)

    def test_configure_model_settings_gpt_4_turbo_preview(self):
        self.model.configure_model_settings("gpt-4-turbo-preview")
        for branch, hit in branch_coverage.items():
            print(f"{branch} was {'hit' if hit else 'not hit'}")
        self.assertEqual(self.model.edit_format, "udiff")
        self.assertTrue(self.model.use_repo_map)
        self.assertTrue(self.model.send_undo_reply)

    def test_configure_model_settings_gpt_4_opus(self):
        self.model.configure_model_settings("claude-3-opus")
        for branch, hit in branch_coverage.items():
            print(f"{branch} was {'hit' if hit else 'not hit'}")
        self.assertEqual(self.model.edit_format, "diff")
        self.assertTrue(self.model.use_repo_map)
        self.assertTrue(self.model.send_undo_reply)

    def test_configure_model_settings_gpt_35(self):
        self.model.configure_model_settings("gpt-3.5")
        for branch, hit in branch_coverage.items():
            print(f"{branch} was {'hit' if hit else 'not hit'}")
        self.assertTrue(self.model.reminder_as_sys_msg)

if __name__ == "__main__":
    unittest.main()
