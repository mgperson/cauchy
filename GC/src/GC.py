#Matt Person
#Rosalind Problem: GC
#source
'''Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.'''

import sys,itertools

sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class GC():
    def __init__(self,file):
        self.utils = RosalindUtilities()
        self.largest_GC_of_file = self.get_largest_GC_of_file(file)
        pass

    def get_GC_of_DNA(self,DNA):
        return (DNA.count('G') + DNA.count('C'))/len(DNA) * 100

    def get_largest_GC_of_file(self,file):
        strings = self.utils.read_input_file(file)
        max_GC = 0
        max_GC_label = ''
        for string in strings:
            GC_of_string = self.get_GC_of_DNA(string[1])
            if GC_of_string > max_GC:
                max_GC = GC_of_string
                max_GC_label = string[0]
        return (max_GC_label,max_GC)

def Main():
    file = 'dataset.txt'
    gc = GC(file)
    print(*gc.largest_GC_of_file,sep='\n')

if __name__ == '__main__':
    Main()