#Matt Person
#Rosalind Problem: INOD
#source
'''Given: A positive integer n (3≤n≤10000).
Return: The number of internal nodes of any unrooted binary tree having n leaves.'''

class INOD:
    def __init__(self,n):
        self.number_internal_nodes = n -2

def Main():
    inod = INOD(9534)
    print(inod.number_internal_nodes)

if __name__ == '__main__':
    Main()
