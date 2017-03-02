import unittest

from ..ORF import ORF

class TestORF(unittest.TestCase):
    def setUp(self):
        self.orf = ORF()

    def test_get_aa_from_DNACodon(self):
        self.assertEqual(self.orf.get_aa_from_DNACodon('ATG'),'M')
        self.assertEqual(self.orf.get_aa_from_DNACodon('UAA'), 'Stop')
        self.assertEqual(self.orf.get_aa_from_DNACodon('ACG'), 'T')

    def test_get_protein_from_DNAString(self):
        protein = self.orf.get_protein_from_DNAString('ATGTAG')
        self.assertEqual(protein,'M')
        protein = self.orf.get_protein_from_DNAString('ATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAG')
        self.assertEqual(protein, 'MGMTPRLGLESLLE')


    def test_get_possible_proteins_from_DNAString(self):
        proteins = self.orf.get_possible_proteins_from_DNAString('AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG')
        self.assertSetEqual(proteins,set(['MLLGSFRLIPKETLIQVAGSSPCNLS','M','MGMTPRLGLESLLE','MTPRLGLESLLE']))