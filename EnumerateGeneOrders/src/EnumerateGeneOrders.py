from itertools import permutations

class EnumerateGeneOrders:
    def __init__(self):
        pass

    def enumerate_n(self,n):
        return list(permutations([i for i in range(1,n+1)]))

    def get_length_of_enumeration_and_enumerate_n(self,n):
        enum = self.enumerate_n(n)
        #trick to set length of enumeration as a list for later unpacking
        return [[len(enum)]] + enum

    def enumerate_gene_order(self,n):
        return self.get_length_of_enumeration_and_enumerate_n(n)

def main():
    ego = EnumerateGeneOrders()
    input_n = 5
    [print(*j) for j in ego.enumerate_gene_order(input_n)]

if __name__ == '__main__':
    main()