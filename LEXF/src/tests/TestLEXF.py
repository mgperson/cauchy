#Matt Person
#Rosalind Problem: LEXF
#unit tests

import unittest

from ..LEXF import LEXF

class TestTRAN(unittest.TestCase):
    def setUp(self):
        a = 'T A G C'.split()
        n = 2
        self.tran = LEXF(a,n)
        pass

    def test_get_lexicographical_order_of_alphabet(self):
        self.assertEqual(self.tran.lexicographical_order_of_alphabet,['AA',
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
