import unittest

from ..TRAN import TRAN

class TestTRAN(unittest.TestCase):
    def setUp(self):
        self.tran = TRAN()
        pass

    def test_get_signed_permutations(self):
        n = 2
        self.assertEqual( self.tran.get_signed_permutations_of_n(n),['-1 -2',
'-1 2',
'1 -2',
'1 2',
'2 -1',
'-2 1',
'2 -1',
'2 1'])

    def test_get_lexicographical_order_of_alphabet(self):
        a = 'T A G C'.split()
        n = 2
        self.assertEqual(self.tran.get_lexicographical_order_of_alphabet(a,n),['AA',
'AC',
'AG',
'AT',
'CA',
'CC',
'CG',
'CT',
'GA',
'GC',
'GG',
'GT',
'TA',
'TC',
'TG',
'TT'])

    def test_get_mutation_type(self):
        a = 'G'
        b = 'T'
        self.assertEqual(self.tran.get_mutation_type(a,b),'transversion')
        a = 'C'
        b = 'T'
        self.assertEqual(self.tran.get_mutation_type(a, b), 'transition')
        a = 'G'
        b = 'G'
        self.assertEqual(self.tran.get_mutation_type(a, b), 'none')

    def test_get_transition_transversion_ratio(self):
        a = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
        b = 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'
        self.assertEqual(self.tran.get_transition_transversion_ratio(a,b),1.21428571429)