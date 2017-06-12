#Matt Person
#Rosalind Problem: ORF
#source
'''Given: A DNA string s of length at most 1 kbp in FASTA format.
Return: Every distinct candidate protein string that can be translated from ORFs of ss. Strings can be returned in any order.'''

import sys

sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class ORF:
    def __init__(self,s):
        self.ru = RosalindUtilities()
        self.possible_proteins = self.get_possible_proteins_from_DNAString(s)

    def get_protein_from_DNAString(self,DNAString):
        protein = ''
        for i in range(0,len(DNAString)-2,3):
            codon = self.ru.get_aa_from_DNA_codon(DNAString[i:i+3])
            if codon == 'Stop':
                return protein
            protein += codon
        return None

    def get_possible_proteins_from_DNAString(self,DNAString):
        reverse_compliment = self.ru.get_reverse_complement(DNAString)
        return set(filter(None,[self.get_protein_from_DNAString(DNAString[i:]) for i in range(len(DNAString)-2) if DNAString[i:i+3] == 'ATG'] + \
            [self.get_protein_from_DNAString(reverse_compliment[i:]) for i in range(len(DNAString) - 2) if
                               reverse_compliment[i:i + 3] == 'ATG']))



def Main():
    DNAString = 'GTGGTTAATTCAGGCCATGAATCGTTCAAGAGATGTCTTTTATACGGTCGTCTCTTGCCAGACAAACCCCAATAACCGCGCGAGTTTGGTTCGACGGAGCGTTTTACTTCCACGGTGAGGACAGAGCAGGCAACGCGGTTCGCTGTGGGATAGCCGTTTCGTGACTCCTATATGGAAGCCAACCTACTAATTGATAATAGCTTTAGTGAGACCGTTTAGCCCGACACCGTTGAACATTGCTTCCAGCCTGTGGCAACTCGAGTCTGAAATCTGCGTCGCTCCCACCCAGAGAAGGTCAGGACTTATACCTTGTATTCGCAATCGCTGAAACAACTTTCCGGGAGAGCCGTGGGACCAGTTATGCCTATCCCCTAGCGCGAGAGTCGTGAGTGGTCACGTGTAAGCATAAAATTTGATACTGCCAGCTACCGTTCCATGATTGCTTATGTCATGGTGAATGATCGCGAACATTATGTAGCTACATAATGTTCGCGATCATTCACCATGACATACGCGGCGTTATTCTAACGGCACGGGGCGATACGTGAATGCACTTGAGCGAGCAAACTTACACTACTAACGTCCTTCTGCACACTATCTATAGAGCCCTCGAACCTACCTCCAGCTCGTACCAGGGGTGGCTTTAGTAGAGATAGTTCAAGTACCTCGGCGCAGATTCTTAGGGATGATTCAGACCCCTAGGGGTATATAGATTCTACAGGGCGCTCGGTCATTATTCTAATGTCGAGTACGTACTAACCCGTTGCTTTAAATCCTCAGGTTAAGCTCTGTGGACAGTCCGGCGCTGCTACTGGGGGTCCGAAACTTCTCCGCGGGTCCATAACCGGTCTCTAACTCGGAATAGACTCACTGGGAATATGTTCCTAACGCCAACGAGGCGCGAACTCGAGACGTTATCAGTCATTCGTACCGAGAATTAGACCATTGAGTGGGCA'
    orf = ORF(DNAString)
    print(*orf.possible_proteins,sep='\n')


if __name__ == '__main__':
    Main()
