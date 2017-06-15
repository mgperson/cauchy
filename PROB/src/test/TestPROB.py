#Matt Person
#Rosalind Problem: PROB
#unit tests

import unittest

from ..PROB import PROB

class TestPROB(unittest.TestCase):
    def setUp(self):
        probs = '0.129 0.287 0.423 0.476 0.641 0.742 0.783'
        s = 'ACGATACAA'
        self.prob = PROB(s,probs)

    def test_calculate_GorC_and_AorT_prob(self):
        self.assertEqual(self.prob.calculate_GorC_and_AorT_prob(.129),(.0645,.4355))

    def test_calculate_prob_of_string_with_log(self):
        gorc_aort_content = self.prob.calculate_GorC_and_AorT_prob(.129)
        s = 'ACGATACAA'
        self.assertEqual(self.prob.calculate_prob_of_string(gorc_aort_content[0],gorc_aort_content[1],s),-5.737)

    def test_calculate_all_probs_of_string_with_log(self):
        self.assertEqual(self.prob.B,[-5.737, -5.217, -5.263, -5.360, -5.958, -6.628, -7.009])