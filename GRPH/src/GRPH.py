#Matt Person
#Rosalind Problem: GPRH
#source
'''Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.'''

import sys
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class GRPH:
    def __init__(self,values,k):
        self.values = values
        self.map = self.set_up_map(values,k)
        pass

    def set_up_map(self,values,k):
        result = {}
        #for label in values:
        for val in values:
            seq = val[1]
            key = self.get_prefix_of_length_k(seq,k)
            if key in result:
                labels = result.get(key)
                labels.append(val[0])
                result[key] = labels
            else:
                result[key] = [val[0]]
        return result

    def get_edges_for_tuple(self,input):
        return self.get_values_of_prefix(self.get_suffix_of_length_k(input[1],3))

    def get_all_edges_of_input(self):
        return [(head_tuple[0], tail) for head_tuple in self.values for tail in
                self.get_edges_for_tuple(head_tuple) if (head_tuple[0] != tail)]

    def get_prefix_of_length_k(self,input,k):
        return input[:k]

    def get_suffix_of_length_k(self,input,k):
        return input[len(input)-k:]

    def get_values_of_prefix(self,prefix):
        return self.map.get(prefix, [])


def Main():
    ru = RosalindUtilities()
    values = ru.read_input_file('sample.txt')
    graph = GRPH(values, 3)
    [print(*edge) for edge in graph.get_all_edges_of_input()]


if __name__ == '__main__':
    Main()