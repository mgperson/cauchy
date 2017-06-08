#Matt Person
#Rosalind Problem: IEV
#UNITTESTS
import unittest

from ..IEV import IEV

class TestIEV(unittest.TestCase):
    def setUp(self):
        sample = list(map(int, '1 0 0 1 0 1'.split()))
        self.iev = IEV(sample)

    def test_get_expected_number(self):
        self.assertEqual(self.iev.expected_number,3.5)