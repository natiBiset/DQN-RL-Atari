from hstest import CheckResult, StageTest, dynamic_test,TestedProgram,WrongAnswer
import os
import re
import ast

class EvaluatingModelTest(StageTest):
    
    @dynamic_test()
    def test_evaluating_model(self):
        try:
            pr = TestedProgram()
            result = pr.start()
            try:
                data = ast.literal_eval(result)
            except:
                raise WrongAnswer("Make sure you have called 'evaluate_policy' correctly.")
            return CheckResult.correct()
        
        except Exception as e:
            raise WrongAnswer(f"An error occurred during testing: {str(e)}")


if __name__ == "__main__":
    EvaluatingModelTest().run_tests()

