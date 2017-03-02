import unittest

from ..PROBLEM3 import Problem3

class TestPROBLEM3(unittest.TestCase):
    def setUp(self):
        with open('src/1') as input_data:
            self.solver = Problem3(input_data.readline().strip())

    def test_is_subsequence(self):
        self.assertTrue(self.solver.is_subsequence('abcdef', 'ace'))
        self.assertFalse(self.solver.is_subsequence('racecar', 'acra'))

    def test_get_superstring_of_permutation(self):
        print('get superstring')
        permutation = (2,0,1)
        strings = ['aab','b','ba']
        self.assertEqual(self.solver.get_superstring_of_permutation(permutation,strings),'baab')

    def test_generate_superstring_of_two_strings(self):
        a = 'aaa'
        b = 'bbb'
        self.assertEqual(self.solver.generate_superstring_of_two_strings(a,b),'aaabbb')
        a = 'aab'
        b = 'bbb'
        self.assertEqual(self.solver.generate_superstring_of_two_strings(a, b), 'aabbb')
        a = 'bab'
        b = 'bbb'
        self.assertEqual(self.solver.generate_superstring_of_two_strings(a, b), 'babbb')
        a = 'ba'
        b = 'aab'
        self.assertEqual(self.solver.generate_superstring_of_two_strings(a, b), 'baab')
        a = 'baab'
        b = 'b'
        self.assertEqual(self.solver.generate_superstring_of_two_strings(a, b), 'baab')

    def test_find_shortest_super_string(self):
        print('find shortest super string')
        strings = ['aaa','bbb']
        self.assertEqual(len(self.solver.find_shortest_super_string(strings)),len('aaabbb'))