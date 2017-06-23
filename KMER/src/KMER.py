#Matt Person
#Rosalind Problem: KMER
#source
'''Given: A DNA string s in FASTA format (having length at most 100 kbp).
Return: The 4-mer composition of s.'''

import sys,itertools

sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class KMER():
    def __init__(self,input_file):
        self.utils = RosalindUtilities()
        self.kmers = self.get_kmers_freq_lexicographically(input_file)

    def get_kmers_freq_lexicographically(self,file):
        DNA_string = self.utils.read_input_file(file)[0][1]
        kmer_size = 4
        kmers = {}
        for kmer in sorted(list(set(itertools.permutations('AAAACCCCGGGGTTTT',4)))):
            kmers[''.join(kmer)] = 0
        for i in range(len(DNA_string)-3):
            kmers[DNA_string[i:i+kmer_size]] = kmers.get(DNA_string[i:i+kmer_size],0) + 1
        return [kmers[kmer] for kmer in sorted(kmers.keys())]


def Main():
    kmer = KMER('solution.txt')
    print(*kmer.kmers)

if __name__ == '__main__':
    Main()