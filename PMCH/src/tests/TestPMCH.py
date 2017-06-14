#Matt Person
#Rosalind Problem: PMCH
#unit tests
import unittest

from ..PMCH import PMCH

class TestPMCH(unittest.TestCase):
    def setUp(self):
        RNA_string = 'AGCUAGUCAU'
        self.pmch = PMCH(RNA_string)

    def test_get_perfect_matchings_of_basepair_edges(self):
        self.assertEqual(self.pmch.perfect_matchings_count,12)
