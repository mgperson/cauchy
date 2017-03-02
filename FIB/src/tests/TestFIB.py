import unittest

from ..FIB import FIB

class TestFIB(unittest.TestCase):
    def setUp(self):
        self.fib = FIB()

    def test_get_fib_n_with_k(self):
        self.assertEqual(self.fib.get_fib_n_with_k(5,3),19)