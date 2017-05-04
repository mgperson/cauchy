import unittest

from .. PCOV import PCOV

class TestPCOV(unittest.TestCase):
    def setUp(self):
        kmers = '''ATTAC
TACAG
GATTA
ACAGA
CAGAT
TTACA
AGATT'''
        self.pcov = PCOV(kmers)

    def test_generate_superstring(self):
        expected = 'GATTACA'
        result = self.pcov.superstring
        self.assertTrue(result in (expected + expected))
        self.assertTrue(len(result) == len(expected))
