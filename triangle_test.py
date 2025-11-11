import unittest
from triangle import *
class TriangleTestCase(unittest.TestCase):
    def test_first_value_zero_area(self):
        res = area(0, 10)
        self.assertEqual(res, 0)
    def test_second_value_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    def test_both_values_positive_area(self):
        res = area(10, 10)
        self.assertEqual(res, 50)
        res = area(2, 5)
        self.assertEqual(res, 5)
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
        res = perimeter(0, 10, 5)
        self.assertEqual(res, 0)
    def test_second_value_zero_perimeter(self):
        res = perimeter(10, 0, 5)
        self.assertEqual(res, 0)
    def test_thirdth_values_positive_perimeter(self):
        res = perimeter(5, 10, 0)
        self.assertEqual(res, 0)
    def test_first_value_negative_perimeter(self):
        res = perimeter(-1, 10, 5)
        self.assertEqual(res, 0)
    def test_second_value_negative_perimeter(self):
        res = perimeter(10, -1, 5)
        self.assertEqual(res, 0)
    def test_thirdth_value_negative_perimeter(self):
        res = perimeter(10, 5, -1)
        self.assertEqual(res, 0)
    def test_all_values_negative_perimeter(self):
        res = perimeter(-1, -1, -1)
        self.assertEqual(res, 0)
    def test_all_values_positive_and_triangle_is_real_perimeter(self):
        res = perimeter(5, 4, 3)
        self.assertEqual(res, 12)
    def test_triangle_is_not_real_perimeter(self):
        res = perimeter(1, 1, 3)
        self.assertEqual(res, 0)
    
