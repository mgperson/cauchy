class LCSQ:
    def __init__(self,s,t):
        self.s,self.t = s,t
        self.len_s,self.len_t = len(s),len(t)
        self.longest_common_subsequence_dictionary = {}
        self.get_longest_common_subsequence()
        pass

    def get_longest_common_subsequence(self):
        if (self.len_s == 0 or self.len_t == 0):
            return ''
        self.load_longest_common_subsequence_ij()
        #print (self.longest_common_subsequence_ij)
        self.answer = self.construct_longest_subsequence()
        self.shortest_supersequence = self.construct_shortest_supersequence()

    def __is_subsequence(self,s,u):
        len_s = len(s)
        s_index = 0
        for i in u:
            while s[s_index] != i:
                s_index += 1
                if (s_index == len_s):
                    return False
        return True

    def load_longest_common_subsequence_ij(self):
        for i in range(self.len_s):
            for j in range(self.len_t):
                penalty = 1 if self.s[i] == self.t[j] else 0
                self.longest_common_subsequence_dictionary[str(i) + ':' + str(j)] = \
                    max(self.get_longest_common_subsequence_ij(i-1,j),self.get_longest_common_subsequence_ij(i,j-1),\
                        self.get_longest_common_subsequence_ij(i-1,j-1) + penalty)

    def construct_shortest_supersequence(self):
        i, j = self.len_s - 1, self.len_t - 1
        length_lcsq = self.get_longest_common_subsequence_ij(i, j)
        result = ''
        while (length_lcsq > 0):
            # move up
            while (length_lcsq == self.get_longest_common_subsequence_ij(i, j - 1)):
                result += self.t[j]
                j -= 1
            # move left
            while (length_lcsq == self.get_longest_common_subsequence_ij(i - 1, j)):
                result += self.s[i]
                i -= 1
            result += self.s[i]
            length_lcsq -= 1
            i -= 1
            j -= 1
        if (i >= 0):
            while i >= 0:
                result += self.s[i]
                i -= 1
        if (j >= 0):
            while j >= 0:
                result += self.t[j]
                j -= 1
        return result[::-1]

    def construct_longest_subsequence(self):
        i,j = self.len_s - 1, self.len_t - 1
        length_lcsq = self.get_longest_common_subsequence_ij(i,j)
        result = ''
        while (length_lcsq > 0):
            # move up
            while (length_lcsq == self.get_longest_common_subsequence_ij(i,j-1)):
                j -= 1
            #move left
            while (length_lcsq == self.get_longest_common_subsequence_ij(i - 1,j)):
                i -= 1
            result += self.s[i]
            length_lcsq -= 1
            i -= 1
            j -= 1
        return result[::-1]


    def get_longest_common_subsequence_ij(self,i,j):
        return 0 if (i < 0 or j < 0) else self.longest_common_subsequence_dictionary[str(i) + ':' + str(j)]


def Main():
    lcsq = LCSQ()
    s = 'TCGACACTAATTTATGGTAACAAACGGAGAATAGAAGCAATTGGCACGATTTTTATGAAGTAATTCAATAAGTGAAATAAAAGAACTAGTGCACTGGAAAAACGACATACATCGTTTCCCCCAAGAAAGAAAATGATGCATATTAAGATCACGTAAATCCCAGGGCCTTTTCAAGTCGGAGGGATTAGGGGGTTACCCATCAGTACGTTATCTTGTCGTGTGTGCTTAGCGCGAACCCCACAGACTAGGGAGCACCAGTTTGGAGTGATGTCAGTGAAGCGTGCCTTTCTAAGCCCAATGATGTCTGAGCGTAGAGACGCTAGAAGTCTGAGTCACCATGTTGAATAACAGGAGTTCCAGCTAACCGGTCCCAAACCACTTGGTACCCATATTAGGGCATGTGTATGCCATGTACCTCCTCGAGGGGATTCGGGTCTTGGCCTTGAATCTCGATACAGTGTTGGGAAATGTCAGGGTTGCGCTCGCCGAGAGCCCCCATGTGGCAACGTCCGGTCTGATAGGGCCCACTGCAGCCATGCTTAGAATCCAGCTGTCTCAGGGATTTAAGGTGGCCCTGAGCGTCCGATCGGTTCGGATCCTTCAGGTTTACGAAGCATGCTGGCTAACACAATCGGCTGTCCCACTCACTCGATTAACTTCACAGCACCTCACTCGTGATGAGAGTCGATGCCTAGGTAACTAAACGCTAGAAATCACCCAGTTTTTAGGATACCGAAGTTTAATGATGTCAAGGGCACAACAATATGCATTACGTTCGCGTACCTGGAGGTCCTATTGGCAGAGTGTAATGCTCAATGGGTACACCTATGCTCCGCTATTGCTGGAAGCTCAGTGTCGGACGAGCACACGTAGATAGGCGACTCACTTAAAGCGAGGTAATAGGGAGGAACCGTTCAAAGCTTACTGACCCCGAGAGGGAAGCGGTAATCCTCTAAAAG'
    t = 'AATTGAATCTGTCTGCAGCCACACCGTACTGTGGGCGAGCCTAAGTGCCGGTCTAGTTGCGGCTTACTAGTCTGGCTATTCCCCGGAGGTGCTACAGAGAGCCAGGTCGCGGTAGTGGTAGGGCGACGCAAAGTTGTGAGTACAGCGCACCATTAGCGGTGATACGAACTATGTTTAGCAAGTAAGGGTAGGAATTAAAACTCGAGCCCCATATGTTTCCCGGTGGGCATCGCAGCTCGTGGCCAAGCCATGCCTCATTTACGACTGGGGTACTCTAGGAATTCAACGGGATGTCGAGTAACATTGACACTATATTACACGGGCAAGGCCCTTGTTTTTACTGACCCAGCAGTCACCCGTAAGCATGTTCAGGAGCCAGTCGACATCCTATAAGTGAAGATCTGCTCACTTACCCAAACGCCAGGCTCACTGAAGGGGACAAATTCATCTTGTCAGGTGGAGCCTAAAGATCGCCGTGTCCCCGTTCAGGACTCGGTCGTCCTTTCTTATTTAAGGCTAACAGGCTTGTTGGCGAAGCGGTTCTAATATAAGAGTGACGGGCTACTAAGGAAAATAATCTATCTGCTTTAGGGTTTCACGGTCAATCTGCATAGCTATAGATGGCCCCGAACAGGTAATACTCGCTGGGAAGTTTTTACGCAACACAGTTATCAACCGACTCACCTTAAACGCAGTAGGGCGCCATCGGGTAGAGTTCTGATTGCCGGTGATTGAGTCAAAGGACCGAGAGTATGGGCTCCACCCGGGAACAGAAATTAGACCCCGATCCGCGAATGGTGCCGTCAGTTACTGTCCCATTCCGCCGAGTTTTGTCACCC'
    print(lcsq._LCSQ__is_subsequence(s,t))
    print (lcsq.get_longest_common_subsequence(s,t))

if __name__ == '__main__':
    Main()


