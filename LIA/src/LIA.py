#Matt Person
#Rosalind Problem: LIA
#source
'''Given: Two positive integers k (k≤7) and NN (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb.
Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.
Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level).
Assume that Mendel's second law holds for the factors.'''

import operator as op
from functools import reduce
import math, itertools

class LIA:
    def __init__(self,k,n):
        self.count_of_genotype_dominant_base = {}
        self.count_of_genotype_dominant_base['Aa'] = 1
        self.expected_value_of_nAaBb_at_generation_k = round(self.get_expected_value_of_nAaBb_at_generation_k(k,n),3)


    def get_combinations(self,n, r):
        r = min(r, n - r)
        if r == 0:
            return 1
        numer = reduce(op.mul, range(n, n - r, -1))
        denom = reduce(op.mul, range(1, r + 1))
        return numer // denom

    def get_expected_value_of_nAaBb_at_generation_k(self,k,n):
        N = 2**k
        print(N)
        return sum([self.get_combinations(N,i) *  0.25**i * 0.75 ** (N-i) for i in range(n,N+1)])


def Main():
    k, n = 6, 17
    lia = LIA(k,n)
    print(lia.expected_value_of_nAaBb_at_generation_k)


if __name__ == '__main__':
    Main()
