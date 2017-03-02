import unittest

from..REVP import REVP

class TESTREVP(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.revp = REVP('TCAATGCATGCGGGTCTATATGCAT')
        pass

    def test_get_all_subsequences_of_length_n(self):
        n = 4
        test_string = 'GATTACA'
        expected =['GATT','ATTA','TTAC','TACA']
        self.assertEqual(self.revp.get_all_subsequences_of_length_n(test_string,n),expected)

    def test_get_all_intervals_of_length_m_of_string_of_length_n(self):
        n = 4
        test_string_length = 7
        expected = [(0,n),(1,n),(2,n),(3,n)]

    def test_get_reverse_of_sequence(self):
        test_string = 'GATTACA'
        expected = 'ACATTAG'
        self.assertEqual(self.revp.get_reverse_of_sequence(test_string),expected)

    def test_complement_of_C_is_G(self):
        expected = 'G'
        self.assertEqual(self.revp.get_complement_of_letter('C'),expected)

    def test_complement_of_G_is_C(self):
        expected = 'C'
        self.assertEqual(self.revp.get_complement_of_letter('G'), expected)

    def test_complement_of_A_is_T(self):
        expected = 'T'
        self.assertEqual(self.revp.get_complement_of_letter('A'), expected)

    def test_complement_of_T_is_A(self):
        expected = 'A'
        self.assertEqual(self.revp.get_complement_of_letter('T'), expected)

    def test_complement_of_ACGT_is_TGCA(self):
        expected = 'TGCA'
        self.assertEqual(self.revp.get_complement_of_string('ACGT'),expected)

    def test_is_reverse_palindrome(self):
        self.assertFalse(self.revp.is_reverse_palindrome('ACGTC'))
        self.assertTrue(self.revp.is_reverse_palindrome('AATTAATT'))

    def test_get_reverse_palindromes_of_length_n(self):
        n = 4
        test_string = 'GGCCAATT'
        expected = [(0,n),(4,n)]
        self.assertEqual(self.revp.get_reverse_palindromes_of_length_n(test_string,n),expected)

    def test_get_reverse_palindromes_of_length_4_to_12(self):
        test_string = 'TCAATGCATGCGGGTCTATATGCAT'
        expected = sorted([(3,6),(4,4),(5,6),(6,4),(16,4),(17,4),(19,6),(20,4)])
        self.assertListEqual(sorted(self.revp.get_reverse_palindromes_of_length_4_to_12(test_string)),expected)

