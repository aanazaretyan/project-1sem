from project import snaryad
import project
import unittest

class snaryadTest(unittest.TestCase):
    def test_draw(self):
    snaryad(project.x,project.y,5,project.colour,project.direction)
    print((project.x,project.y))
    self.assertAlmostEqual((project.x,project.y), (50,700 - 76))


if __name__=='__main__':
    unittest.main()

