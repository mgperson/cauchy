import unittest

from ..CountMutations import  CountMutations

class TestCountMutations(unittest.TestCase):
    def setUp(self):
        self.cm = CountMutations()
        self.cm.read_input_file_and_initialize_distance_matrix('SRC\sample')
        self.sample_first_string = 'GAGCCTACTAACGGGAT'
        self.sample_second_string = 'CATCGTAATGACGGCCT'

    def test_get_distance_matrix(self):
        self.cm.get_distance_matrix()
        self.assertEqual(self.cm.distance_matrix,[[0, 0.4, 0.1, 0.1], [0.4, 0, 0.4, 0.3], [0.1, 0.4, 0, 0.2], [0.1, 0.3, 0.2, 0]])

    def test_get_p_distance(self):
        self.assertEqual(self.cm.get_p_distance(self.sample_first_string,self.sample_second_string),7/17)

    def test_string_different_characters_is_correct(self):
        self.assertEqual(3,self.cm.count_string_differences('PARENT','PORACT'))

    #@unittest.skip('Skip for now')
    def test_solution_of_sample_should_be_7(self):
        self.assertEqual(self.cm.count_mutations(self.sample_first_string,self.sample_second_string),7)

