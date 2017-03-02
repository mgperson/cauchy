class FIB:
    def __init__(self):
        pass

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
    fib = FIB()
    n,k = 28,2
    print(fib.get_fib_n_with_k(n,k))

if __name__ == '__main__':
    Main()