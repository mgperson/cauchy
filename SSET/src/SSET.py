#Matt Person
#Rosalind Problem: SSET
#source
'''Given: A positive integer n (n≤1000).
Return: The total number of subsets of {1,2,…,n} modulo 1,000,000.'''

class SSET:
    def __init__(self,n):
        self.number_of_subsets = 2**n % 1000000

def Main():
    sset = SSET(858)
    print(sset.number_of_subsets)

if __name__ == '__main__':
    Main()
