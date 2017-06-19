#Matt Person
#Rosalind Problem: MMCH
#unit tests

import unittest

from ..MMCH import MMCH

class TestMMCH(unittest.TestCase):
    def setUp(self):
        self.mmch = MMCH('AUGCUUC')

    def test_get_maximum_matchings(self):
        self.assertEqual(self.mmch.number_maximum_matchings,6)

