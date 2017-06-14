#Matt Person
#Rosalind Problem: PMCH
#source
'''Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.'''

import math

class PMCH:
    def __init__(self,s):
        self.perfect_matchings_count= self.get_perfect_matchings_of_basepair_edges(s)

    def get_perfect_matchings_of_basepair_edges(self,RNA_string):
        '''factorial of count of GC pairs * factorial of count of AU pairs'''
        GC_count = RNA_string.count('G')
        AU_count = RNA_string.count('A')
        return math.factorial(GC_count) * math.factorial(AU_count)

def Main():
    RNA_string = 'AGAGUGCAAGUGUCUAUUUCCCUGCCGGAAUGAGUAACCGGGCUGUAUCCAGACGAGCGCGUAACUCGUCCC'
    solver = PMCH(RNA_string)
    print(solver.perfect_matchings_count)

if __name__ == '__main__':
    Main()