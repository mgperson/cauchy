import unittest
from ..ERRORS import ERRORS

class TestErrors(unittest.TestCase):
    def setUp(self):
        self.errors = ERRORS(4,2,0,1,{})

    @unittest.SkipTest
    def test_get_expected_misreads(self):
        errors = ERRORS(15, 6, 0.005, 10,{})
        self.assertEqual(errors.answer,0.08040206039130814)

    def test_get_brute_force_probability(self):
        self.assertEqual(self.errors.get_brute_force_probability(1,2),7/9)
        self.assertEqual(self.errors.get_brute_force_probability(1, 0), 0)
        self.assertEqual(self.errors.get_brute_force_probability(1, 4), 1)
        self.assertEqual(self.errors.get_brute_force_probability(2, 3), 4/9)

    def test_get_probability_incorrect_decision(self):
        self.assertEqual(round(self.errors.get_probability_incorrect_decision(1, 2),4), round(7 / 9,4))
        self.assertEqual(self.errors.get_probability_incorrect_decision(1, 0), 0)
        self.assertEqual(self.errors.get_probability_incorrect_decision(1, 4), 1)
        self.assertEqual(round(self.errors.get_probability_incorrect_decision(2, 3),4), round(4 / 9,4))

    def test_get_probability_distribution_of_incorrect_reads(self):
        expected = [2/3,1/3]
        self.assertEqual(self.errors.get_probability_distribution_of_incorrect_reads(1,3),expected)
        expected = [4/9,4/9,1/9]
        self.assertEqual(self.errors.get_probability_distribution_of_incorrect_reads(2,3), expected)
        expected = [1/2,1/2]
        self.assertEqual(self.errors.get_probability_distribution_of_incorrect_reads(1, 2), expected)
        expected = [1/8,3/8,3/8,1/8]
        self.assertEqual(self.errors.get_probability_distribution_of_incorrect_reads(3, 2), expected)

    def test_get_distributions(self):
        expected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(self.errors.get_distributions(1),expected)

    def test_get_error_probability_with_distribution(self):
        self.assertEqual(self.errors.get_error_probability_with_distribution(1,1,1,1),0.75)
        self.assertEqual(self.errors.get_error_probability_with_distribution(2, 1, 1, 1), 0)
        self.assertEqual(self.errors.get_error_probability_with_distribution(2, 2, 2, 1), 2/3)

    def test_generate_distributions(self):
        self.assertEqual(self.errors.generate_distributions(1),['C','G','T'])
        self.assertEqual(self.errors.generate_distributions(2),  ['CC', 'GC', 'TC', 'CG', 'GG', 'TG', 'CT', 'GT', 'TT'])
