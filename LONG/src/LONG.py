import os
import sys,difflib
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class LONG:
    def __init__(self,file):
        self.ru = RosalindUtilities()
        values = self.ru.read_input_file(file)
        self.strands = [value[1] for value in values]

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
        '''s = difflib.SequenceMatcher(None, a, b)
        pos_a, pos_b, size = s.find_longest_match(0, len(a), 0, len(b))
        return a + b[size:] if pos_a != 0 else b + a[size:]'''
        #return a[pos_a:pos_a + size]
        if a in b:
            return b
        if b in a:
            return a
        overlap_ab,overlap_ba = self.get_maximum_overlap_length(a,b), self.get_maximum_overlap_length(b,a)
        return a + b[overlap_ab:] if overlap_ab > overlap_ba else b + a[overlap_ba:]

    '''def get_super_string_of_string_list(self,strings):
        result = strings.pop()
        max_overlap = 0
        while len(strings) > 0:
            for string in strings:
                overlap = self.get_maximum_overlap_length(result,string)
                if overlap > max_overlap:
                    max_overlap = overlap
                    max_overlap_string = string
            result = self.get_super_string_of_strings(result,string)
            strings.remove(string)
        return result'''

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
            print (new_string,strings,max_overlap_indices)
            old_string_a,old_string_b = strings[max_overlap_indices[0]],strings[max_overlap_indices[1]]
            strings.remove(old_string_a)
            strings.remove(old_string_b)
            strings.append(new_string)
            print(strings)
        return strings[0]

    def verify_strands_in_result(self,result):
        for strand in self.strands:
            if not strand in result:
                return False
        return True

    def write_to_output(self,file,result):
        with open(file,'w') as output_data:
            output_data.write(result)

def Main():
    solver = LONG('dataset_1')
    #solver.get_maximum_overlap_length(solver.strands[0],solver.strands[1])
    a = 'ATTAGACCTG'
    b = 'CCTGCCGGAA'
    solver.get_maximum_overlap_length(a,b)
    result = solver.get_super_string_of_string_list(solver.strands)
    print(solver.verify_strands_in_result(result))
    solver.write_to_output('result',result)
    #print(result,end='')

if __name__ == '__main__':
    Main()