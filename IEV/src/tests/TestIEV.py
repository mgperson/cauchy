import unittest

from ..IEV import IEV

class TestIEV(unittest.TestCase):
    def setUp(self):
        self.iev = IEV()

    def test_get_expected_number(self):
        sample = list(map(int,'1 0 0 1 0 1'.split()))
        self.assertEqual(self.iev.get_expected_number(sample),3.5)