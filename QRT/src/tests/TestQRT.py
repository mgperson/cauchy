import unittest

from ..QRT import QRT

class TestQRT(unittest.TestCase):
    def setUp(self):
        taxa_input = 'cat dog elephant ostrich mouse rabbit robot'
        table_input = '''01xxx00
x11xx00
111x00x'''
        self.qrt = QRT(taxa_input,table_input)

    def test_get_indices_of_characters_and_not_characters_in_split(self):
        split= '01xxx0'
        expected = ([1],[0,5])
        self.assertEqual(self.qrt.get_indices_of_characters_and_not_characters_in_split(split),expected)

    def test_generate_quartets_of_split(self):
        split = '111x00x'
        expected = [((0,1),(4,5)),((0,2),(4,5)),((1,2),(4,5))]
        self.assertEqual(self.qrt.generate_quartets_of_split(split), expected)

    def test_generate_unique_quartets(self):
        quartets = [((0,1), (2,3)),((0,1), (3,2)),((1,0), (2,3)),((1,0), (3,2)),((2,3), (0,1)),((2,3), (1,0)),((3,2), (0,1)),((3,2), (1,0))]
        for quartet in quartets:
            self.assertEqual(self.qrt.generate_numeric_quartet_hash(quartet),'0123')

    def test_get_quartets(self):
        quartets = '''{elephant, dog} {rabbit, robot}
{cat, dog} {mouse, rabbit}
{mouse, rabbit} {cat, elephant}
{dog, elephant} {mouse, rabbit}'''
        #self.qrt.generate_all_quartets()
        self.assertEqual(quartets,self.qrt.quartets)
