import unittest
from collections import Counter

from ..CountNucleotides import CountNucleotides

class TestCountNucleotides(unittest.TestCase):
    def setUp(self):
        self.counter = CountNucleotides()
        self.sample = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

    def test_counter_should_return_proper_counter(self):
        proper_counter = Counter({'T':21, 'A':20, 'G':17, 'C':12})
        self.assertEqual(self.counter.create_counter(self.sample),proper_counter)

    def test_solution_of_sample_should_be_20_12_17_21(self):
        self.assertEqual(self.counter.count_nucleotides(self.sample),[20,12,17,21])






