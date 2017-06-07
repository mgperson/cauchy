#Matt Person
#Rosalind Problem: FIB
#source
'''Given: Positive integers n≤40n≤40 and k≤5k≤5.
Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation,
every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).'''

class FIB:
    def __init__(self,n,k):
        self.num_rabbit_pairs = self.get_fib_n_with_k(n,k)

    def get_fib_n_with_k(self,n,k):
        if n <= 2:
            return 1
        prev, two_prev = 1,1
        for i in range(2,n):
            cur = two_prev*k + prev
            two_prev = prev
            prev = cur

        return cur

def Main():
    fib = FIB(28,2)
    print(fib.num_rabbit_pairs)

if __name__ == '__main__':
    Main()