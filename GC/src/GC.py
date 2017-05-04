'''Solution for GC and KMER'''

import sys,itertools

sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class GC():
    def __init__(self):
        self.utils = RosalindUtilities()
        pass

    def get_kmers_freq_lexicographically(self,file):
        DNA_string = self.utils.read_input_file(file)[0][1]
        kmer_size = 4
        kmers = {}
        for kmer in sorted(list(set(itertools.permutations('AAAACCCCGGGGTTTT',4)))):
            kmers[''.join(kmer)] = 0
        #print(kmers)
        for i in range(len(DNA_string)-3):
            kmers[DNA_string[i:i+kmer_size]] = kmers.get(DNA_string[i:i+kmer_size],0) + 1
        return [kmers[kmer] for kmer in sorted(kmers.keys())]

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
    gc = GC()
    file = 'dataset.txt'
    #print(*gc.get_largest_GC_of_file(file),sep='\n')
    print(*gc.get_kmers_freq_lexicographically('solution.txt'))

if __name__ == '__main__':
    Main()