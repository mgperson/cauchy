import unittest

from ..LONG import LONG

class TestLONG(unittest.TestCase):
    def setUp(self):
        self.long = LONG('SRC\sample.txt')

    def test_get_maximum_overlap_length(self):
        a = 'ATTAGACCTG'
        b = 'CCTGCCGGAA'
        self.assertEqual(self.long.get_maximum_overlap_length(a,b),4)
        self.assertEqual(self.long.get_maximum_overlap_length(b, a), 1)

    def test_get_super_string_of_strings(self):
        a = 'ATTAGACCTG'
        b = 'CCTGCCGGAA'
        c = 'AGACCTGCCG'
        self.assertEqual(self.long.get_super_string_of_strings(a,b),'ATTAGACCTGCCGGAA')
        self.assertEqual(self.long.get_super_string_of_strings(b,a), 'ATTAGACCTGCCGGAA')
        self.assertEqual(self.long.get_super_string_of_strings('ATTAGACCTGCCGGAA',c), 'ATTAGACCTGCCGGAA')

    def test_get_super_string_of_string_list(self):
        a = 'ATTAGACCTG'
        b = 'CCTGCCGGAA'
        c = 'AGACCTGCCG'
        self.assertEqual(self.long.get_super_string_of_string_list([a,b,c]),'ATTAGACCTGCCGGAA')
        a = 'GGCT'
        b = 'TGCC'
        c = 'CTTG'
        self.assertEqual(self.long.get_super_string_of_string_list(([a,b,c])),'GGCTTGCC')

    def test_get_super_string_of_sample(self):
        self.assertEqual(self.long.get_super_string_of_string_list(self.long.strands),'ATTAGACCTGCCGGAATAC')
