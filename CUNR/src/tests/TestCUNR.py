import unittest

from ..CUNR import CUNR

class TestCUNR(unittest.TestCase):
    def setUp(self):
        self.cunr = CUNR()

    def test_get_num_distinct_unrooted_binary_trees(self):
        n = 5
        self.assertEqual(self.cunr.get_num_distinct_unrooted_binary_trees(n),15)
        n = 7
        self.assertEqual(self.cunr.get_num_distinct_unrooted_binary_trees(n), 945)