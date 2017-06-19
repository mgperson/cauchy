#Matt Person
#Rosalind Problem: MMCH
#source
'''Given: An RNA string s of length at most 100.
Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s.'''

import math

class MMCH:
    def __init__(self,s):
        self.number_maximum_matchings = self.get_maximum_matchings_of_basepair_edges(s)

    def get_maximum_matchings_of_complementary_basepair_edges(self, count_one, count_two):
        max_count, min_count = max(count_one, count_two), min(count_one, count_two)
        return math.factorial(max_count) // math.factorial(max_count - min_count)

    def get_maximum_matchings_of_basepair_edges(self, RNA_string):
        G_count, C_count = RNA_string.count('G'), RNA_string.count('C')
        A_count, U_count = RNA_string.count('A'), RNA_string.count('U')
        return self.get_maximum_matchings_of_complementary_basepair_edges(G_count,
                                                                          C_count) * self.get_maximum_matchings_of_complementary_basepair_edges(A_count, U_count)
def Main():
    RNA_string = 'UUGUUAAAGAGAUGCACGCGGUAGCUCAACAAGGGGUCCCAACCAUUCCGGUCGAAUGAUAUCCGGCAAACGGACACAUACCGCUCGGCC'
    mmch = MMCH(RNA_string)
    print(mmch.number_maximum_matchings)

if __name__ == '__main__':
    Main()
