import unittest

from ..SGRA import SGRA

class TestSGRA(unittest.TestCase):
    def setUp(self):
        L =  '''3524.8542
3623.5245
3710.9335
3841.974
3929.00603
3970.0326
4026.05879
4057.0646
4083.08025'''
        self.sgra = SGRA(L)

    def test_get_spectrum_graph(self):
        spectrum_graph = {0: [(2, 'W')], 2: [(3, 'M')], 3: [(4, 'S'), (5, 'Q')], 4: [(6, 'P'), (7, 'Q')], 5: [(7, 'S')], 6: [(8, 'G')]}
        self.assertEqual(spectrum_graph,self.sgra.spectrum_graph)

    def test_generate_longest_protein_string(self):
        longest_protein_string= 'WMSPG'
        self.assertEqual(self.sgra.longest_protein_string,longest_protein_string)