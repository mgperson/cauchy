import unittest

from ..CAT import CAT

class TestCAT(unittest.TestCase):
    def setUp(self):
        self.cat = CAT()

    def test_get_catalan_by_n(self):
        self.assertEqual(self.cat.get_catalan_by_n(3),5)
        self.assertEqual(self.cat.get_catalan_by_n(4), 14)

    def test_get_catalan_by_RNA_string(self):
        RNA_string = 'AUAU'
        self.assertEqual(self.cat.get_catalan_by_RNA_string(RNA_string),2)
        RNA_string = 'AUCGAU'
        self.assertEqual(self.cat.get_catalan_by_RNA_string(RNA_string), 2)
