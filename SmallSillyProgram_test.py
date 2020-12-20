import unittest
from SmallSillyProgram import object

class pytest(unittest.TestCase):

    def firstTest(self):
        ball = object()
        self.assertAlmostEqual(ball.x, 40.0)

    def secondTest(self):
        ball = object()
        self.assertAlmostEqual(ball.y, 460.0)

if __name__=='__main__':
    unittest.main()
