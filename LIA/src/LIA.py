#MEH had to look up binomial expansions

import operator as op
from functools import reduce

class LIA:
    def __init__(self):
        self.count_of_genotype_dominant_base = {}
        self.count_of_genotype_dominant_base['Aa'] = 1
        pass

    def generate_expected_genotypes_for_genotype(self,genotype):
        result = {}
        A_count = genotype[:2].count('A')
        B_count = genotype[2:].count('B')
        A_pair = ['AA','Aa','aa']
        B_pair = ['BB', 'Bb', 'bb']
        for a_pair in A_pair:
            for b_pair in B_pair:
                result[a_pair + b_pair] = 1
        return result

    def update_expected_genotypes_with_next_gen(self):
        temp_count = self.count_of_genotype_dominant_base.copy()
        self.count_of_genotype_dominant_base['AA'] = temp_count.get('AA',0) * .5 \
            + temp_count.get('Aa',0) * .5 * .5
        self.count_of_genotype_dominant_base['Aa'] = temp_count.get('AA', 0) * .5 \
            + temp_count.get('Aa', 0) * .5 * .5 * 2 \
            + temp_count.get('aa',0) * .5
        self.count_of_genotype_dominant_base['aa'] = temp_count.get('Aa', 0) * .5 * .5  \
            + temp_count.get('aa', 0) * .5
        print(self.count_of_genotype_dominant_base)

    def get_count_of_genotype(self,genotype,n):
        return self.count_of_genotype_dominant_base[genotype]

    def get_combinations(self,n, r):
        print(n,r)
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
    lia = LIA()
    k,n = 6,17
    print(lia.get_expected_value_of_nAaBb_at_generation_k(k,n))

if __name__ == '__main__':
    Main()