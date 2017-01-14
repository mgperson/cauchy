import unittest

from ..FindMotif import FindMotif

class TestFindMotif(unittest.TestCase):
    def setUp(self):
        self.fm = FindMotif()
        self.s = 'GATATATGCATATACTT'
        self.t = 'ATAT'

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