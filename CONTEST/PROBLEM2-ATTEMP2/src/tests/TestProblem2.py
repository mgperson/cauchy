import unittest

from ..Problem2 import Problem2

class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.solver = Problem2()

    def test_is_compliment_is_correct(self):
        self.assertTrue(self.solver.get_complement('G'), 'C')
        self.assertTrue(self.solver.get_complement('U'), 'A')

    def test_given_cases_are_perfect(self):
        self.assertEqual(self.solver.get_sequence_state('UGCA'),'perfect')

    def test_indeces_loading_is_proper(self):
        self.solver.load_indeces_lists('UACG')
        self.assertEqual(self.solver.indeces_by_base['C'], [2])

    def test_correct_extra_base_list(self):
        self.solver.load_indeces_lists('UACGG')
        self.assertEqual(self.solver.get_extra_base_list(),[3,4])

    #@unittest.skip('skip')
    def test_given_cases_are_almost_perfect(self):
        self.assertEqual(self.solver.get_sequence_state('AGUCU'), 'almost perfect')

    #@unittest.skip('skip')
    def test_given_cases_are_imperfect_even(self):
        self.assertEqual(self.solver.get_sequence_state('AGUC'), 'imperfect')
        self.assertEqual(self.solver.get_sequence_state('AAUC'), 'imperfect')

    #@unittest.skip('skip')
    def test_given_cases_are_imperfect_odd(self):
        self.assertEqual(self.solver.get_sequence_state('CAGUU'), 'imperfect')