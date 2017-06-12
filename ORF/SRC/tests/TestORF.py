#Matt Person
#Rosalind Problem: ORF
#unit tests

import unittest

from ..ORF import ORF

class TestORF(unittest.TestCase):
    def setUp(self):
        s = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
        self.orf = ORF(s)

    def test_get_protein_from_DNAString(self):
        protein = self.orf.get_protein_from_DNAString('ATGTAG')
        self.assertEqual(protein,'M')
        protein = self.orf.get_protein_from_DNAString('ATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAG')
        self.assertEqual(protein, 'MGMTPRLGLESLLE')


    def test_get_possible_proteins_from_DNAString(self):
        proteins = self.orf.possible_proteins
        self.assertSetEqual(proteins,set(['MLLGSFRLIPKETLIQVAGSSPCNLS','M','MGMTPRLGLESLLE','MTPRLGLESLLE']))