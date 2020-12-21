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
    
    def test_movement_right(self):
        x = 50
        y = 700 - 76
        colour = (50,50,50)
        r = 5
        direction = 1
        bullet = snaryad(x,y,r,colour,direction)
        bullet.movement(1)
        self.assertAlmostEqual((bullet.x,bullet.y), (58, 700 - 76))
    
    def test_movement_left(self):
        x = 50
        y = 700 - 76
        colour = (50,50,50)
        r = 5
        direction = -1
        bullet = snaryad(x,y,r,colour,direction)
        bullet.movement(1)
        self.assertAlmostEqual((bullet.x,bullet.y), (42, 700 - 76))
    def test_positive_speed(self):
        x = 50
        y = 700 - 76
        colour = (50,50,50)
        r = 5
        direction = 1
        bullet = snaryad(x,y,r,colour,direction)
        a=bullet.movement(2)
        b=bullet.movement(1)
        self.assertAlmostEqual(b-a, 8)
    def test_negative_speed(self):
        x = 50
        y = 700 - 76
        colour = (50,50,50)
        r = 5
        direction = -1
        bullet = snaryad(x,y,r,colour,direction)        
        a=bullet.movement(2)
        b=bullet.movement(1)
        self.assertAlmostEqual(b-a, -8)

if __name__=='__main__':
    unittest.main()

