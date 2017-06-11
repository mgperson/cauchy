#Matt Person
#Rosalind Problem: MRNA
#unit tests

import unittest

from ..MRNA import MRNA

class TestMRNA(unittest.TestCase):
    def setUp(self):
        self.mrna = MRNA('MA')

    def test_get_count_of_codons_for_amino_acid(self):
        self.assertEqual(self.mrna.get_count_codons_for_amino_acids('M'),1)
        self.assertEqual(self.mrna.get_count_codons_for_amino_acids('A'), 4)
        self.assertEqual(self.mrna.get_count_codons_for_amino_acids('Stop'), 3)

    def test_get_number_possible_RNA(self):
        self.assertEqual(self.mrna.num_different_RNA_strings,12)