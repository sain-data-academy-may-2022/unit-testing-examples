from Rectangle import Rectangle
import pytest


# The test functions to be executed by PyTest

# def test_exception_with_missed_arg():
#     with pytest.raises(Exception):
#         Rectangle(3)

# def test_exception_with_extra_arg():
#     with pytest.raises(Exception):
#         Rectangle(3, 4, 5)

def test_type_error_for_non_int_arg():
    with pytest.raises(TypeError):
        Rectangle('1', 2)

def test_type_error_for_non_positive_arg():
    with pytest.raises(ValueError):
        Rectangle(-1, 2)

def test_can_calc_area():
    rectangle = Rectangle(2, 3)
    assert rectangle.get_area() == 6, "incorrect area"

# edge case
def test_can_calc_area_for_big_numbers():
    rectangle = Rectangle(20000, 30000)
    assert rectangle.get_area() == 600000000, "incorrect area for big numbers"

def test_can_calc_area_after_width_change():
    rectangle = Rectangle(2, 3)
    rectangle.width = 10
    assert rectangle.get_area() == 30, "incorrect area after width change"

# extra
def test_type_error_with_attr_change_to_non_int_value():
    with pytest.raises(ValueError):
        rectangle = Rectangle(2, 3)
        rectangle.width = '1'

def test_type_error_with_attr_change_to_non_positive_value():
    with pytest.raises(ValueError):
        rectangle = Rectangle(2, 3)
        rectangle.width = -3


# class TestGetAreaRectangle:
#     def test_normal_case(self):
#         rectangle = Rectangle(2, 3)
#         assert rectangle.get_area() == 6, "incorrect area"

    # def test_negative_area(self):
    #     rectangle = Rectangle(2, 3)
    #     rectangle.width = -2
    #     rectangle.length = 3
    #     assert rectangle.get_area() == -6, "incorrect area"


# ---------------------------------------------------------------------

# from Rectangle import Rectangle
# import pytest


# @pytest.fixture
# def rectangle():
#     return Rectangle(2, 3)


# # The test function to be executed by PyTest
# def test_normal_case(rectangle):
#     assert rectangle.get_area() == 6, "incorrect area"


# class TestGetAreaRectangle:
#     def test_normal_case(self, rectangle):
#         assert rectangle.get_area() == 6, "incorrect area"

#     def test_another_normal_case(self, rectangle):
#         assert rectangle.get_area() == 6, "incorrect area"

#     def test_negative_area(self, rectangle):
#         rectangle.width = -2
#         rectangle.length = 3
#         assert rectangle.get_area() == -6, "incorrect area"



# -----------------------------------------------
## using just unittest
# import unittest
# from Rectangle import Rectangle


# # The test based on unittest module
# # class TestGetAreaRectangle(unittest.TestCase):
# #     def runTest(self):
# #         rectangle = Rectangle(2, 3)
# #         self.assertEqual(rectangle.get_area(), 6, "incorrect area")
# class TestGetAreaRectangle(unittest.TestCase):
#     def test_normal_case(self):
#         rectangle = Rectangle(2, 3)
#         self.assertEqual(rectangle.get_area(), 6, "incorrect area")
 
#     def test_negative_case(self): 
#         """expect -1 as output to denote error when looking at negative area"""
#         rectangle = Rectangle(-1, 2)
#         self.assertEqual(rectangle.get_area(), -1, "incorrect negative output")

#     def test_geq(self):
#         """tests if value is greater than or equal to a particular target"""
#         self.assertGreaterEqual(self.rectangle.get_area(), 100)

#     def test_assert_raises(self): 
#         """using assertRaises to detect if an expected error is raised when running a particular block of code"""
#         with self.assertRaises(ZeroDivisionError):
#             a = 1 / 0
# # run the test
# unittest.main()
