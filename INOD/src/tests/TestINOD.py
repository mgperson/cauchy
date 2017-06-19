#Matt Person
#Rosalind Problem: INOD
#unit tests
import unittest

from ..INOD import INOD

class TestINOD(unittest.TestCase):
    def setUp(self):
        self.inod = INOD(4)

    def test_get_number_internal_nodes(self):
        self.assertEqual(self.inod.number_internal_nodes,2)