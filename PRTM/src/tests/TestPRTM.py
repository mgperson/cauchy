#Matt Person
#Rosalind Problem: PRTM
#unit tests

import unittest

from ..PRTM import PRTM

class TestPRTM(unittest.TestCase):
    def setUp(self):
        P = 'SKADYEK'
        self.prtm = PRTM(P)

    def test_get_aa_monoisotropic_weight(self):
        self.assertEqual(self.prtm.get_aa_monoisotropic_weight('F'),147.06841)

    def test_get_protein_monoisotropic_weight(self):
        self.assertEqual(self.prtm.weight,821.392)

