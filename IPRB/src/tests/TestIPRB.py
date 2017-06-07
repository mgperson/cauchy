#Matt Person
#Rosalind Problem: IPRB
#unit tests

import unittest

from ..IPRB import IPRB

class TestIPRB(unittest.TestCase):
    def setUp(self):
        self.irpb = IPRB(2,2,2)

    def test_get_probability(self):
        self.assertEqual(self.irpb.total_prob,2.35/3)