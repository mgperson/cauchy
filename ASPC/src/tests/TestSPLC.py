import unittest

from ..SPLC import SPLC

class TestSPLC(unittest.TestCase):
    def setUp(self):
        self.splc = SPLC()

    def test_get_combinations(self):
        n,m = 6,3
        self.assertEqual(self.splc.get_combinations(n,m),42)

    def test_remove_intron_from_DNA(self):
        DNA = 'AUCGUGUCAUCAUGACUGUCACUG'
        expected = 'AUCGUGUGACUGUCACUG'
        first_removal = self.splc.remove_intron_from_DNA(DNA,'UCAUCA')
        self.assertEqual(first_removal,expected)
        expected = 'AUCGUGUGACUGU'
        second_removal = self.splc.remove_intron_from_DNA(first_removal,'CACUG')
        self.assertEqual(second_removal,expected)

    def test_read_input_file(self):
        lines = self.splc.read_input_file('src\sample.txt')
        self.assertEqual(lines[1][1],'ATCGGTCGAA')

    #@unittest.skip('for now')
    def test_remove_all_introns_from_DNA(self):
        expected = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCATCTCGAGAGGCATATGGTCACATGTTCAAAGTTTGCGCCTAG'
        self.assertEqual(self.splc.remove_all_introns_from_DNA('src\sample.txt'),expected)

    #@unittest.skip('for now')
    def test_get_amino_codes_after_removing_introns_from_DNA(self):
        expected = 'MVYIADKQHVASREAYGHMFKVCA'
        self.assertEqual(self.splc.get_amino_codes_after_removing_introns_from_DNA('src\sample.txt'),expected)

    def test_remove_first_intron_from_DNA(self):
        expected = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG'
        lines = self.splc.read_input_file('src\sample.txt')
        s = lines[0][1]
        s = self.splc.remove_intron_from_DNA(s,lines[1][1])
        self.assertEqual(s,expected)
        expected = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCATCTCGAGAGGCATATGGTCACATGTTCAAAGTTTGCGCCTAG'
        print(lines)
        print ('intron:' + lines[2][1])
        self.assertEqual(self.splc.remove_intron_from_DNA(s,lines[2][1]),expected)
