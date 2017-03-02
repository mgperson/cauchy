import unittest

from ..FINALROUND5 import FINALROUND5

class TestFINALROUND5(unittest.TestCase):
    def setUp(self):
        self.solver = FINALROUND5('1','1.proteins')

    def test_did_reaction_happen(self):
        reaction_num = 0
        start_chems = ['c1','c2','c3','c5','c6']
        avail_chems = ['c1','c2','c3','c4','c5','c6']
        self.assertEqual(self.solver.did_reaction_happen(reaction_num,start_chems,avail_chems),'YES')
        reaction_num = 5
        start_chems = ['c1', 'c2', 'c3','c5','c6']
        avail_chems = ['c1', 'c2', 'c3','c4','c5','c6']
        self.assertEqual(self.solver.did_reaction_happen(reaction_num, start_chems, avail_chems), 'NO')
        reaction_num = 2
        self.assertEqual(self.solver.did_reaction_happen(reaction_num, start_chems, avail_chems), 'MAYBE')

    def test_get_reactions_that_happened(self):
        start_chemicals = 'c1 c2 c3'
        avail_chemicals = 'c1 c2 c3 c4 c5'
        self.assertEqual(self.solver.get_reactions_that_happened(start_chemicals,avail_chemicals),[0,1])

    def test_get_new_chemicals(self):
        self.assertEqual(self.solver.get_new_chemicals('c4','c4 c5'),{'c5'})