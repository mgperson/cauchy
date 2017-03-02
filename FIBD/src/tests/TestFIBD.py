import unittest

from ..FIBD import FIBD

class TestFIBD(unittest.TestCase):
    def setUp(self):
        self.fibd = FIBD()

    def test_get_fibd_of_n_m(self):
        n,m = 6,3
        self.assertEqual(self.fibd.get_fibd_of_n_m(n,m),4)