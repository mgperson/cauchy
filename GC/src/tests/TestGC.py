import unittest

from ..GC import GC

class TestGC(unittest.TestCase):
    def setUp(self):
        self.gc = GC()

    def test_get_GC_of_DNA(self):
        self.assertEqual(self.gc.get_GC_of_DNA('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'),60.91954022988506)

    def test_get_largest_GC_of_file(self):
        file = 'src\sample.txt'
        self.assertEqual(self.gc.get_largest_GC_of_file(file),('Rosalind_0808',60.91954022988506))
