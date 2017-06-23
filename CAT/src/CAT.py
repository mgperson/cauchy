#Matt Person
#Rosalind Problem: CAT
#source
'''Given: An RNA string s having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
The length of the string is at most 300 bp.
Return: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of s, modulo 1,000,000.'''



import sys

sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class CAT:
    def __init__(self,s):
        self.ru = RosalindUtilities()
        self.combinations_by_RNA_string = {}
        self.number_noncrossing_perfect_matches = self.get_catalan_by_RNA_string(s) % 1000000

    def find_occurences(self, s, ch):
        return [i for i, letter in enumerate(s) if letter == ch]

    def get_catalan_by_RNA_string(self,RNA_string):
        if RNA_string in self.combinations_by_RNA_string:
            return self.combinations_by_RNA_string[RNA_string]

        if len(RNA_string) == 0:
            return 1

        first_base = RNA_string[0]
        comp_base = self.ru.get_RNA_complement(first_base)
        comp_base_indeces = self.find_occurences(RNA_string, comp_base)
        len_comp_base_indeces = len(comp_base_indeces)

        if len_comp_base_indeces == 0:
            return len_comp_base_indeces

        catalan_num = 0
        for i in comp_base_indeces:
            catalan_num += self.get_catalan_by_RNA_string(RNA_string[1:i]) * self.get_catalan_by_RNA_string(RNA_string[i+1:])

        self.combinations_by_RNA_string[RNA_string] = catalan_num
        return catalan_num


def Main():
    RNA_string = 'GAAUAUAAUUUAUCGGCCGCAUGAUGCCUAGAAUUAUGCAGCGCUAGAUUACUAUGCGUAGCGCAUAUCGCAUCUUCAGCCGUGAUCGAUGCCUGCAGAAUUCGCGUUAACGCUAGGCGCAGGUACGCGCGGCUACCUUGCGCAUAAUAUGCACUAAUGUAUAUAUCCAUGGAUGCAGUACACUAGACGUCGCUGCCUAUAGCGCAUGUUUGCAAGCGCGCCGAAGUACGCAUGGCGUAGAUCCUA'
    solver = CAT(RNA_string)
    print(solver.number_noncrossing_perfect_matches)

if __name__ == '__main__':
    Main()


