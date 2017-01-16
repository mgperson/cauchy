import unittest
from itertools import permutations

from ..EnumerateGeneOrders import EnumerateGeneOrders

class TestEnumerateGeneOrders(unittest.TestCase):
    def setUp(self):
        self.ego = EnumerateGeneOrders()
        self.sample = 3;

    def test_enumeration_of_permutations_of_3_is_proper(self):
        proper_enumeration = list(permutations([i for i in range(1,4)]))
        self.assertEqual(self.ego.enumerate_n(3),proper_enumeration)

    def test_length_of_enumeration_and_enumeration_of_permutations_of_3_is_proper(self):
        '''Testing proper enumeration of length display
        '''
        proper_enumeration = list(permutations([i for i in range(1,4)]))
        proper_result = [[6]] + proper_enumeration
        self.assertEqual(self.ego.get_length_of_enumeration_and_enumerate_n(3),proper_result)

    #@unittest.skip('Skip for now')
    def test_enumeration_of_gene_order_for_3_is_proper(self):
        proper_enumeration = list(permutations([i for i in range(1,4)]))
        proper_result = [[6]] + proper_enumeration
        self.assertEqual(self.ego.enumerate_gene_order(3),proper_result)