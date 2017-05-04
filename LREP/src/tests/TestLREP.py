import unittest

from ..LREP import LREP

class TestLREP(unittest.TestCase):
    def setUp(self):
        DNA_string = 'CATACATAC$'
        k = 2
        nodes = '''node1 node2 1 1
        node1 node7 2 1
        node1 node14 3 3
        node1 node17 10 1
        node2 node3 2 4
        node2 node6 10 1
        node3 node4 6 5
        node3 node5 10 1
        node7 node8 3 3
        node7 node11 5 1
        node8 node9 6 5
        node8 node10 10 1
        node11 node12 6 5
        node11 node13 10 1
        node14 node15 6 5
        node14 node16 10 1'''.split('\n')
        self.lrep = LREP(DNA_string, k, nodes)

    def test_get_longest_value_repeated_k_or_more_times(self):
        k = 2
        self.lrep.longest_repeated_substring_k_or_more_times['CATAC'] = 2
        self.lrep.longest_repeated_substring_k_or_more_times['ATAC'] = 3
        self.lrep.longest_repeated_substring_k_or_more_times['CATATAC'] = 1
        self.assertEqual(self.lrep.get_longest_value_repeated_k_or_more_times(),'CATAC')


    def test_get_longest_substring_repeated_k_or_more_times(self):
        self.assertEqual(self.lrep.get_longest_substring_repeated_k_or_more_times(),'CATAC')
