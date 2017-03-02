import unittest

from ..TREE import TREE

class TestTREE(unittest.TestCase):
    def setUp(self):
        self.tree = TREE()
        self.tree.read_data('SRC\sample.txt')

    def test_get_missing_nodes(self):
        self.assertEqual(self.tree.missing_nodes,set(['3']))

    def test_edges_belong_to_one_subtree(self):
        self.tree.generate_unique_sub_trees(self.tree.edges)
        print(self.tree.subtrees)
        self.assertTrue(self.tree.edges_belong_to_one_subtree(self.tree.edges,self.tree.subtrees))

    def test_subtrees_are_unique(self):
        self.tree.generate_sub_trees(self.tree.edges)
        self.assertTrue(self.tree.subtrees_are_unique(self.tree.subtrees))

    #@unittest.skip('skip')
    def test_get_subtree_count(self):
        self.tree.generate_unique_sub_trees(self.tree.edges)
        #self.tree.generate_sub_trees(self.tree.edges)
        #print(self.tree.subtrees)
        #self.tree.consolidate_all_trees(self.tree.subtrees)
        self.assertEqual(len(self.tree.subtrees)-1 + len(self.tree.missing_nodes),3)

    def test_consolidate_all_trees(self):
        tree_a = set(['1','2','5'])
        tree_b = set(['3','4','7','5'])
        tree_c = set(['1','4'])
        self.assertEqual(sorted(list(self.tree.consolidate_all_trees([tree_a,tree_b,tree_c]))),
                         sorted([{'1','2','3','4','5','7'}]))

    def test_consolidate_trees(self):
        tree_a = {'1','2','5'}
        tree_b = {'3','4','7','5'}
        tree_a = self.tree.consolidate_trees(tree_a,tree_b)
        self.assertEqual(tree_a,{'1','2','3','4','5','7'})

    def test_add_edge_to_sub_tree(self):
        edge_a = ('1','5')
        sub_tree = {'1','2','3'}
        self.tree.add_edge_to_sub_tree(edge_a,sub_tree)
        self.assertEqual(sub_tree,{'1','2','3','5'})

    def test_generate_sub_trees(self):
        edge_a = ('1', '5')
        edge_b = ('2', '5')
        self.tree.generate_sub_trees([edge_a, edge_b])
        self.assertEqual({'1','2','5'},self.tree.subtrees[0])

    def test_are_edges_connected(self):
        edge_a = ('1','5')
        edge_b = ('2','5')
        edge_c = ('3','4')
        self.assertTrue(self.tree.are_edges_connected(edge_a,edge_b))
        self.assertFalse(self.tree.are_edges_connected(edge_c, edge_b))

    def test_is_edge_in_sub_tree(self):
        edge_a = ('1','5')
        sub_tree_a = set(['1','2','3'])
        sub_tree_b = set(['4','6','7'])
        self.assertTrue(self.tree.is_edge_in_tree(edge_a,sub_tree_a))
        self.assertFalse(self.tree.is_edge_in_tree(edge_a, sub_tree_b))