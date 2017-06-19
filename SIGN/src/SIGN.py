#Matt Person
#Rosalind Problem: LGIS
#source
'''Given: A positive integer n≤6.
Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).'''

from itertools import product,permutations

class SIGN:
    def __init__(self,n):
        self.positive_and_negative_permutations  = list(self.get_positive_and_negative_permutations(range(1,n+1)))

    def get_positive_and_negative_permutations(self,items):
        for p in permutations(items):
            for signs in product([-1,1],repeat=len(items)):
                yield [a*sign for a,sign in zip(p,signs)]

def Main():
    sign = SIGN(3)
    print(len(sign.positive_and_negative_permutations))
    [print(*permutation) for permutation in sign.positive_and_negative_permutations]

if __name__ == '__main__':
    Main()