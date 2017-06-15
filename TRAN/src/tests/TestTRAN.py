#Matt Person
#Rosalind Problem: TRAN
#unit tests

import unittest

from ..TRAN import TRAN

class TestTRAN(unittest.TestCase):
    def setUp(self):
        a = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
        b = 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'
        self.tran = TRAN(a,b)

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
        self.assertEqual(self.tran.transition_transversion_ratio,1.21428571429)