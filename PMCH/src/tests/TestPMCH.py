'''Also tests PPER'''
import unittest

from ..PMCH import PMCH

class TestPMCH(unittest.TestCase):
    def setUp(self):
        self.pmch = PMCH()

    def test_get_maximum_matchings_of_complementary_basepair_edges(self):
        count_one = 3
        count_two = 1
        self.assertEqual(self.pmch.get_maximum_matchings_of_complementary_basepair_edges(count_one,count_two),3)

    def test_get_perfect_matchings_of_basepair_edges(self):
        RNA_string = 'AGCUAGUCAU'
        self.assertEqual(self.pmch.get_perfect_matchings_of_basepair_edges(RNA_string),12)

    def test_get_partial_permutations(self):
        self.assertEqual(self.pmch.get_partial_permutations(21,7),51200)

    def test_get_maximum_matchings_of_basepair_edges(self):
        RNA_string = 'AUGCUUC'
        self.assertEqual(self.pmch.get_maximum_matchings_of_basepair_edges(RNA_string),6)