import unittest

from ..Transcription import Transcription

class TestTrascription(unittest.TestCase):
    def setUp(self):
        self.transcript = Transcription()
        self.sample = 'GATGGAACTTGACTACGTAAATT'

    def test_replacement_of__t_with_u(self):
        self.assertEqual(self.transcript.replaceTWithU('ACGT'),'ACGU')

    def test_solution_of_sample(self):
        proper_result = 'GAUGGAACUUGACUACGUAAAUU'
        self.assertEqual(self.transcript.transcribe(self.sample),proper_result)