import unittest

from ..PROBLEM2 import PROBLEM2

class TestPROBLEM2(unittest.TestCase):
    def setUp(self):
        sequence = 'UACG'
        self.problem2 = PROBLEM2()
        #self.problem2.initialize_sequence(sequence)

    def test_is_compliment_is_correct(self):
        self.problem2.initialize_sequence('UACG')
        self.assertTrue(self.problem2.is_complement('G','C'))
        self.assertTrue(self.problem2.is_complement('U', 'A'))
        self.assertFalse(self.problem2.is_complement('G', 'A'))
        self.assertEqual(self.problem2.get_complement('G'),'C')

    def test_all_is_mapped_are_init_to_true(self):
        self.problem2.initialize_sequence('UACG')
        self.assertTrue(not all(self.problem2.is_index_mapped))

    def test_indeces_loading_is_proper(self):
        self.problem2.initialize_sequence('UACG')
        self.assertEqual(self.problem2.indeces_by_base['C'],[2])

    def test_all_pairs_mapped(self):
        self.problem2.initialize_sequence('UACG')
        self.problem2.map_all_pairs_and_get_state()
        self.assertEqual(len(self.problem2.indeces_by_base['C']),0)

    def test_is_pair_perfect(self):
        self.problem2.initialize_sequence('UACG')
        self.assertTrue(self.problem2.is_pair_perfect(1,2,3,4))
        self.assertTrue(self.problem2.is_pair_perfect(1, 4, 2, 3))
        self.assertFalse(self.problem2.is_pair_perfect(1,3,2,4))
        self.assertFalse((self.problem2.is_pair_perfect(0,2,1,3)))

    def test_is_mapping_perfect(self):
        self.problem2.initialize_sequence('UAGC')
        self.assertEqual(self.problem2.map_all_pairs_and_get_state(),'perfect')
        self.problem2.initialize_sequence('UGCA')
        self.assertEqual(self.problem2.map_all_pairs_and_get_state(),'perfect')

    def test_is_mapping_not_perfect(self):
        self.problem2.initialize_sequence('AGUC')
        self.assertEqual(self.problem2.map_all_pairs_and_get_state(),'imperfect')
        self.problem2.initialize_sequence('AAUC')
        self.assertEqual(self.problem2.map_all_pairs_and_get_state(),'imperfect')
        self.problem2.initialize_sequence('CAGUU')
        self.assertEqual(self.problem2.map_all_pairs_and_get_state(), 'imperfect')

    def test_is_mapping_almost_perfect(self):
        self.problem2.initialize_sequence('ACGCU')
        self.assertEqual(self.problem2.map_all_pairs_and_get_state(), 'almost perfect')
        self.problem2.initialize_sequence('ACCGC')
        self.assertEqual(self.problem2.map_all_pairs_and_get_state(), 'imperfect')
        self.problem2.initialize_sequence('AGUCU')
        self.assertEqual(self.problem2.map_pairs_and_get_state('perfect'), 'almost perfect')


