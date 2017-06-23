#Matt Person
#Rosalind Problem: PDST
#source
'''Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given in FASTA format.
Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that your answer is allowed an absolute error of 0.001'''

import os
import sys
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class PDST:
    def __init__(self,input_file):
        self.distance_matrix = []
        self.ru = RosalindUtilities()
        self.reads = []
        self.read_input_file_and_initialize_distance_matrix(input_file)
        self.get_distance_matrix()

    def __str__(self):
        return '\n'.join([' '.join(map(str,self.distance_matrix[i])) for i in range(len(self.distance_matrix))])

    def read_input_file_and_initialize_distance_matrix(self,file):
        values = self.ru.read_input_file(file)
        for i in range(len(values)):
            value = values[i]
            self.distance_matrix.append([None]*len(values))
            self.reads.append(value[1])

    def get_distance_matrix(self):
        for i in range(len(self.reads)):
            self.distance_matrix[i][i] = round(0,5)
            for j in range(i+1,len(self.reads)):
                p_distance = self.get_p_distance(self.reads[i],self.reads[j])
                self.distance_matrix[i][j] = round(p_distance,5)
                self.distance_matrix[j][i] = round(p_distance, 5)

    def get_p_distance(self,first_string,second_string):
        return self.count_string_differences(first_string,second_string) /len(first_string)

    def count_string_differences(self,first_string,second_string):
        return sum(1 for a,b in zip(first_string,second_string) if a!=b)


def main():
    cm = PDST('sample')
    print(cm)

if __name__ == '__main__':
    main()