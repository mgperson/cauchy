#Matt Person
#Rosalind Problem: PDST
#unit tests

import unittest

from ..PDST import  PDST

class TestPDST(unittest.TestCase):
    def setUp(self):
        self.cm = PDST('SRC\given.txt')
        self.sample_first_string = 'GAGCCTACTAACGGGAT'
        self.sample_second_string = 'CATCGTAATGACGGCCT'

    def test_get_distance_matrix(self):
        self.cm.get_distance_matrix()
        self.assertEqual(self.cm.distance_matrix,[[0, 0.4, 0.1, 0.1], [0.4, 0, 0.4, 0.3], [0.1, 0.4, 0, 0.2], [0.1, 0.3, 0.2, 0]])

    def test_get_p_distance(self):
        self.assertEqual(self.cm.get_p_distance(self.sample_first_string,self.sample_second_string),7/17)

    def test_string_different_characters_is_correct(self):
        self.assertEqual(3,self.cm.count_string_differences('PARENT','PORACT'))


