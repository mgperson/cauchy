import unittest

from src.Rosalind import Haystack


class HaystackTest(unittest.TestCase):
    def test_solution_of_sample_should_be_AC(self):
        DNAStrings = ['GATTACA','TAGACCA','ATACA']

        haystack = Haystack(DNAStrings)
        self.assertIsNotNone(haystack.DNAStrings)

        result = haystack.generate_substrings_of_length_n('ABCDEFGH',3)
        expected = ['ABC','BCD','CDE','DEF','EFG','FGH']

        self.assertCountEqual(result,expected)
        self.assertListEqual(result,expected)

        result = haystack.generate_all_substrings('ABCD')
        expected = ['ABCD','ABC','BCD','AB','BC','CD','A','B','C','D']

        self.assertCountEqual(result,expected)
        self.assertListEqual(result,expected)

        result = haystack.find_substring_in_string('germany','germ')
        self.assertTrue(result)

        self.assertEqual(haystack.solve_for_longest_common_substring(DNAStrings),'AC')
