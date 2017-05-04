import unittest

from ..DBRU import DBRU

class TestDBRU(unittest.TestCase):
    def setUp(self):
        self.drbu = DBRU('src\sample.txt')
        self.drbu.get_union_of_kmers_and_rc()
        pass

    def test_get_union_of_kmers_and_rc(self):
        self.assertEqual(self.drbu.kmers_and_rc,{'TGAT','CATG','TCAT','ATGC','CATC','ATCA','ATGA','GCAT','GATG'})

    def test_get_de_brujin_graph(self):
        self.drbu.get_de_brujin_graph()
        self.assertEqual(sorted(self.drbu.de_brujin_graph),sorted([('ATC', 'TCA'),
('ATG', 'TGA'),
('ATG', 'TGC'),
('CAT', 'ATC'),
('CAT', 'ATG'),
('GAT', 'ATG'),
('GCA', 'CAT'),
('TCA', 'CAT'),
('TGA', 'GAT')]))