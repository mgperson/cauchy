import unittest

from ..ITWV import ITWV

class TestITWV(unittest.TestCase):
    def setUp(self):
        values = '''GACCACGGTT
ACAG
GT
CCG'''.split('\n')
        self.itwv = ITWV(values)
        pass

    def test_get_matrix_of_interwoven_possibilities(self):
        matrix = self.itwv.matrix
        print(matrix)
        self.itwv.print_matrix()

    def test_get_all_interwoven_strings_of_t_and_u(self):
        interwoven_strings = ['ACTG','ATCG','ATGC','TACG','TAGC','TGAC']
        t = 'AC'
        u = 'TG'
        self.assertEqual(sorted(self.itwv.get_all_interwoven_strings_of_t_and_u('',t,u)),sorted(interwoven_strings))

    def test_can_t_and_u_be_interwoven_into_s(self):
        s = 'GACCACGGTT'
        t = 'ACAG'
        u = 'CCG'
        self.assertTrue(self.itwv.can_t_and_u_be_interwoven_into_s(s,t,u))
        s = 'GACCACAAAAGGTT'
        t = 'ACAG'
        u = 'CCG'
        self.assertFalse(self.itwv.can_t_and_u_be_interwoven_into_s(s, t, u))


