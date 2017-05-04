import unittest

from ..NWCK import NWCK

class TestNWCK(unittest.TestCase):
    def setUp(self):
        NWCK_tree = '(C,D,(A,B));'
        self.nwck = NWCK(NWCK_tree)
        NWCK_tree_2 = '(cat)dog;'
        self.nwck_2 = NWCK(NWCK_tree_2)
        NWCK_tree_3 = '((A,B),C,D);'
        self.nwck_3 = NWCK(NWCK_tree_3)

    def test_get_difference_between_nodes(self):
        node_a = 'C'
        node_b = 'A'
        self.assertEqual(self.nwck.get_distance_between_nodes(node_a, node_b), 3)
        node_a = 'dog'
        node_b = 'cat'
        self.assertEqual(self.nwck_2.get_distance_between_nodes(node_a,node_b),1)
        node_a = 'C'
        node_b = 'A'
        self.assertEqual(self.nwck_3.get_distance_between_nodes(node_a, node_b), 3)