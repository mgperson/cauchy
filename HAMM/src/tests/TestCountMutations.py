#Matt Person
#Rosalind Problem: HAMM
#unit tests

import unittest

from ..HAMM import HAMM

class TestCountMutations(unittest.TestCase):
    def setUp(self):
        sample_first_string = 'GAGCCTACTAACGGGAT'
        sample_second_string = 'CATCGTAATGACGGCCT'
        self.cm = HAMM(sample_first_string,sample_second_string)

    def test_get_p_distance(self):
        self.assertEqual(self.cm.hamming_distance,7)


