# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangle(unittest.TestCase):
    '''# define multiple sets of tests as functions with names that begin'''
    def test_right_triangle_a(self):
        '''checks for right angle triangle'''
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def test_right_triangle_b(self):
        '''checks for right angle triangle'''
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
    def test_equilateral_triangles_a(self):
        '''checks for equilateral triangle'''
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    def test_equilateral_triangles_b(self):
        '''checks for equilateral triangle'''
        self.assertEqual(classify_triangle(2,2,2),'Equilateral','2,2,2 should be equilateral')
    def test_scalene_triangles(self):
        '''checks for scalene triangle'''
        self.assertEqual(classify_triangle(5,6,3),'Scalene','5,6,3 should be scalene')
    def test_not_a_triangles(self):
        '''checks for not a triangle'''
        self.assertEqual(classify_triangle(6,2,1),'NotATriangle','6,2,1 is not a triangle')
    def test_invalid_input_a(self):
        '''checks for invalid input'''
        self.assertEqual(classify_triangle(620,23,1),'InvalidInput','620,23,1 is invalid input')
    def test_invalid_input_b(self):
        '''checks for invalid input'''
        self.assertEqual(classify_triangle(-3,2,-1),'InvalidInput','-3,2,-1 is invalid input')
    def test_invalid_input_c(self):
        '''checks for invalid input'''
        self.assertEqual(classify_triangle("x",23,1),'InvalidInput','"x",23,1 is invalid input')
    def test_isoceles_triangle_a(self):
        '''checks for isoceles triangle'''
        self.assertEqual(classify_triangle(3,3,4),'Isoceles','3,3,4 is an isoceles triangle')
    def test_isoceles_triangle_b(self):
        '''checks for isoceles triangle'''
        self.assertEqual(classify_triangle(4,5,4),'Isoceles','4,5,4 is an isoceles triangle')
    def test_right_triangle_c(self):
        '''checks for right angle triangle'''
        self.assertEqual(classify_triangle(4,3,5),'Right','5,12,13 is a Right triangle')
    def test_equilateral_triangle_c(self):
        '''checks for equilateral triangle'''
        self.assertEqual(classify_triangle(12,12,12),'Equilateral','12,12,12 should be equilateral')
    def test_scalene_triangle_b(self):
        '''checks for scalene triangle'''
        self.assertEqual(classify_triangle(6,7,4),'Scalene','6,7,4 is a scalene triangle')
    def test_not_a_triangle(self):
        '''checks for not a triangle'''
        self.assertEqual(classify_triangle(7,3,2),'NotATriangle','7,3,2 is not a triangle')
    def test_invalid_input_d(self):
        '''checks for invalid input'''
        self.assertEqual(classify_triangle(700,25,2),'InvalidInput','700,25,2 is invalid input')
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
