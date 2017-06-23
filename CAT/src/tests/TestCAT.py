import unittest

from ..CAT import CAT

class TestCAT(unittest.TestCase):
    def setUp(self):
        RNA_string = 'AUAU'
        self.cat = CAT(RNA_string)

    def test_get_catalan_by_RNA_string(self):
        RNA_string = 'AUAU'
        self.assertEqual(self.cat.get_catalan_by_RNA_string(RNA_string),2)
        RNA_string = 'AUCGAU'
        self.assertEqual(self.cat.get_catalan_by_RNA_string(RNA_string), 2)


