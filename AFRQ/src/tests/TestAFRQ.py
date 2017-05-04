import unittest
IASWMQS
from ..AFRQ import AFRQ

class TestAFRQ(unittest.TestCase):
    def setUp(self):
        self.afrq = AFRQ()

    def test_get_at_least_one_recessive_freq(self):
        self.assertEqual(self.afrq.get_at_least_one_recessive_freq(.25),0.75)

    def test_get_at_least_one_recessive_freq_of_values(self):
        values = map(float,'0.1 0.25 0.5'.split())
        self.assertEqual(self.afrq.get_at_least_one_recessive_freq_of_values(values),[0.532, 0.75, 0.914])