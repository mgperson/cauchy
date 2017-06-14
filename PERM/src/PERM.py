#Matt Person
#Rosalind Problem: PERM
#source
'''Given: A positive integer n≤7.
Return: The total number of permutations of length nn, followed by a list of all such permutations (in any order).'''

from itertools import permutations

class PERM:
    def __init__(self,n):
        self.enumerated_gene_order = self.enumerate_gene_order(n)

    def enumerate_n(self,n):
        return list(permutations([i for i in range(1,n+1)]))

    def get_length_of_enumeration_and_enumerate_n(self,n):
        enum = self.enumerate_n(n)
        #trick to set length of enumeration as a list for later unpacking
        return [[len(enum)]] + enum

    def enumerate_gene_order(self,n):
        return self.get_length_of_enumeration_and_enumerate_n(n)

def main():
    ego = PERM(5)
    [print(*j) for j in ego.enumerated_gene_order]

if __name__ == '__main__':
    main()