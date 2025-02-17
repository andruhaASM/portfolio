import unittest

import selection_sort

class TestSelectionSort(unittest.TestCase):
    def setUp(self):
        self.int_list = [1, -10, 5, 10, 0, 100, 2, 3, 4, 4]
        self.float_list = [-0.01, 0.003, 0.0002, 0.1, 0.5]
        self.empty_list = []
        self.one_element_list = [4]

    def test_selection_sort_success(self):
        int_result = selection_sort.selection_sort(self.int_list)
        expected_int_result = [-10, 0, 1, 2, 3, 4, 4, 5, 10, 100 ]

        float_result = selection_sort.selection_sort(self.float_list)
        expected_float_result = [-0.01, 0.0002, 0.003, 0.1, 0.5]

        one_element_result = selection_sort.selection_sort(
            self.one_element_list
        )
        expected_one_element_result = [4]
        self.assertEqual(int_result, expected_int_result)
        self.assertEqual(float_result, expected_float_result)
        self.assertEqual(
            one_element_result,
            expected_one_element_result
        )
        
