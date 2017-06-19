#Matt Person
#Rosalind Problem: SSET
#unit tests
import unittest

from ..SSET import SSET

class TestSSET(unittest.TestCase):
    def setUp(self):
        self.sset = SSET(3)

    def test_get_number_of_subsets(self):
        self.assertEqual(self.sset.number_of_subsets,8)

