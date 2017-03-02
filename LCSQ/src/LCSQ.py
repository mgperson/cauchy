class LCSQ:
    def __init__(self):
        self.longest_common_subsequence_ij = {}
        pass

    def get_longest_common_subsequence(self,s,t):
        len_s = len(s)
        len_t = len(t)
        if (len_s == 0 or len_t == 0):
            return ''
        self.load_longest_common_subsequence_ij(s,t,len_s,len_t)
        #print (self.longest_common_subsequence_ij)
        return self.construct_longest_subsequence(s,len_s,len_t)

    def is_subsequence(self,s,u):
        len_s = len(s)
        s_index = 0
        for i in u:
            while (s[s_index] != i):
                s_index += 1
                if (s_index == len_s):
                    return False
        return True

    def load_longest_common_subsequence_ij(self,s,t,len_s,len_t):
        for i in range(len_s):
            for j in range(len_t):
                self.longest_common_subsequence_ij[str(i) + ':' + str(j)] = \
                    max(self.get_longest_common_subsequence_ij(i-1,j),self.get_longest_common_subsequence_ij(i,j-1),\
                        self.get_longest_common_subsequence_ij(i-1,j-1) + 1 if s[i] == t[j] else 0)
                pass

    def construct_longest_subsequence(self,s,len_s,len_t):
        i,j = len_s -1, len_t - 1
        length_lcsq = self.get_longest_common_subsequence_ij(i,j)
        result = ''
        while (length_lcsq > 0):
            # move up
            while (length_lcsq == self.get_longest_common_subsequence_ij(i,j-1)):
                j-=1
            #move left
            while (length_lcsq == self.get_longest_common_subsequence_ij(i - 1,j)):
                i -= 1
            result += s[i]
            length_lcsq -= 1
            i-= 1
            j-=1
        return result[::-1]


    def get_longest_common_subsequence_ij(self,i,j):
        return 0 if (i < 0 or j < 0) else self.longest_common_subsequence_ij[str(i) + ':' + str(j)]


def Main():
    lcsq = LCSQ()
    s = 'TCGACACTAATTTATGGTAACAAACGGAGAATAGAAGCAATTGGCACGATTTTTATGAAGTAATTCAATAAGTGAAATAAAAGAACTAGTGCACTGGAAAAACGACATACATCGTTTCCCCCAAGAAAGAAAATGATGCATATTAAGATCACGTAAATCCCAGGGCCTTTTCAAGTCGGAGGGATTAGGGGGTTACCCATCAGTACGTTATCTTGTCGTGTGTGCTTAGCGCGAACCCCACAGACTAGGGAGCACCAGTTTGGAGTGATGTCAGTGAAGCGTGCCTTTCTAAGCCCAATGATGTCTGAGCGTAGAGACGCTAGAAGTCTGAGTCACCATGTTGAATAACAGGAGTTCCAGCTAACCGGTCCCAAACCACTTGGTACCCATATTAGGGCATGTGTATGCCATGTACCTCCTCGAGGGGATTCGGGTCTTGGCCTTGAATCTCGATACAGTGTTGGGAAATGTCAGGGTTGCGCTCGCCGAGAGCCCCCATGTGGCAACGTCCGGTCTGATAGGGCCCACTGCAGCCATGCTTAGAATCCAGCTGTCTCAGGGATTTAAGGTGGCCCTGAGCGTCCGATCGGTTCGGATCCTTCAGGTTTACGAAGCATGCTGGCTAACACAATCGGCTGTCCCACTCACTCGATTAACTTCACAGCACCTCACTCGTGATGAGAGTCGATGCCTAGGTAACTAAACGCTAGAAATCACCCAGTTTTTAGGATACCGAAGTTTAATGATGTCAAGGGCACAACAATATGCATTACGTTCGCGTACCTGGAGGTCCTATTGGCAGAGTGTAATGCTCAATGGGTACACCTATGCTCCGCTATTGCTGGAAGCTCAGTGTCGGACGAGCACACGTAGATAGGCGACTCACTTAAAGCGAGGTAATAGGGAGGAACCGTTCAAAGCTTACTGACCCCGAGAGGGAAGCGGTAATCCTCTAAAAG'
    t = 'AATTGAATCTGTCTGCAGCCACACCGTACTGTGGGCGAGCCTAAGTGCCGGTCTAGTTGCGGCTTACTAGTCTGGCTATTCCCCGGAGGTGCTACAGAGAGCCAGGTCGCGGTAGTGGTAGGGCGACGCAAAGTTGTGAGTACAGCGCACCATTAGCGGTGATACGAACTATGTTTAGCAAGTAAGGGTAGGAATTAAAACTCGAGCCCCATATGTTTCCCGGTGGGCATCGCAGCTCGTGGCCAAGCCATGCCTCATTTACGACTGGGGTACTCTAGGAATTCAACGGGATGTCGAGTAACATTGACACTATATTACACGGGCAAGGCCCTTGTTTTTACTGACCCAGCAGTCACCCGTAAGCATGTTCAGGAGCCAGTCGACATCCTATAAGTGAAGATCTGCTCACTTACCCAAACGCCAGGCTCACTGAAGGGGACAAATTCATCTTGTCAGGTGGAGCCTAAAGATCGCCGTGTCCCCGTTCAGGACTCGGTCGTCCTTTCTTATTTAAGGCTAACAGGCTTGTTGGCGAAGCGGTTCTAATATAAGAGTGACGGGCTACTAAGGAAAATAATCTATCTGCTTTAGGGTTTCACGGTCAATCTGCATAGCTATAGATGGCCCCGAACAGGTAATACTCGCTGGGAAGTTTTTACGCAACACAGTTATCAACCGACTCACCTTAAACGCAGTAGGGCGCCATCGGGTAGAGTTCTGATTGCCGGTGATTGAGTCAAAGGACCGAGAGTATGGGCTCCACCCGGGAACAGAAATTAGACCCCGATCCGCGAATGGTGCCGTCAGTTACTGTCCCATTCCGCCGAGTTTTGTCACCC'
    print (lcsq.get_longest_common_subsequence(s,t))

if __name__ == '__main__':
    Main()


