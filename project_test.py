from project import snaryad
import project
import unittest

class snaryadTest(unittest.TestCase):
    def test_draw(self):
        x = 50
        y = 700 - 76
        colour = (50,50,50)
        r = 5
        direction = 1
        bullet = snaryad(x,y,r,colour,direction)
        self.assertAlmostEqual((bullet.x,bullet.y), (50,700 - 76))


if __name__=='__main__':
    unittest.main()

