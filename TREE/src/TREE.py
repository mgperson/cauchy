#Matt Person
#Rosalind Problem: TREE
#source
'''Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on nn nodes that contains no cycles.
Return: The minimum number of edges that can be added to the graph to produce a tree.'''
class TREE:
    def __init__(self,input_file):
        with open(input_file) as input_data:
            lines = input_data.readlines()
        #a fully, minimally connected graph of n nodes will have n-1 edges. Thus, the number of edges to add is (n-1) - m, where m is the number of edges we have already
        self.minimum_edges_to_add = int(lines[0]) - len(lines[1:]) - 1


def Main():
    solver = TREE('sample.txt')
    print(solver.minimum_edges_to_add)

if __name__ == '__main__':
    Main()