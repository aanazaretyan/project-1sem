import pygame
import unittest

from SmallSillyProgram import objectq

class testOfTheTest(unittest.TestCase):

    def test_firstTest(self):
        x = 40.0
        y = 460.0
        colour = (255,255,255)
        speed_x = 0.5
        speed_y = 0.5
        ball = objectq(x,y,colour,speed_x,speed_y)
        self.assertEqual(ball.colour, (255,255,255))

    def test_secondTest(self):
        x = 40.0
        y = 460.0
        colour = (255,255,255)
        speed_x = 0.5
        speed_y = 0.5
        ball = objectq(x,y,colour,speed_x,speed_y)
        self.assertNotEqual(ball.colour, (255,0,0))

    def test_thirdTest(self):
        x = 40.0
        y = 460.0
        colour = (255,255,255)
        speed_x = 0.5
        speed_y = 0.5
        ball = objectq(x,y,colour,speed_x,speed_y)
        ball.movement()
        self.assertEqual(ball.x, (39.5))
        self.assertEqual(ball.y, (459.5))


if __name__ == "__main__":
    unittest.main()