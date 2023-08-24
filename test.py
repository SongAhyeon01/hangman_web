import unittest
import app

class HangmanTestCase(unittest.TestCase) :
    
    def test_checkCorrectAnswer(self) :
        answer = app.checkCorrectAnswer("baon", "baboon")
        self.assertTrue(answer)

    def test_checckWrongAnswer(self) :
        answer = app.checkWrongAnswer("zebrio", "zebra")
        self.assertTrue(answer)

if __name__=="__main__" :
    unittest.main()

