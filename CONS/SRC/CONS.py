import sys

sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class CONS:
    def __init__(self):
        self.ru = RosalindUtilities()
        self.profile_matrix = {}
        self.profile_matrix['A'] = {}
        self.profile_matrix['C'] = {}
        self.profile_matrix['G'] = {}
        self.profile_matrix['T'] = {}
        pass

    def load_profile_matrix(self,file):
        values = self.ru.read_input_file(file)
        self.string_length = len(values[0][1])
        for value in values:
            string = value[1]
            for i in range(len(string)):
                self.profile_matrix[string[i]][i] = self.profile_matrix[string[i]].get(i,0) + 1

    def group_count_by_letter_at_pos_i(self,i):
        return [(letter,self.profile_matrix[letter].get(i,0)) for letter in self.profile_matrix.keys()]

    def get_consensus_string(self):
        consensus_string = ''
        for i in range(self.string_length):
            grouping = self.group_count_by_letter_at_pos_i(i)
            consensus_string += max(grouping,key =lambda x:x[1])[0]
        return consensus_string

    #quick and dirty just to print output
    def print_matrix(self):
        print('A:',*[self.profile_matrix['A'].get(i,0) for i in range(self.string_length)])
        print('C:', *[self.profile_matrix['C'].get(i, 0) for i in range(self.string_length)])
        print('G:', *[self.profile_matrix['G'].get(i, 0) for i in range(self.string_length)])
        print('T:', *[self.profile_matrix['T'].get(i, 0) for i in range(self.string_length)])


def Main():
    cons = CONS()
    cons.load_profile_matrix('sample.txt')
    print(cons.get_consensus_string())
    cons.print_matrix()

if __name__ == '__main__':
    Main()
