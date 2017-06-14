#Matt Person
#Rosalind Problem: PPER
#source
'''Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.
Return: The total number of partial permutations P(n,k), modulo 1,000,000.'''
import math,itertools

class PPER:
    def __init__(self,n,k):
        self.partial_permutations = len(list(itertools.combinations(range(n), k))) * math.factorial(k) % 1000000

def Main():
    solver = PPER(93,9)
    print (solver.partial_permutations)

if __name__ == '__main__':
    Main()