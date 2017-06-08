#Matt Person
#Rosalind Problem: GC
#unit tests

import unittest

from ..GC import GC

class TestGC(unittest.TestCase):
    def setUp(self):
        file = 'src\sample.txt'
        self.gc = GC(file)

    def test_get_GC_of_DNA(self):
        self.assertEqual(self.gc.get_GC_of_DNA('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'),60.91954022988506)

    def test_get_largest_GC_of_file(self):
        self.assertEqual(self.gc.largest_GC_of_file,('Rosalind_0808',60.91954022988506))