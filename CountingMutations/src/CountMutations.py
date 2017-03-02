'''Solutions for HAMM and PDST'''
import os
import sys
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class CountMutations:
    def __init__(self):
        self.distance_matrix = []
        self.ru = RosalindUtilities()
        self.reads = []

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

    def count_mutations(self,first_string,second_string):
        return self.count_string_differences(first_string,second_string)

def main():
    cm = CountMutations()
    first_string = 'AATTCGCCATTCGAGATGTTCATACAGCCGTCGTCCTAAAACGGATGGCCCGAGGCGTTCAGGGAGGATTGAGGCTCCCATGCCAGACGCACTTGCTGAGTATAATGGCCCAAAGCTTCTGTTCGCATTGTCGTCCGTCGTAAGCCCGATTTATGCAGGTACGAGGTAAACTCTAGCCAGGTTACAAACAATAAGATGAGGTAAGCTGGAATCTCACTGAGCTAAGACTGTATGAGGATGCCTTCCTCAAGTCGCGGGGATTTCTCAACCGAATGATAAGGCACACAATAAGATCCAGGTATAACTTGCTAGTAATGGGACAAGCGGTGCACTGCGATAGTGAAGAACCCGCAATATCGAAGAATTAGAGTCCCCTTTTATTTGGCGCAAAATCCGAATCGAGACGTGGTTTCGCGATAGCAAAAAACGGACCCGAGATTACTATAGTTTCCACAATTAAAGCCAAGGCAAACTGTAGACCAAGCGGATCTATTCGTTCCGACCGACCCTTGTACCACTGAGGCTGGGCGCATAGGTAGGGATGTAACCGCAAAACAAACTACCAATACAGTGCCCATTGGGGGCGAGGGGGTAACGTTGCGAATTACTATTGCGACTCTAACAAGGTGCGACCTTAACCCGTGGGTACCAACGCTCCGTCGCGTCAATTCCTCCTTTATTTTGTCATAGAATTGGCGTCGTACTCGCAGGATTTCTGTAAACAGATACTAAGAACCTAGCATGCGGTAGACACCCACAAGTTGCGAATCATTATATCGGCACCTTGCTCTTATGTTTTTTTGAGAAATCACACTGTATCTTCAAGATTGAGCAACCATTCTGTTTACGGGATAGTTGTTTGACCTTCCTAGCAGTTCGGAGTGGATTCTCCCCGGTGGCCTTTTTCA'
    second_string = 'TCGTCGCTATTTGATGGGTACTCTGAGTCGTCGTCATACGGTAACTGTGACGACTGGGCCTGGGTGATTTCTCTGTCCTTTCCGAAAAACGCCTGCTGAGTGTCATGGTCACAAGTGCCGCCTAGATTCGACTAGGGTCCGGAACCCAATTTGCTCTTGGCCCAGGTAGTATGTTTTACGGTTTCACATAATAATTCGAGTCCAACCTGAAACCTACCCTGCGAATACTGTACCTGGAGTCCATCCCCACGAGTCGGACCCTCTCCCATCAAAGGATACGAAACCACATCGGTGCTGTGGAAAACCCACACCTTGTCTGAAGAACTTGCCAATAGGTCAGTAAACTTCCCGCCATGCCCTAGAAATAGAGTCATCTTCAATACGAAACAAAATCCGAACCTGGGCGTCGTTCTCTGATAGCAAAATCAGACGTTACGAAAACTGTATATTCTAATATAATAGCCTAGGCATGAGGTAGATTCTGTCGACCGCTCCCTCCCCCCCGCCCCCTACCCAACCAACGCTTACCTCATTGTTATCGAGGTACCACGCAACCCATTAGCCACCACGATACCCCTTGGGGACGACGCGGCCTATTTGGGCATGGATAATCGGGCTATACTAGCCAGCTTCCTTGGCCAGTAGTTGGGAAGCAGCAATTCCCGGCTGTCTACACATCTCTTGTACTCGAATCGCCGTCGCGAGCGAGGACTTTCACCACGGACATTCTACGGACTTAGTCGCCTCACACAATCAACTATGGGTGAAGTTTCATAGGGGCACGCATCTCTAGAAAACTGTTGGGGTACCACGCCTACTAGGCAAGTCTATGCGGAGGACCCTATTATCGGACAGTCCAATCAACGCCCCAGCAGCTGATAGGGGGAACTCAGAGTCTGCACTTGTTG'
    #print(cm.count_mutations(first_string,second_string))
    cm.read_input_file_and_initialize_distance_matrix('sample')
    cm.get_distance_matrix()
    for i in range(len(cm.distance_matrix)):
        print (' '.join(map(str,cm.distance_matrix[i])))
    #print ('\n'.join(''.join(*zip(list(map(str,*row)))) for row in cm.distance_matrix))

if __name__ == '__main__':
    main()