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

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    #ADDED
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(4,3,5),'Right','5,3,4 is a Right triangle')

    #ADDED
    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(10,6,5),'Scalene','10,6,5 is a Scalene triangle')

    #ADDED
    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(6,7,11),'Scalene','6,7,11 is a Scalene triangle')

    #ADDED
    def testScaleneTriangleC(self): 
        self.assertEqual(classifyTriangle(6,14,9),'Scalene','6,14,9 is a Scalene triangle')

    #ADDED
    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(10,6,6),'Isoceles','10,6,6 is a Isoceles triangle')

    #ADDED
    def testIsocelesTriangleB(self): 
        self.assertEqual(classifyTriangle(9,9,12),'Isoceles','9,9,12 is a Isoceles triangle')

    #ADDED
    def testIsocelesTriangleC(self): 
        self.assertEqual(classifyTriangle(7,10,7),'Isoceles','7,10,7 is a Isoceles triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral', '1,1,1 should be equilateral')

    #ADDED
    def testInvalidA(self): 
        self.assertEqual(classifyTriangle(-5,10,7),'InvalidInput','-5,10,7 is an invalid input')

    #ADDED
    def testInvalidB(self): 
        self.assertEqual(classifyTriangle(250,670,250),'InvalidInput','250,670,250 is an invalid input')

    #ADDED
    def testInvalidC(self): 
        self.assertEqual(classifyTriangle("hello","world",250),'InvalidInput','"hello","world",7 is an invalid input')

    #ADDED
    def testNotTriangleA(self): 
        self.assertEqual(classifyTriangle(190,10,7),'NotATriangle','190,10,7 is not a triangle')

    #ADDED
    def testNotTriangleB(self): 
        self.assertEqual(classifyTriangle(10,190,7),'NotATriangle','10,190,7 is not a triangle')

    #ADDED
    def testNotTriangleC(self): 
        self.assertEqual(classifyTriangle(7,190,10),'NotATriangle','7,190,10 is not a triangle')

        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

