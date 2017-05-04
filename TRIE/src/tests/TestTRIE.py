import unittest

from ..TRIE import TRIE

class TestTRIE(unittest.TestCase):
    def setUp(self):
        pass


    def test_load_trie(self):
        trie = '''ATAGA
ATC
GAT'''.split()
        test = TRIE(trie)
        self.assertEqual(test.get_adjacency_list_in_triplets(),
                         [(1, 2, 'A'),(1,8,'G'),(2, 3, 'T'), (3, 4, 'A'), (3, 7, 'C'), (4, 5, 'G'), (5, 6, 'A'),(8,9,'A'),(9,10,'T')])

    def test_load_one_line_trie(self):
        trie = TRIE(['ATAGA'])
        self.assertEqual(trie.get_adjacency_list_in_triplets(),[(1, 2, 'A'),(2,3,'T'),(3,4,'A'),(4, 5, 'G'),(5, 6, 'A')])

    def test_load_two_line_trie(self):
        trie = TRIE(['ATAGA','ATC'])
        self.assertEqual(trie.get_adjacency_list_in_triplets(),
                         [(1, 2, 'A'), (2, 3, 'T'), (3, 4, 'A'), (3,7,'C'),(4, 5, 'G'), (5, 6, 'A')])