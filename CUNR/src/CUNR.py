from math import factorial

class CUNR():
    def __init__(self):
        pass

    def get_num_distinct_unrooted_binary_trees(self,n):
        result = 1
        factor = 1
        for i in range(2,n):
            result *= factor
            factor += 2
        return result % 1000000


def Main():
    cunr = CUNR()
    n = 953
    print(cunr.get_num_distinct_unrooted_binary_trees(n))

if __name__ == '__main__':
    Main()
