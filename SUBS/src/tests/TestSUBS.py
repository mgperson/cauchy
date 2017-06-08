#Matt Person
#Rosalind Problem: SUBS
#unit tests

import unittest

from ..SUBS import SUBS

class TestSUBS(unittest.TestCase):
    def setUp(self):
        self.subs = SUBS('GATATATGCATATACTT','ATAT')

    def test_get_locations(self):
        self.assertEqual(self.subs.locations,[2,4,10])
