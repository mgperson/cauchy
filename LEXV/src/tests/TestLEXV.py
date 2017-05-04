import unittest

from .. LEXV import LEXV

class TestLEXV(unittest.TestCase):
    def setUp(self):
        self.lexv = LEXV()

    def test_get_strings_length_n_from_A(self):
        A = ''.join('D N A'.split())
        n = 3
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
        self.lexv.get_strings_length_n_from_A(output, A, '', n)
        self.assertEqual(output,expected)