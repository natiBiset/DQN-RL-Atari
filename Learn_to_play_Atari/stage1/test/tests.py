from hstest import CheckResult, StageTest, dynamic_test,TestedProgram,WrongAnswer
import gymnasium as gym

class GymnasiumSetupTest(StageTest):
    @dynamic_test
    def test_preprocessing(self):
        try:
            pr = TestedProgram()
            result = pr.start()
            try:
                env = gym.make('ALE/Breakout-v5')
            except:
                WrongAnswer(f'Cannot load the Breakout environment. Make sure you have installed stable baselines3')
            result = result.strip()
            words = ['action','observation','space','(',')']
            for word in words:
                if word in result:
                    pass
                else:
                    return WrongAnswer(f'make sure you have printed using the same format as the given example.')
            return CheckResult.correct()
        except Exception as e:
            raise WrongAnswer(f"An error occurred during testing: {str(e)}")


if __name__ == '__main__':
    GymnasiumSetupTest().run_tests()
