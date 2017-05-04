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

    def test_get_protein_by_prefix_spectrum(self):
        prefix_spectrum = list(map(float,('''3524.8542
3710.9335
3841.974
3970.0326
4057.0646'''.split())))
        self.assertEqual(self.prtm.get_protein_by_prefix_spectrum(prefix_spectrum),'WMQS')