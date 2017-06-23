import unittest

from ..RSTR import RSTR

class TestRSTR(unittest.TestCase):
    def setUp(self):
        gc = .6
        s = 'ATAGCCGA'
        n = 90000
        self.rstr = RSTR(n,gc,s)

    def test_calculate_prob_of_string_in_n_given_gc(self):
        gc = .6
        s = 'ATAGCCGA'
        n = 90000
        self.assertEqual(self.rstr.calculate_prob_of_string_in_n_given_gc(s, n, gc), 0.689)

    def test_calculate_GorC_and_AorT_prob(self):
        self.assertEqual(self.rstr.calculate_GorC_and_AorT_prob(.129), (.0645, .4355))

    def test_calculate_prob_of_string_with_log(self):
        gorc_aort_content = self.rstr.calculate_GorC_and_AorT_prob(.129)
        s = 'ACGATACAA'
        self.assertEqual(self.rstr.calculate_prob_of_string(gorc_aort_content[0], gorc_aort_content[1], s), -5.737)
