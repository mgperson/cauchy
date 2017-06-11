import unittest

from ..LIA import LIA

class TestLia(unittest.TestCase):
    def setUp(self):
        k, n = 1, 1
        self.lia = LIA(k,n)

    def test_get_expected_value_of_nAaBb_at_generation_k(self):
        self.assertEqual(self.lia.expected_value_of_nAaBb_at_generation_k, 0.438)
        self.lia = LIA(2,1)
        self.assertEqual(self.lia.expected_value_of_nAaBb_at_generation_k,0.684)
