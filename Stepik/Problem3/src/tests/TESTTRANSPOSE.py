import unittest

from ..TRANSPOSE import TRANSPOSE

class TESTTRANSPOSE(unittest.TestCase):
    def setUp(self):
        n, l, d = 3, 30, 1
        genome = '''CTTCTCCCAGACTAGACCATCCTCTTGCTTGCCCCTACTCCCACTCGCGATGTCAGCGTGGAGCGCCGAACGTTTCACAGCTCCATAGGCTAGACCATCCTCTTGCTTGCCCCTACGCCACTGTAGAACGGCTAGACCATCCTCTTGCTTGCCCCTACTAC'''
        #n, l, d = 4, 10, 1
        #genome = 'CGCATGCCAGCATTCAACCGAAAATGCAGCATTAAGTGTCTAAAAATGCAGCATTTGTGTTACTTAGTATCAGCATTGCAA'
        #n, l, d = 1, 0, 0
        #genome = 'C'
        self.transpose = TRANSPOSE(n,l,d,genome,False)

    def test_get_cigar_string(self):
        n, l, d = 3, 30, 1
        genome = '''CTTCTCCCAGACTAGACCATCCTCTTGCTTGCCCCTACTCCCACTCGCGATGTCAGCGTGGAGCGCCGAACGTTTCACAGCTCCATAGGCTAGACCATCCTCTTGCTTGCCCCTACGCCACTGTAGAACGGCTAGACCATCCTCTTGCTTGCCCCTACTAC'''
        transpose = TRANSPOSE(n, l, d, genome,False)
        actual = transpose.get_CIGAR_string_at_location('CTAGACCATCCTCTTGCTTGCCCCTACTCC',89)
        self.assertEqual(actual,'27M1X2M')
        actual = transpose.get_CIGAR_string('ATGCAGCATT','ATCAGCATT')
        self.assertEqual(actual, '2M1I7M')
        actual = transpose.get_CIGAR_string('ATGCAGCATT', 'ATGCCAGCATT')
        self.assertTrue(actual == '4M1D6M' or actual == '3M1D7M')

    def test_is_strand_a_match(self):
        strand,other_strand,d = 'Racecar','Ragecar',1
        self.assertTrue(self.transpose.is_strand_a_match(strand,other_strand,d))
        strand, other_strand, d = 'Racecar', 'Raecar', 1
        self.assertTrue(self.transpose.is_strand_a_match(strand, other_strand, d))
        strand, other_strand = 'CTAGACCATCCTCTTGCTTGCCCCTACTCC', 'CTAGACCATCCTCTTGCTTGCCCCTACGCC'
        self.assertTrue(self.transpose.is_strand_a_match(strand, other_strand, d))
        strand, other_strand = 'CTAGACCATCCTCTTGCTTGCCCCTACTAC', 'CTAGACCATCCTCTTGCTTGCCCCTACGCC'
        self.assertFalse(self.transpose.is_strand_a_match(strand, other_strand, d))
        strand,other_strand = 'ATGCAGCATT','CATGCCAGCA'
        self.assertFalse(self.transpose.is_strand_a_match(strand, other_strand, d))
        strand, other_strand = 'ATGCAGCATT', 'ATCAGCATT'
        self.assertTrue(self.transpose.is_strand_a_match(strand, other_strand, d))
        strand, other_strand = 'GACCAAGCATTTCCTGTGGGGG', 'GACCAAGCATTTCCTGTGGGGG'
        self.assertTrue(self.transpose.is_strand_a_match(strand, other_strand, 5))
        strand, other_strand = 'GACCAAGCATTTCCTGTGGGGG', 'GCTGAATTCAAGCATTTCCTGTG'
        self.assertTrue(self.transpose.is_strand_a_match(strand, other_strand, 5))

    def test_get_solution(self):
        n, l, d = 3, 30, 1
        genome = '''CTTCTCCCAGACTAGACCATCCTCTTGCTTGCCCCTACTCCCACTCGCGATGTCAGCGTGGAGCGCCGAACGTTTCACAGCTCCATAGGCTAGACCATCCTCTTGCTTGCCCCTACGCCACTGTAGAACGGCTAGACCATCCTCTTGCTTGCCCCTACTAC'''
        transpose = TRANSPOSE(n,l,d,genome,False)
        expected = '''CTAGACCATCCTCTTGCTTGCCCCTACTCC
12 30M
90 27M1X2M
132 28M1X1M'''
        print(str(transpose))
        #self.assertEqual(str(transpose),expected)

        n, l, d = 4, 10, 1
        genome = 'CGCATGCCAGCATTCAACCGAAAATGCAGCATTAAGTGTCTAAAAATGCAGCATTTGTGTTACTTAGTATCAGCATTGCAA'

        expected = '''ATGCAGCATT
4 4M1D6M
24 10M
46 10M
69 2M1I7M'''
        print(str(transpose))
        transpose = TRANSPOSE(n, l, d, genome, True)
        #self.assertEqual(str(transpose),expected)
