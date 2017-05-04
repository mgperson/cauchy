import unittest

from ..RNAS import RNAS

class TestRNAS(unittest.TestCase):
    def setUp(self):
        self.cat = RNAS()

    def test_get_wobble_matching_by_RNA_string(self):
        RNA_string = 'CGAUGCUAG'
        self.assertEqual(self.cat.get_wobble_matching_by_RNA_string(RNA_string),12)
        RNA_string = 'AUGCUAGUACGGAGCGAGUCUAGCGAGCGAUGUCGUGAGUACUAUAUAUGCGCAUAAGCCACGU'
        self.assertEqual(self.cat.get_wobble_matching_by_RNA_string(RNA_string),284850219977421)
