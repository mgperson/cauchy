import os, math
import sys
import itertools
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class FULL:
    def __init__(self,values):
        self.values = sorted(list(map(float,values)))
        self.ru = RosalindUtilities()
        pass

    def get_inner_peptide(self):
        prev_b_ion = self.values[0]
        inner_peptide = ''
        for i in range((len(self.values)-2)//2):
            while(True):
                for next_value in self.values:
                    if next_value > prev_b_ion:
                        aa = self.ru.get_aa_by_monoisotopic_mass(next_value - prev_b_ion)
                        if aa != '-1':
                            inner_peptide += aa
                            prev_b_ion = next_value
                            break
                break
        return inner_peptide

def Main():
    with open('Sample.txt') as input_file:
        values = [line for line in input_file][1:]
    full = FULL(values)
    print(full.get_inner_peptide())

if __name__ == '__main__':
    Main()
