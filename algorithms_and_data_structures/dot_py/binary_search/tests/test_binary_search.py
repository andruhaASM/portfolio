import unittest

import binary_search

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.int_list = [1, 3, 5, 10, 99, 987, 1034, 1035]
        self.float_list = [0.01, 0.02, 0.05, 0.1, 0.2, 0.234, 0.5]
        self.empty_list = []
        self.one_element_list = [4]

    def test_binary_search_returns_correct_value(self):
        int_result = binary_search.binary_search(self.int_list, 99)
        expected_int_result = (99, 4)

        float_result = binary_search.binary_search(
            self.float_list,
            0.2
        )
        expected_float_result = (0.2, 4)

        one_element_result = binary_search.binary_search(
            self.one_element_list,
            4
        )
        expected_one_element_result = (4, 0)

        not_found_result = binary_search.binary_search(
            self.int_list,
            -2
        )
        expected_not_found_result = (-2, None)

        self.assertEqual(int_result, expected_int_result)
        self.assertEqual(float_result, expected_float_result)
        self.assertEqual(
            one_element_result,
            expected_one_element_result
        )
        self.assertEqual(not_found_result, expected_not_found_result)
        
