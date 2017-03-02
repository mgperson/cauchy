import unittest

from ..SSEQ import SSEQ

class TestSSEQ(unittest.TestCase):
    def setUp(self):
        self.sseq = SSEQ()
        pass

    def test_get_subsequence_indexing(self):
        s = 'ACGTACGTGACG'
        t = 'GTA'
        expected = [3, 4, 5]
        self.assertEqual(self.sseq.get_subsequence_indexing(s,t),expected)