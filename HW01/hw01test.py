import unittest
import hw01

class TestTriangles(unittest.TestCase):
    def testScalene(self): #test for scalene and right triangles
        self.assertEqual(hw01.classify_triangle(3,4,5),'Scalene and Right')
        self.assertEqual(hw01.classify_triangle(4,5,6),'Scalene')
        self.assertEqual(hw01.classify_triangle(5,6, 7),'Scalene')
        self.assertEqual(hw01.classify_triangle(5, 12, 13),'Scalene and Right')
        
    def testIsosceles(self): #test for isosceles triangles
        self.assertEqual(hw01.classify_triangle(1,1,2),'Isosceles')
        self.assertEqual(hw01.classify_triangle(10,10,20),'Isosceles')
        self.assertEqual(hw01.classify_triangle(6,10,6),'Isosceles')

    def testEquilateral(self): #test for equilateral triangles
        self.assertEqual(hw01.classify_triangle(3, 3, 3),'Equilateral')
        self.assertEqual(hw01.classify_triangle(30, 30, 30),'Equilateral')
        self.assertEqual(hw01.classify_triangle(5, 5, 5),'Equilateral')


if __name__ == '__main__':
    unittest.main(exit=True)