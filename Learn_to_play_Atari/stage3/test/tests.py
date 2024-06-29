from hstest import CheckResult, StageTest, dynamic_test,TestedProgram,WrongAnswer
import os
from stable_baselines3 import DQN

class TrainingTest(StageTest):
    @dynamic_test
    def test_training(self):
        try:
            pr = TestedProgram()
            result = pr.start()
            model_path = os.path.join(os.getcwd(), "logs/saved/DQN_Breakout_500000")
            if not os.path.isdir(model_path):
                raise WrongAnswer(f"model couldnt be found at {model_path}")
            try:
                model = DQN.load(model_path)
            except:
                raise WrongAnswer("Couldn't load the model. Make sure the training is completed successfully.")
            return CheckResult.correct()
        except Exception as e:
            raise WrongAnswer(f"An error occurred during testing: {str(e)}")


if __name__ == '__main__':
    TrainingTest().run_tests()
