#Matt Person
#Rosalind Problem: REVC
#source
'''Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.'''

class REVC:
    def __init__(self,s):
        self.s = s
        self.reverse_complement = self.get_reverse_complement()
        pass

    def get_DNA_base_complement(self,base):
        if base not in 'ATCG':
            raise Exception("Not a DNA base")
        if base == 'A':
            return 'T'
        if base == 'T':
            return 'A'
        if base == 'C':
            return 'G'
        if base == 'G':
            return 'C'


    def get_reverse_complement(self):
        return ''.join([self.get_DNA_base_complement(c) for c in self.s][::-1])

def main():
    inputString = 'TTAGTGCCGTCACAGGTACTGTGACCAAGTGTAGTACACGACTGTCCGTCGACCACCCCCCTGGTAAGCCCACAAAAGGTGTCGAGAGAACAACCCTTCTTCTCGAACATCACGATAATGGTATAGTTATTCTCGCGCATTTCATACGACACTGATCACGACCGAATTGAAATGCAAGGATGACAGGAGTGGAAAGAAAGGCACAGCGTACCAAGGTTTTATATTCAGGCGCATAATGCCAAGACACATTCCGCATGTGGCAACAGGTTCACAAGCCCGGCTTCACGTGATCGCGTATACTCAAGACGGGACCATACCATTATATTATGTAGGATGGTACGGCAGGGTGCATCGGAGCTCGACTTACTATACTGTCTTAGGACATGTCGAGAATATACAGCTCGGTATGGGCTTAAATAAATTCCTCATATTACTCTTGGTTCACGTACTGATTAGTCTGGTCATCCTGCTGGGTTGGATGAGCCAAATAGTTTTACTCGGAGATGCAGCCACCTGAAATCATACGTTGCTGTTGCTTACCGCTATACGGGGACAGTTGGCCCCGGCATACATGACCGGAGTTGGCACTACTAGAAATAGGACAACATGCGTGCGGACTATAGCGGTGGAAACTCATTTGGCTTACCACTTGACCTACGCCACCGGTGAGTATTTGTCTTCTCATACTTTTTCAAGAGCCGTTTTAAGTTTGCAGGCGAGGGACGGAGCCGACCTGAATCTTTATTGATCCAGAACTAGCCCCCCGAATCGCTACTCGATTAGTTGCTAGCCTGACGAGCTCAACCATACGAAATGATCATGTTCCGTGGTAAGAACATATTCCAAGCCCACTTACAAGTATAGCTTTCCCTTTAGCTT'
    complement = REVC(inputString)
    print(complement.reverse_complement)

if __name__ == '__main__':
    main()