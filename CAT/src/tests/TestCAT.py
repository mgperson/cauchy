import unittest

from ..CAT import CAT

class TestCAT(unittest.TestCase):
    def setUp(self):
        self.cat = CAT()

    def test_get_wobble_matching_by_RNA_string(self):
        RNA_string = 'CGAUGCUAG'
        self.assertEqual(self.cat.get_wobble_matching_by_RNA_string(RNA_string),12)
        RNA_string = 'AUGCUAGUACGGAGCGAGUCUAGCGAGCGAUGUCGUGAGUACUAUAUAUGCGCAUAAGCCACGU'
        self.assertEqual(self.cat.get_wobble_matching_by_RNA_string(RNA_string),284850219977421)

    def test_get_motzkin_by_RNA_string(self):
        RNA_string = 'AU'
        self.assertEqual(self.cat.get_motzkin_by_RNA_string(RNA_string), 2)
        RNA_string = 'UAU'
        self.assertEqual(self.cat.get_motzkin_by_RNA_string(RNA_string), 3)
        RNA_string = 'AUAU'
        self.assertEqual(self.cat.get_motzkin_by_RNA_string(RNA_string),7)
        RNA_string = 'AGUC'
        self.assertEqual(self.cat.get_motzkin_by_RNA_string(RNA_string), 3)
        RNA_string = 'AUGC'
        self.assertEqual(self.cat.get_motzkin_by_RNA_string(RNA_string), 4)

    def test_get_catalan_by_n(self):
        self.assertEqual(self.cat.get_catalan_by_n(3),5)
        self.assertEqual(self.cat.get_catalan_by_n(4), 14)

    def test_get_catalan_by_RNA_string(self):
        RNA_string = 'AUAU'
        self.assertEqual(self.cat.get_catalan_by_RNA_string(RNA_string),2)
        RNA_string = 'AUCGAU'
        self.assertEqual(self.cat.get_catalan_by_RNA_string(RNA_string), 2)
