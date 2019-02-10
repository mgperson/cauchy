import unittest

from ..BEES import BEES

class TESTEES(unittest.TestCase):
    def setUp(self):
        pass

    def test_find_limit(self):
        #bees = BEES(0.500,1.000,1.000)
        #self.assertEqual(str(bees),str(0))
        #bees = BEES(0.500, 3.000, 1.000)
        #self.assertNotEqual(str(bees), str(-1))
        #bees = BEES(0.500, 3.000, 1.000)
        #self.assertEqual(str(bees), str(2))
        #number 12
        #bees = BEES(2.759, 2.018, 0.694)
        #self.assertNotEqual(str(bees), str(-1))
        #NUmber 15
        #bees = BEES(1.728, 2.909, 1.622)
        #self.assertNotEqual(str(bees), str(-1))
        #Number 24
        #bees = BEES(0.813, 2.636, 2.769)
        #self.assertNotEqual(str(bees), str(-1))
        #Number 27
        bees = BEES(0.287, 1.000, 1.664)
        self.assertNotEqual(str(bees), str(0.0024))