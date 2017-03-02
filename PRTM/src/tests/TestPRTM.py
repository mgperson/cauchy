import unittest

from ..PRTM import PRTM

class TestPRTM(unittest.TestCase):
    def setUp(self):
        self.prtm = PRTM()

    def test_get_aa_monoisotropic_weight(self):
        self.assertEqual(self.prtm.get_aa_monoisotropic_weight('F'),147.06841)

    def test_get_protein_monoisotropic_weight(self):
        P = 'SKADYEK'
        self.assertEqual(self.prtm.get_protein_monoisotropic_weight(P),821.392)