import os, math
import sys
import itertools
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class TRIE():
    def __init__(self,trie_strings):
        self.adjacency_list = {}
        self.next_node_number = 1
        self.generate_adjacency_list(trie_strings)
        pass

    def generate_adjacency_list(self,trie_strings):
        for string in trie_strings:
            self.generate_adjacency_list_for_string(string)

    def generate_adjacency_list_for_string(self,string):
        current_node = 1
        for letter in string:
            edges = self.adjacency_list.get(current_node,{})
            if letter in edges:
                next_node = edges[letter]
            else:
                next_node = self.get_next_node_number()
                edges[letter] = next_node
                self.adjacency_list[current_node] = edges
            current_node = next_node

    def get_next_node_number(self):
        self.next_node_number += 1
        return self.next_node_number

    def get_adjacency_list_in_triplets(self):
        result = []
        for start_node in self.adjacency_list.keys():
            for edge in self.adjacency_list[start_node].keys():
                result.append((start_node,self.adjacency_list[start_node][edge],edge))
        return result

def Main():
    trie = ''
    with open('data.txt') as input_data:
        for line in input_data:
            trie += line
    solver = TRIE(trie.split())
    for triplet in solver.get_adjacency_list_in_triplets():
        print(*triplet)
    with open('output.txt','w') as output_data:
        for triplet in solver.get_adjacency_list_in_triplets():
            output_data.write(str(triplet[0]) + ' ' +  str(triplet[1]) + ' ' + triplet[2] + '\n')

if __name__ == '__main__':
    Main()