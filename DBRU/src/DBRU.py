import os
import sys,difflib
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class DBRU:
    def __init__(self,file):
        self.ru = RosalindUtilities()
        self.kmers = set()
        self.kmers_and_rc = set()
        self.de_brujin_graph = []
        self.load_kmers_from_file(file)
        pass

    def load_kmers_from_file(self,file):
        with open(file) as input_data:
            for line in input_data:
                self.kmers.add(line.strip('\n'))

    def get_union_of_kmers_and_rc(self):
        self.kmers_and_rc = self.kmers.copy()
        [self.kmers_and_rc.add(self.ru.get_reverse_complement(kmer)) for kmer in self.kmers]

    def get_de_brujin_graph(self):
        k = len(list(self.kmers_and_rc)[0])-1
        [self.de_brujin_graph.append((kmer[:k],kmer[1:])) for kmer in self.kmers_and_rc]

def Main():
    drbu = DBRU('Dataset_1')
    drbu.get_union_of_kmers_and_rc()
    drbu.get_de_brujin_graph()
    print(*drbu.de_brujin_graph,sep='\n')
    with open('output.txt','w') as output_data:
        for edge in drbu.de_brujin_graph:
            output_data.write('(' + edge[0] + ',' + edge[1] + ')\n')

if __name__ == '__main__':
    Main()