#Matt Person
#Rosalind Problem: KMP
#unit tests

import unittest

from ..KMP import KMP

class TestFindMotif(unittest.TestCase):
    def setUp(self):
        self.s = 'GATATATGCATATACTT'
        self.fm = KMP(self.s)
        self.t = 'ATAT'

    def test_get_failure_array_of_DNA_string(self):
        DNA_string = 'CAGCATGGTATCACAGCAGAG'
        failure_array = list(map(int,'0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0'.split()))
        self.assertEqual(self.fm.get_failure_array_of_DNA_string(DNA_string),failure_array)
        DNA_string = 'CAGTAAGCAGGGACTG'
        failure_array = list(map(int, '0 0 0 0 0 0 0 1 2 3 0 0 0 1 0 0'.split()))


    def test_found_t_in_s(self):
        proper_result = [2,4]
        self.assertEqual(self.fm.find_t_in_s('ABABA','B'),proper_result)

    def test_found_t_in_s_with_overlap(self):
        proper_result = [2,4]
        self.assertEqual(self.fm.find_t_in_s('CGAGAGACT','GAGA'),proper_result)

    #@unittest.skip('skip for now')
    def test_found_motif_in_string(self):
        proper_result = [2,4,10]
        self.assertEqual(self.fm.find_motif_in_string(self.s,self.t),proper_result)