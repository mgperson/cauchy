import unittest

from ..CONS import CONS

class TestCONS(unittest.TestCase):
    def setUp(self):
        self.cons = CONS()
        self.cons.load_profile_matrix('SRC\sample.txt')

    def test_load_profile_matrix(self):
        self.assertEqual(self.cons.profile_matrix,{'A': {0: 5, 4: 5, 5: 5, 1: 1}, 'C': {2: 1, 3: 4, 6: 6, 7: 1, 4: 2}, 'G': {5: 1, 0: 1, 1: 1, 2: 6, 3: 3}, 'T': {1: 5, 7: 6, 5: 1, 0: 1, 6: 1}})

    def test_group_count_by_letter_at_pos_i(self):
        self.assertEqual(self.cons.group_count_by_letter_at_pos_i(1),[('A',1),('C',0),('G',1),('T',5)])

    def test_get_consensus_string(self):
        self.assertEqual(self.cons.get_consensus_string(),'ATGCAACT')