#Matt Person
#Rosalind Problem: FIB
#Unit test

import unittest

from ..FIB import FIB

class TestFIB(unittest.TestCase):
    def setUp(self):
        self.fib = FIB(5,3)

    def test_get_fib_n_with_k(self):
        self.assertEqual(self.fib.num_rabbit_pairs,19)