import unittest

from ..EDTA import EDTA

class TestEDTA(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_optimal_alignment(self):
        s = 'PRETTY'
        t = 'PRTTEIN'
        edta = EDTA(s,t)
        self.assertEqual(edta.optimal_alignment_length,4)
        #self.assertEqual(edta.s_prime,'PRETTY--')
        #self.assertEqual(edta.t_prime, 'PR-TTEIN')
