# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    
    #Tests for Right Triangles
    def testRightTriangle1(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangle2(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5,12,13 is a Right triangle')

    #Tests for Equilateral Triangles
    def testEquilateralTriangle1(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 is an Equilateral triangle')

    def testEquilateralTriangle2(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '10,10,10 is an Equilateral triangle')

    #Tests for Isosceles Triangles
    def testIsoscelesTriangle1(self):
        self.assertEqual(classifyTriangle(4, 4, 6), 'Isosceles', '4,4,6 is an Isosceles triangle')
    
    def testIsoscelesTriangle2(self):
        self.assertEqual(classifyTriangle(9, 9, 5), 'Isosceles', '9,9,5 is an Isosceles triangle')

    #Tests for Scalene Triangles
    def testScaleneTriangle1(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene', '4,5,6 is a Scalene triangle')

    def testScaleneTriangle2(self):
        self.assertEqual(classifyTriangle(20,30,40), 'Scalene', '20,30,40 is a Scalene triangle')

    # Triangles that violate constraints for eligible triangle sides
    def testNotATriangle1(self):
        self.assertEqual(classifyTriangle(1, 9, 10), 'NotATriangle', '1,9,10 is not a valid triangle')

    def testNotATriangle2(self):
        self.assertEqual(classifyTriangle(7, 2, 2), 'NotATriangle', '7,2,2 is not a valid triangle')
    
    # Invalid inputs: one or more sides less than or equal to zero
    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', '0,0,0 is an invalid input')

    def testInvalidInput2(self):
        self.assertEqual(classifyTriangle(-5, 5, 5), 'InvalidInput', '-5,5,5 is an invalid input')

    def testInvalidInput3(self):
        self.assertEqual(classifyTriangle(200, 200, 205), 'InvalidInput', '200,200,205 exceeds input limits')

    # Non-integer inputs
    def testInvalidInputNonInteger(self):
        self.assertEqual(classifyTriangle(2.5, 3.2, 4.1), 'InvalidInput', 'Non-integer values should be invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

