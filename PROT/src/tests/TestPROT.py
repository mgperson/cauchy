#Matt Person
#Rosalind Problem: PROT
#unit tests

import unittest

from ..PROT import PROT

class TestPROT(unittest.TestCase):
    def setUp(self):
        RNA = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
        self.prot = PROT(RNA)
        pass

    def test_get_codons_from_RNA(self):
        RNA = 'AUGGCC'
        self.assertEqual(self.prot.get_codons_from_RNA(RNA),['AUG','GCC'])

    def test_get_codes_from_RNA(self):
        expected = 'MAMAPRTEINSTRING'
        self.assertEqual(self.prot.protein_string, expected)