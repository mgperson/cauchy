'''Solution for SPLC and ASPC'''
import os, math
import sys
import itertools
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

print (os.getcwd())

class SPLC:
    def __init__(self):
        self.amino_acid_codes_for_codons = {}
        self.load_amino_acid_codes_for_codons()
        pass

    def remove_intron_from_DNA(self,DNA,intron):
        return DNA.replace(intron,'')

    def get_combinations(self,n,m):
        result = 0
        for i in range(m,n+1):
            result += math.factorial(n) // (math.factorial(n-i) * math.factorial(i))
        return  result % 1000000

    def load_amino_acid_codes_for_codons(self):
        values = [('UUU', 'F'), ('UUC', 'F'), ('UUA', 'L'), ('UUG', 'L'),
                  ('UCU', 'S'), ('UCC', 'S'), ('UCA', 'S'), ('UCG', 'S'),
                  ('UAU', 'Y'), ('UAC', 'Y'), ('UAA', 'Stop'), ('UAG', 'Stop'),
                  ('UGU', 'C'), ('UGC', 'C'), ('UGA', 'Stop'), ('UGG', 'W'),

                  ('CUU', 'L'), ('CUC', 'L'), ('CUA', 'L'), ('CUG', 'L'),
                  ('CCU', 'P'), ('CCC', 'P'), ('CCA', 'P'), ('CCG', 'P'),
                  ('CAU', 'H'), ('CAC', 'H'), ('CAA', 'Q'), ('CAG', 'Q'),
                  ('CGU', 'R'), ('CGC', 'R'), ('CGA', 'R'), ('CGG', 'R'),

                  ('AUU', 'I'), ('AUC', 'I'), ('AUA', 'I'), ('AUG', 'M'),
                  ('ACU', 'T'), ('ACC', 'T'), ('ACA', 'T'), ('ACG', 'T'),
                  ('AAU', 'N'), ('AAC', 'N'), ('AAA', 'K'), ('AAG', 'K'),
                  ('AGU', 'S'), ('AGC', 'S'), ('AGA', 'R'), ('AGG', 'R'),

                  ('GUU', 'V'), ('GUC', 'V'), ('GUA', 'V'), ('GUG', 'V'),
                  ('GCU', 'A'), ('GCC', 'A'), ('GCA', 'A'), ('GCG', 'A'),
                  ('GAU', 'D'), ('GAC', 'D'), ('GAA', 'E'), ('GAG', 'E'),
                  ('GGU', 'G'), ('GGC', 'G'), ('GGA', 'G'), ('GGG', 'G')]

        for val in values:
            self.amino_acid_codes_for_codons[val[0]] = val[1]

    def get_amino_acid_code_for_codon(self,codon):
        return self.amino_acid_codes_for_codons.get(codon)

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
        lines = self.read_input_file(input)
        s = lines[0][1]
        for i in range(1,len(lines)):
            s = self.remove_intron_from_DNA(s,lines[i][1])
        return s

    def get_amino_codes_after_removing_introns_from_DNA(self,input):
        s = self.remove_all_introns_from_DNA(input)
        s = self.replaceTWithU(s)
        return self.get_codes_from_RNA(s)

    def replaceTWithU(self, inputString):
        return inputString.replace('T', 'U')

    def read_input_file(self,file):
        values = []
        with open(file) as input_data:
            current_line = ''
            label = ''
            for line in input_data:
                if line[0] == '>':
                    if not current_line == '':
                        values.append((label,current_line))
                    label = line[1:]
                    current_line = ''
                else:
                    current_line += line.rstrip('\n')
            values.append((label,current_line))
        return values


def Main():
    ru = RosalindUtilities()
    print(sys.path)
    splc = SPLC()
    splc.read_input_file('sample.txt')
    print (splc.get_amino_codes_after_removing_introns_from_DNA('test.txt'))
    n,m = 1679,622
    print(splc.get_combinations(n,m))

if __name__ == '__main__':
    Main()