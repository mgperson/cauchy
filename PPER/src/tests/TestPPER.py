#Matt Person
#Rosalind Problem: PPER
#unit tests
import unittest

from ..PPER import PPER

class TestPMCH(unittest.TestCase):
    def setUp(self):
        self.PPER = PPER(21,7)

    def test_get_partial_permutations(self):
        self.assertEqual(self.PPER.partial_permutations,51200)