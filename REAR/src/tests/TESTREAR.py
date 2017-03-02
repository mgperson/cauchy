import unittest

from ..REAR import REAR

class TestREAR(unittest.TestCase):
    def setUp(self):
        self.rear = REAR()
        self.sample = [8,6,7,9,4,1,3,10,2,5]
        self.goal = [8,2,7,6,9,1,5,3,10,4]

    def test_is_hamming_distance_correct(self):
        self.assertEqual(self.rear.get_hamming_distance(self.sample,self.goal),7)

    def test_get_all_possible_flips_is_correct(self):
        expected = [[2,1,3],[3,2,1],[1,3,2]]
        self.assertEqual(self.rear.get_all_possible_flips([1,2,3]),expected)

    def test_get_all_possible_flips_starting_at_position_i_is_correct(self):
        expected = [[1,3,2]]
        self.assertEqual(self.rear.get_all_possible_flips_starting_at_position_i([1,2,3],1),expected)

    def test_get_flip_with_lowest_hamming_distance(self):
        goal = [1,3,2,4]
        expected = [0,goal]
        start_perm = self.rear.get_all_possible_flips([1,2,3,4])
        self.assertEqual(self.rear.get_result_with_lowest_hamming_distance(start_perm,goal,[]),expected)

    def test_get_flip_with_lowest_hamming_distance_of_all_possible_flips(self):
        expected,goal  = [0,[1,2,4,3]], [1,2,4,3]
        start_perm = [1,2,3,4]
        self.assertEqual(self.rear.get_flip_with_lowest_hamming_distance_of_all_possible_flips(start_perm,goal,[]),expected)

    @unittest.skip('Skip until we come up with a good test case')
    def test_get_flip_with_lowest_hamming_distance_of_all_possible_flips_starting_at_position_i(self):
        pass


    def test_get_position_of_first_difference(self):
        expected = 1
        self.assertEqual(self.rear.get_position_of_first_difference(self.sample,self.goal),expected)

    def test_get_flip_with_correct_number_at_position_i(self):
        expected = [8,2,10,3,1,4,9,7,6,5]
        self.assertEqual(self.rear.get_flip_with_correct_number_at_position_i(self.sample,self.goal,1),expected)

    def test_get_flip_with_correct_number_at_first_position_with_difference(self):
        expected = [8,2,10,3,1,4,9,7,6,5]
        self.assertEqual(self.rear.get_flip_with_correct_number_at_first_position_with_difference(self.sample,self.goal),expected)

    def test_interval_start_index_greater_than_end_index_throws_exception(self):
        perm = [5,3,2,1,4]
        self.assertRaises(IndexError,self.rear.flip_interval,perm,3,2)

    def test_interval_start_index_equal_end_index_throws_exception(self):
        perm = [5, 3, 2, 1, 4]
        self.assertRaises(IndexError, self.rear.flip_interval, perm, 3, 3)

    def test_is_interval_flip_correct(self):
        perm = [5,3,2,1,4]
        expected = [5,3,4,1,2]
        self.assertEqual(self.rear.flip_interval(perm,2,4),expected)
        expected = [5,1,2,3,4]
        self.assertEqual(self.rear.flip_interval(perm, 1, 3), expected)
        expected = [2,3,5,1,4]
        self.assertEqual(self.rear.flip_interval(perm, 0, 2), expected)

    #@unittest.skip('Skip for now')
    def test_sample_flip_solution_is_correct(self):
        expected = 5
        self.assertEqual(self.rear.find_reversal_distance(self.sample,self.goal),expected)
