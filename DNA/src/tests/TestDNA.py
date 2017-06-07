#Matt Person
#Rosalind Problem: DNA
#Unit tests

import unittest
from collections import Counter

from ..DNA import DNA

class TestCountNucleotides(unittest.TestCase):
    def setUp(self):
        self.sample = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
        self.counter = DNA(self.sample)

    def test_counter_should_return_proper_counter(self):
        proper_counter = Counter({'T':21, 'A':20, 'G':17, 'C':12})
        self.assertEqual(self.counter.create_counter(self.sample),proper_counter)

    def test_solution_of_sample_should_be_20_12_17_21(self):
        self.assertEqual(self.counter.nucleotide_count,[20,12,17,21])






