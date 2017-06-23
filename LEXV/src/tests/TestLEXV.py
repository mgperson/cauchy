#Matt Person
#Rosalind Problem: LEXV
#unit tests

import unittest

from .. LEXV import LEXV

class TestLEXV(unittest.TestCase):
    def setUp(self):
        A = ''.join('D N A'.split())
        n = 3
        self.lexv = LEXV(A,n)

    def test_get_strings_length_n_from_A(self):
        output = []
        expected = '''D
DD
DDD
DDN
DDA
DN
DND
DNN
DNA
DA
DAD
DAN
DAA
N
ND
NDD
NDN
NDA
NN
NND
NNN
NNA
NA
NAD
NAN
NAA
A
AD
ADD
ADN
ADA
AN
AND
ANN
ANA
AA
AAD
AAN
AAA'''.split()
        self.assertEqual(self.lexv.lexicographically_ordered_strings,expected)