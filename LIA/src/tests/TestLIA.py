import unittest

from ..LIA import LIA

class TestLia(unittest.TestCase):
    def setUp(self):
        self.lia = LIA()

    @unittest.skip('skip')
    def test_generate_expected_genotypes_for_genotype(self):
        self.assertDictEqual(self.lia.generate_expected_genotypes_for_genotype('AaBb'),\
            {'AABB':1,'AABb':2,'AAbb':1,'AaBB':2,'AaBb':4,'Aabb':2,'aaBB':1,'aaBb':2,'aabb':1})

    @unittest.skip('skip')
    def test_update_expected_genotypes_with_next_gen(self):
        self.assertEqual(self.lia.get_count_of_genotype('Aa',1), 1)
        self.lia.update_expected_genotypes_with_next_gen()
        self.assertEqual(self.lia.get_count_of_genotype('Aa',2), 0.4375)
        self.lia.update_expected_genotypes_with_next_gen()
        self.assertEqual(self.lia.get_count_of_genotype('Aa', 4), 0.25)

    def test_get_expected_value_of_nAaBb_at_generation_k(self):
        k, n = 1, 1
        self.assertEqual(self.lia.get_expected_value_of_nAaBb_at_generation_k(k, 1), 0.4375)
        k,n = 2,1
        self.assertEqual(self.lia.get_expected_value_of_nAaBb_at_generation_k(k,1),0.684)
