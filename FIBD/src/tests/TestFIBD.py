#Matt Person
#Rosalind Problem: FIBD
#unit tests

import unittest

from ..FIBD import FIBD

class TestFIBD(unittest.TestCase):
    def setUp(self):
        n, m = 6, 3
        self.fibd = FIBD(n,m)

    def test_get_fibd_of_n_m(self):
        self.assertEqual(self.fibd.number_of_pairs,4)