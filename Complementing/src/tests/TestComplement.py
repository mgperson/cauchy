import unittest

from ..Complement import Complement

class TestComplement(unittest.TestCase):
    def setUp(self):
        self.complement = Complement()
        self.sample = 'AAAACCCGGT'

    def test_reverse_of_sample_is_proper(self):
        proper_reverse = 'TGGCCCAAAA'
        self.assertEqual(self.complement.get_reverse(self.sample),proper_reverse)

    def test_swap_two_chars_in_string(self):
        proper_swap = 'TTTTCCCGGA'
        self.assertEqual(self.complement.swap_two_chars_in_string(self.sample,'T','A'),proper_swap)

    def test_complement_of_sample_is_proper(self):
        proper_complement = 'TTTTGGGCCA'
        self.assertEqual(self.complement.get_complement(self.sample),proper_complement)

    #looks like this is python equivalent of pending? skip decorator
    #@unittest.skip('skipping for now')
    def test_complement_should_return_proper_complement(self):
        proper_complement= 'ACCGGGTTTT'
        self.assertEqual(self.complement.get_reverse_complement(self.sample),proper_complement)

