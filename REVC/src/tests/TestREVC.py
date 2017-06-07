#Matt Person
#Rosalind Problem: REVC
#Unit Test
import unittest

from ..REVC import REVC

class TestComplement(unittest.TestCase):
    def setUp(self):
        self.sample = 'AAAACCCGGT'
        self.complement = REVC(self.sample)

    def test_get_DNA_base_complement(self):
        base = 'T'
        self.assertEqual(self.complement.get_DNA_base_complement(base),'A')
        base = 'A'
        self.assertEqual(self.complement.get_DNA_base_complement(base), 'T')
        base = 'C'
        self.assertEqual(self.complement.get_DNA_base_complement(base), 'G')
        base = 'G'
        self.assertEqual(self.complement.get_DNA_base_complement(base), 'C')
        base = 'X'
        self.assertRaises(Exception,self.complement.get_DNA_base_complement,base)

    def test_complement_should_return_proper_complement(self):
        proper_complement= 'ACCGGGTTTT'
        self.assertEqual(self.complement.reverse_complement,proper_complement)

