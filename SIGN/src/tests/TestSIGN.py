import unittest

from ..SIGN import SIGN

class testSIGN(unittest.TestCase):
    def setUp(self):
        self.sign = SIGN(2)

    def test_get_positive_and_negative_permutations(self):
        expected_len = 8
        expected_permutations = [[-1, -2],[-1, 2],[1,-2],[1,2],[-2,-1],[-2,1],[2,-1],[2,1]]
        self.assertEqual(len(self.sign.positive_and_negative_permutations),expected_len)
        self.assertEqual([permutation for permutation in self.sign.positive_and_negative_permutations], expected_permutations)