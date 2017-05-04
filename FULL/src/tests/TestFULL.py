import unittest

from ..FULL import FULL

class TestFULL(unittest.TestCase):
    def setUp(self):
        values = '''1988.21104821
610.391039105
738.485999105
766.492149105
863.544909105
867.528589105
992.587499105
995.623549105
1120.6824591
1124.6661391
1221.7188991
1249.7250491
1377.8200091'''.split('\n')
        self.full = FULL(values[1:])
        pass

    def test_get_inner_peptide(self):
        self.assertEqual(self.full.get_inner_peptide(),'KEKEP')