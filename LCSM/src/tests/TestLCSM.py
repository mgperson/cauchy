#Matt Person
#Rosalind Problem: TestLCSM
#unit tests
import unittest

from ..LCSM import LCSM

class TestLCSM(unittest.TestCase):
    def test_solution_of_sample_should_be_AC(self):
        DNAStrings = ['GATTACA','TAGACCA','ATACA']

        lcsm = LCSM('src/test_input.txt')
        self.assertIsNotNone(lcsm.DNAStrings)

        result = lcsm.generate_substrings_of_length_n('ABCDEFGH',3)
        expected = ['ABC','BCD','CDE','DEF','EFG','FGH']

        self.assertCountEqual(result,expected)
        self.assertListEqual(result,expected)

        result = lcsm.generate_all_substrings('ABCD')
        expected = ['ABCD','ABC','BCD','AB','BC','CD','A','B','C','D']

        self.assertCountEqual(result,expected)
        self.assertListEqual(result,expected)

        result = lcsm.find_substring_in_string('germany','germ')
        self.assertTrue(result)

        self.assertEqual(lcsm.longest_common_substring,'TA')
