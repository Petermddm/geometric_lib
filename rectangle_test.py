import unittest
from rectangle import *
class RectangleTestCase(unittest.TestCase):
    def test_first_value_zero_area(self):
        res = area(0, 10)
        self.assertEqual(res, 0)
    
    def test_second_value_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_both_values_positive_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
        res = area(2, 5)
        self.assertEqual(res, 10)
    
    def test_first_value_negative_area(self):
        res = area(-1, 10)
        self.assertEqual(res, 0)
    
    def test_second_value_negative_area(self):
        res = area(10, -1)
        self.assertEqual(res, 0)
    
    def test_both_values_negative_area(self):
        res = area(-1, -1)
        self.assertEqual(res, 0)

    def test_first_value_zero_perimeter(self):
        res = perimeter(0, 10)
        self.assertEqual(res, 20)
    
    def test_second_value_zero_perimeter(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)
    
    def test_both_values_positive_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
        res = perimeter(5, 2)
        self.assertEqual(res, 14)
    
    def test_first_value_negative_perimeter(self):
        res = perimeter(-1, 10)
        self.assertEqual(res, 0)
    
    def test_second_value_negative_perimeter(self):
        res = perimeter(10, -1)
        self.assertEqual(res, 0)
    
    def test_both_values_negative_perimeter(self):
        res = perimeter(-1, -1)
        self.assertEqual(res, 0)
    
