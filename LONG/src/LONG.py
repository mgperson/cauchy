#Matt Person
#Rosalind Problem: LONG
#source
'''Given: At most 50 DNA strings of equal length, not exceeding 1 kbp, in FASTA format (which represent reads
deriving from the same strand of a single linear chromosome).
The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire
chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.
Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).'''

import sys
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class LONG:
    def __init__(self,file):
        self.ru = RosalindUtilities()
        values = self.ru.read_input_file(file)
        self.strands = [value[1] for value in values]
        self.shortest_superstring = self.get_super_string_of_string_list(self.strands)


    def get_maximum_overlap_length(self,a,b):
        len_a = len(a)
        len_b = len(b)
        if a in b or b in a:
            return min(len_a,len_b)
        for i in range(len_a,0,-1):
            if a[len_a-i:] == b[:i]:
                return i
        return 0


    def get_super_string_of_strings(self,a,b):
        if a in b:
            return b
        if b in a:
            return a
        overlap_ab,overlap_ba = self.get_maximum_overlap_length(a,b), self.get_maximum_overlap_length(b,a)
        return a + b[overlap_ab:] if overlap_ab > overlap_ba else b + a[overlap_ba:]

    def get_super_string_of_string_list(self,strings):
        while len(strings) > 1:
            max_overlap = 0
            for i in range(len(strings)):
                for j in range(len(strings)):
                    if i != j:
                        overlap = self.get_maximum_overlap_length(strings[i],strings[j])
                        if overlap > max_overlap:
                            max_overlap = overlap
                            max_overlap_indices = (i,j)
            new_string = self.get_super_string_of_strings(strings[max_overlap_indices[0]], strings[max_overlap_indices[1]])
            old_string_a,old_string_b = strings[max_overlap_indices[0]],strings[max_overlap_indices[1]]
            strings.remove(old_string_a)
            strings.remove(old_string_b)
            strings.append(new_string)
        return strings[0]

    #Used as a helper method while debugging solution
    def verify_strands_in_result(self,result):
        for strand in self.strands:
            if not strand in result:
                return False
        return True

    def write_to_output(self,file):
        with open(file,'w') as output_data:
            output_data.write(self.shortest_superstring)

def Main():
    solver = LONG('dataset_1')
    solver.write_to_output('result')

if __name__ == '__main__':
    Main()