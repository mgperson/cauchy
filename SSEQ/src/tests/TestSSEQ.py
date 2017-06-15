#Matt Person
#Rosalind Problem: SSEQ
#unit tests

import unittest

from ..SSEQ import SSEQ

class TestSSEQ(unittest.TestCase):
    def setUp(self):
        s = 'ACGTACGTGACG'
        t = 'GTA'
        self.sseq = SSEQ(s,t)

    def test_get_subsequence_indexing(self):
        expected = [3, 4, 5]
        self.assertEqual(self.sseq.subsequence_indexing,expected)