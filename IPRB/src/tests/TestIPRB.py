import unittest

from ..IPRB import IPRB

class TestIPRB(unittest.TestCase):
    def setUp(self):
        self.irpb = IPRB()

    def test_get_probability(self):
        self.assertEqual(self.irpb.get_probability(2,2,2),2.35/3)