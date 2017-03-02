import unittest

from ..PROT import PROT

class TestPROT(unittest.TestCase):
    def setUp(self):
        self.prot = PROT()
        pass

    def test_get_code_from_codon(self):
        self.assertEqual(self.prot.get_amino_acid_code_for_codon('CAC'),'H')

    def test_get_codons_from_RNA(self):
        RNA = 'AUGGCC'
        self.assertEqual(self.prot.get_codons_from_RNA(RNA),['AUG','GCC'])

    def test_get_codes_from_RNA(self):
        RNA = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
        expected = 'MAMAPRTEINSTRING'
        self.assertEqual(self.prot.get_codes_from_RNA(RNA),expected)