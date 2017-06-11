#Matt Person
#Rosalind Problem: GPRH
#unit tests

import unittest


from ..GRPH import GRPH

class TestGRAPH(unittest.TestCase):
    def setUp(self):
        values = [('Rosalind_0498','AAATAAA'),('Rosalind_2391','AAATTTT'),('Rosalind_2323','TTTTCCC'),('Rosalind_0442','AAATCCC'),('Rosalind_5013','GGGTGGG')]
        self.graph = GRPH(values, 3)

    def test_get_prefix_of_length_k(self):
        k = 3
        expected = 'AAA'
        self.assertEqual(self.graph.get_prefix_of_length_k('AAATAAA',k),expected)

    def test_get_suffix_of_length_k(self):
        k=3
        expected = 'AAA'
        self.assertEqual(self.graph.get_suffix_of_length_k('AAATAAA',k),expected)

    def test_get_values_from_map(self):
        expected = sorted(['Rosalind_0498','Rosalind_2391','Rosalind_0442'])
        prefix ='AAA'
        self.assertEqual(sorted(self.graph.get_values_of_prefix(prefix)),expected)

    def test_map_is_set_up(self):
        expected = sorted(['Rosalind_0498','Rosalind_2391','Rosalind_0442'])
        prefix ='AAA'
        self.assertEqual(sorted(self.graph.get_values_of_prefix(prefix)),expected)

    def test_get_edges_for_tuple(self):
        expected = ['Rosalind_0498','Rosalind_2391','Rosalind_0442']
        input = ('Rosalind_0498','AAATAAA')
        self.assertEqual(self.graph.get_edges_for_tuple(input),expected)

    def test_get_all_edges_of_input(self):
        expected = [('Rosalind_0498','Rosalind_2391'),('Rosalind_0498','Rosalind_0442'),('Rosalind_2391','Rosalind_2323')]
        self.assertEqual(self.graph.get_all_edges_of_input(),expected)

