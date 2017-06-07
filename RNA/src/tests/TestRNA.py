#Matt Person
#Rosalind Problem: RNA
#unit tests

import unittest

from ..RNA import RNA

class TestRNA(unittest.TestCase):
    def setUp(self):
        self.sample = 'GATGGAACTTGACTACGTAAATT'
        self.transcript = RNA(self.sample)

    def test_replacement_of__t_with_u(self):
        self.assertEqual(self.transcript.replaceTWithU('ACGT'),'ACGU')

    def test_solution_of_sample(self):
        proper_result = 'GAUGGAACUUGACUACGUAAAUU'
        self.assertEqual(self.transcript.transcription,proper_result)