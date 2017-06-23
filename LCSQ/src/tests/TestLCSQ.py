#Matt Person
#Rosalind Problem: LCSQ
#unit tests

import unittest

from ..LCSQ import LCSQ

class TestLCSQ(unittest.TestCase):
    def setUp(self):
        self.s3 = 'ATCTGAT'
        self.t3 = 'TGCATA'
        self.lcsq = LCSQ(self.s3,self.t3)
        self.u3 = self.lcsq.shortest_supersequence
        pass

    def test_is_subsequence(self):
        self.assertTrue(self.lcsq._LCSQ__is_subsequence('abcdef','ace'))
        self.assertFalse(self.lcsq._LCSQ__is_subsequence('racecar','acra'))

    def test_is_shortest_supersequence_correct(self):
        self.assertEqual(self.u3,'ATCTGCATA')



