#Matt Person
#Rosalind Problem: LEXF
#source
'''Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
Return: All strings of length nn that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).'''

import itertools

class LEXF:
    def __init__(self,a,n):
        results = []
        for iter in itertools.product(sorted(a), repeat=n):
            result = ''
            for letter in iter:
                result += letter
            results.append(result)
        self.lexicographical_order_of_alphabet = results


def Main():
    a = 'A B C D E F G H'.split()
    n = 3
    solver = LEXF(a, n)
    print(*solver.lexicographical_order_of_alphabet)


if __name__ == '__main__':
    Main()