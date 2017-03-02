'''Will also do PPER here since these are simple. And MMCH since highly related'''
import math,itertools

class PMCH:
    def __init__(self):
        pass

    def get_maximum_matchings_of_complementary_basepair_edges(self,count_one,count_two):
        max_count,min_count = max(count_one,count_two),min(count_one,count_two)
        return math.factorial(max_count) // math.factorial(max_count - min_count)

    def get_maximum_matchings_of_basepair_edges(self,RNA_string):
        G_count,C_count  = RNA_string.count('G'),RNA_string.count('C')
        print(G_count,C_count)
        A_count, U_count = RNA_string.count('A'), RNA_string.count('U')
        return self.get_maximum_matchings_of_complementary_basepair_edges(G_count,C_count) * self.get_maximum_matchings_of_complementary_basepair_edges(A_count,U_count)

    def get_perfect_matchings_of_basepair_edges(self,RNA_string):
        '''factorial of count of GC pairs * factorial of count of AU pairs'''
        GC_count = RNA_string.count('G')
        AU_count = RNA_string.count('A')
        return math.factorial(GC_count) * math.factorial(AU_count)

    def get_partial_permutations(self,n,k):
        return len(list(itertools.combinations(range(n),k))) * math.factorial(k) % 1000000

def Main():
    solver = PMCH()
    RNA_string = 'AGAGUGCAAGUGUCUAUUUCCCUGCCGGAAUGAGUAACCGGGCUGUAUCCAGACGAGCGCGUAACUCGUCCC'
    #print(solver.get_perfect_matchings_of_basepair_edges(RNA_string))
    #print (solver.get_partial_permutations(93,9))
    RNA_string = 'UUGUUAAAGAGAUGCACGCGGUAGCUCAACAAGGGGUCCCAACCAUUCCGGUCGAAUGAUAUCCGGCAAACGGACACAUACCGCUCGGCC'
    print(solver.get_maximum_matchings_of_basepair_edges(RNA_string))

if __name__ == '__main__':
    Main()