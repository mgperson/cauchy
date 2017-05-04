import os, math
import sys
import itertools
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class SGRA():
    def __init__(self,L):
        self.L = list(map(float,L.split('\n')))
        self.RU = RosalindUtilities()
        self.spectrum_graph = {}
        self.generate_spectrum_graph()
        self.generate_longest_protein_string(0,'')
        pass

    def generate_spectrum_graph(self):
        for i in range(len(self.L)):
            for j in range(i+1,len(self.L)):
                aa = self.RU.get_aa_by_monoisotopic_mass(self.L[j]-self.L[i])
                if aa != '-1':
                    self.spectrum_graph[i] = self.spectrum_graph.get(i,[]) + [(j,aa)]
                    #self.spectrum_graph.append((i,j,aa))

    def generate_longest_protein_string(self,start_index,prefix):
        edges = self.spectrum_graph.get(start_index,None)
        longest_protein_string = prefix
        if edges == None:
            return prefix
        for edge in edges:
            result = self.generate_longest_protein_string(edge[0],prefix+edge[1])
            if len(result) > len(longest_protein_string):
                longest_protein_string = result
        self.longest_protein_string = longest_protein_string
        return longest_protein_string

def Main():
    with open('input.txt') as input_data:
        lines = ''.join([line for line in input_data])
    sgra = SGRA(lines)
    print (sgra.longest_protein_string)

if __name__ == '__main__':
    Main()
