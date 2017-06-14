#Matt Person
#Rosalind Problem: TREE
#unit tests
import unittest

from ..TREE import TREE

class TestTREE(unittest.TestCase):
    def setUp(self):
        self.tree = TREE('SRC\given.txt')

    def test_get_missing_nodes(self):
        self.assertEqual(self.tree.minimum_edges_to_add,3)

