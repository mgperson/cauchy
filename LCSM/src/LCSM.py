#Matt Person
#Rosalind Problem: LCSM
#source
'''Given: A collection of k (k≤100k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)'''

import sys
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class LCSM:
    def __init__(self,DNAStrings_file):
        self.ru = RosalindUtilities()
        self.DNAStrings = self.ru.read_input_file(DNAStrings_file)
        self.longest_common_substring = self.solve_for_longest_common_substring(self.DNAStrings)


    def generate_substrings_of_length_n(self,string,n):
        substrings = [string[i:(i+n)] for i in range(len(string) - n + 1)]
        return substrings

    def generate_all_substrings(self,string):
        substrings = []
        for i in range(len(string),0,-1):
            [substrings.append(j) for j in self.generate_substrings_of_length_n(string,i)]
        return substrings

    def find_substring_in_string(self,string,substring):
        return substring in string

    def solve_for_longest_common_substring(self,DNAStrings):
        longest_substing = ''
        first_string = DNAStrings[0][1]
        for substring in self.generate_all_substrings(first_string):
            found_in_all = True
            for i in range(1,len(DNAStrings)):
                if not self.find_substring_in_string(DNAStrings[i][1],substring):
                    found_in_all = False;
                    break;
            if found_in_all:
                return substring
        return longest_substing



def main():
    lcsm = LCSM('input/rosalind_lcsm.txt')
    print(lcsm.longest_common_substring)

if __name__ == '__main__':
    main()


