# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    """define multiple sets of tests as functions with names that begin""" 
    #Tests for Right Triangles
    def test_right_triangle_1(self):
        """Tests for Right Triangle 1"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def test_right_triangle_2(self):
        """Tests for Right Triangle 2"""
        self.assertEqual(classify_triangle(5, 12, 13), 'Right', '5,12,13 is a Right triangle')

    #Tests for Equilateral Triangles
    def test_equilateral_triangle_1(self):
        """Tests for Equilateral Triangle 1"""
        self.assertEqual(classify_triangle(1, 1, 1),
                         'Equilateral', '1,1,1 is an Equilateral triangle')

    def test_equilateral_triangle_2(self):
        """Tests for Equilateral Triangle 2"""
        self.assertEqual(classify_triangle(10, 10, 10),
                         'Equilateral', '10,10,10 is an Equilateral triangle')

    #Tests for Isosceles Triangles
    def test_isosceles_triangle_1(self):
        """Tests for Isosceles Triangle 1"""
        self.assertEqual(classify_triangle(4, 4, 6), 'Isosceles', '4,4,6 is an Isosceles triangle')
    def test_isosceles_triangle_2(self):
        """Tests for Isosceles Triangle 2"""
        self.assertEqual(classify_triangle(9, 9, 5), 'Isosceles', '9,9,5 is an Isosceles triangle')

    #Tests for Scalene Triangles
    def test_scalene_triangle_1(self):
        """Tests for Scalene Triangle 1"""
        self.assertEqual(classify_triangle(4, 5, 6), 'Scalene', '4,5,6 is a Scalene triangle')

    def test_scalene_triangle_2(self):
        """Tests for Scalene Triangle 2"""
        self.assertEqual(classify_triangle(20,30,40), 'Scalene', '20,30,40 is a Scalene triangle')

    # Triangles that violate constraints for eligible triangle sides
    def test_not_a_triangle_1(self):
        """Triangles that violate constraints for eligible triangle sides (1)"""
        self.assertEqual(classify_triangle(1, 9, 10),
                         'NotATriangle', '1,9,10 is not a valid triangle')

    def test_not_a_triangle_2(self):
        """Triangles that violate constraints for eligible triangle sides (2)"""
        self.assertEqual(classify_triangle(7, 2, 2),
                         'NotATriangle', '7,2,2 is not a valid triangle')

    # Invalid inputs: one or more sides less than or equal to zero
    def test_invalid_input1(self):
        """Invalid inputs: one or more sides less than or equal to zero (1)"""
        self.assertEqual(classify_triangle(0, 0, 0), 'InvalidInput', '0,0,0 is an invalid input')

    def test_invalid_input2(self):
        """Invalid inputs: one or more sides less than or equal to zero (2)"""
        self.assertEqual(classify_triangle(-5, 5, 5), 'InvalidInput', '-5,5,5 is an invalid input')

    def test_invalid_input3(self):
        """Invalid inputs: one or more sides less than or equal to zero (3)"""
        self.assertEqual(classify_triangle(200, 200, 205),
                         'InvalidInput', '200,200,205 exceeds input limits')

    # Non-integer inputs
    def test_invalid_input_non_integer(self):
        """Non-integer inputs"""
        self.assertEqual(classify_triangle(2.5, 3.2, 4.1),
                         'InvalidInput', 'Non-integer values should be invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
