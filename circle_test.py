import unittest
from circle import *
class CircleTestCase(unittest.TestCase):
    def test_value_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
        
    def test_value_positive_area(self):
        res = area(10)
        self.assertEqual(res, math.pi * 10 * 10)
        res = area(5)
        self.assertEqual(res, math.pi * 5 * 5)
    
    def test_value_negative_area(self):
        res = area(-1)
        self.assertEqual(res, 0)

    def test_value_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_value_positive_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 2 * math.pi * 10)
        res = perimeter(5)
        self.assertEqual(res, 2 * math.pi * 5)
    
    def test_value_negative_perimeter(self):
        res = perimeter(-1)
        self.assertEqual(res, 0)
    
