#Matt Person
#Rosalind Problem: SPLC
#source
'''Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)'''

import sys
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class SPLC:
    def __init__(self,input_file):
        self.ru = RosalindUtilities()
        self.protein_string = self.get_amino_codes_after_removing_introns_from_DNA(input_file)
        pass

    def remove_intron_from_DNA(self,DNA,intron):
        return DNA.replace(intron,'')

    def get_amino_acid_code_for_codon(self,codon):
        return self.ru.amino_acid_codes_for_codons.get(codon)

    def get_codons_from_RNA(self,RNA):
        n = len(RNA) // 3 * 3
        return [RNA[i:i+3] for i in range(0,n,3)]

    def get_codes_from_RNA(self,RNA):
        result = ''
        for codon in self.get_codons_from_RNA(RNA):
            code = self.get_amino_acid_code_for_codon(codon)
            if code == 'Stop':
                return result
            result += code
        return result

    def remove_all_introns_from_DNA(self,input):
        self.lines = self.ru.read_input_file(input)
        s = self.lines[0][1]
        for i in range(1,len(self.lines)):
            s = self.remove_intron_from_DNA(s,self.lines[i][1])
        return s

    def get_amino_codes_after_removing_introns_from_DNA(self,input):
        s = self.remove_all_introns_from_DNA(input)
        s = self.replaceTWithU(s)
        return self.get_codes_from_RNA(s)

    def replaceTWithU(self, inputString):
        return inputString.replace('T', 'U')


def Main():
    splc = SPLC('test.txt')
    print (splc.protein_string)

if __name__ == '__main__':
    Main()