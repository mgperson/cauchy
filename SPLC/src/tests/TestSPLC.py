#Matt Person
#Rosalind Problem: TestSPLC
#source

import unittest

from ..SPLC import SPLC

class TestSPLC(unittest.TestCase):
    def setUp(self):
        self.splc = SPLC('src\sample.txt')

    def test_remove_intron_from_DNA(self):
        DNA = 'AUCGUGUCAUCAUGACUGUCACUG'
        expected = 'AUCGUGUGACUGUCACUG'
        first_removal = self.splc.remove_intron_from_DNA(DNA,'UCAUCA')
        self.assertEqual(first_removal,expected)
        expected = 'AUCGUGUGACUGU'
        second_removal = self.splc.remove_intron_from_DNA(first_removal,'CACUG')
        self.assertEqual(second_removal,expected)

    def test_remove_all_introns_from_DNA(self):
        expected = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCATCTCGAGAGGCATATGGTCACATGTTCAAAGTTTGCGCCTAG'
        self.assertEqual(self.splc.remove_all_introns_from_DNA('src\sample.txt'),expected)

    def test_get_amino_codes_after_removing_introns_from_DNA(self):
        expected = 'MVYIADKQHVASREAYGHMFKVCA'
        self.assertEqual(self.splc.get_amino_codes_after_removing_introns_from_DNA('src\sample.txt'),expected)

    def test_remove_first_intron_from_DNA(self):
        expected = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG'
        self.splc = SPLC('src\sample.txt')
        lines = self.splc.lines
        s = lines[0][1]
        s = self.splc.remove_intron_from_DNA(s,lines[1][1])
        self.assertEqual(s,expected)
        expected = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCATCTCGAGAGGCATATGGTCACATGTTCAAAGTTTGCGCCTAG'
        print(lines)
        print ('intron:' + lines[2][1])
        self.assertEqual(self.splc.remove_intron_from_DNA(s,lines[2][1]),expected)
