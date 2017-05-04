import unittest

from ..CSTR import CSTR

class TestCSTR(unittest.TestCase):
    def setUp(self):
        DNA_strings = '''ATGCTACC
CGTTTACC
ATTCGACC
AGTCTCCC
CGTCTATC'''
        self.cstr = CSTR(DNA_strings)

    def test_get_character_row_of_index(self):
        index = 0
        expected = '10110'
        self.assertEqual(self.cstr.get_character_row_of_index(index),expected)
        index = 2
        expected = ''
        self.assertEqual(self.cstr.get_character_row_of_index(index), expected)
        index = 7
        expected = ''
        self.assertEqual(self.cstr.get_character_row_of_index(index), expected)

    def test_get_character_table(self):
        expected = ['10110','10100']
        self.assertEqual(expected,self.cstr.character_table)