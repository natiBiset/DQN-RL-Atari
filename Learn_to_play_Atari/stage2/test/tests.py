from hstest import StageTest, dynamic_test, CheckResult,TestedProgram,WrongAnswer
import os

class DQNSetupTest(StageTest):
    @dynamic_test
    def test_dqn_setup(self):
        try:
            pr = TestedProgram()
            result = pr.start()
            log_dir =  os.path.join(os.getcwd(), "logs/training")
            if not os.path.isdir(log_dir):
                raise WrongAnswer(f"Log folder not found. Make sure you have created it in the folder {os.getcwd()}")
            return CheckResult.correct()
        except Exception as e:
            raise WrongAnswer(f"An error occurred during testing: {str(e)}")


if __name__ == '__main__':
    DQNSetupTest().run_tests()



