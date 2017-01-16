import unittest

from ..LGIS import LGIS

class TestLGIS(unittest.TestCase):
    def setUp(self):
        self.lgis = LGIS()
        self.sample_n = 5
        self.sample_permutation = [5,1,4,2,3]

    def test_subequences_of_51423_of_length_4_are_correct(self):
        expected_result = [(5,1,4,2),(5,1,4,3),(5,1,2,3),(5,4,2,3),(1,4,2,3)]
        self.assertEqual(self.lgis.get_subsequences_with_length_n(self.sample_permutation,4),expected_result)

    def test_is_sequence_increasing_is_correct_for_123(self):
        self.assertTrue(self.lgis.is_sequence_increasing([1,2,3]))

    def test_is_sequence_increasing_is_false_for_132(self):
        self.assertFalse(self.lgis.is_sequence_increasing([1,3,2]))

    def test_is_sequence_decreasing_is_correct_for_321(self):
        self.assertTrue(self.lgis.is_sequence_decreasing([3,2,1]))

    def test_is_sequence_decreasing_is_false_for_132(self):
        self.assertFalse(self.lgis.is_sequence_decreasing([1,3,2]))

    #@unittest.skip('skip for now')
    def test_longest_increasing_subsequence_of_12_is_12(self):
        expected_result = (1, 2)
        self.assertEqual(self.lgis.get_longest_increasing_subsequence([1, 2]), expected_result)

    #@unittest.skip('skip for now')
    def test_longest_increasing_subsequence_of_132_is_13_or_12(self):
        longest_subsequence= self.lgis.get_longest_increasing_subsequence([1,3,2])
        self.assertTrue(longest_subsequence == (1,2) or longest_subsequence == (1,3))

    #@unittest.skip('skip for now')
    def test_longest_increasing_subsequence_of_sample_is_123(self):
        self.assertCountEqual(self.lgis.get_longest_increasing_subsequence(self.sample_permutation),(1,2,3))

    def test_longest_decreasing_subsequence_of_132_is_32(self):
        longest_subsequence = self.lgis.get_longest_decreasing_subsequence([1, 3, 2])
        self.assertEqual(longest_subsequence,(3,2))

    @unittest.skip('skip for now')
    def test_longest_decreasing_subsequence_of_sample_is_542(self):
        self.assertCountEqual(self.lgis.get_longest_decreasing_subsequence(self.sample_permutation), [5,4,2])