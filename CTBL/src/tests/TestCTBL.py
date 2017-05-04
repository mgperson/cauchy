import unittest

from ..CTBL import CTBL

class TestCTBL(unittest.TestCase):
    def setUp(self):
        self.input_nwck = '(dog,((elephant,mouse),robot),cat);'
        self.input_nwck_2 = '(((C,D),(E,F)),A,B);'

    def test_get_taxa_lexicographically_sorted(self):
        self.ctbl = CTBL(self.input_nwck)
        expected = ['cat','dog','elephant','mouse','robot']
        self.assertEqual(self.ctbl.get_taxa_lexicographically_sorted(),expected)

    def test_get_character_table(self):
        self.ctbl = CTBL(self.input_nwck)
        expected = ['00111','00110']
        self.ctbl.get_character_table()
        self.assertEqual(sorted(self.ctbl.result),sorted(expected))
        self.ctbl = CTBL(self.input_nwck_2)
        expected = ['001100','000011','001111']
        self.ctbl.get_character_table()
        self.assertEqual(sorted(self.ctbl.result),sorted(expected))