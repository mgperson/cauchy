import sys

class Problem2:
    def __init__(self):
        pass

    def get_complement(self,base):
        if base == 'C':
            return 'G'
        if base == 'G':
            return 'C'
        if base == 'A':
            return 'U'
        if base == 'U':
            return 'A'
        raise Exception

    def get_sequence_state_without_skip(self,sequence):
        base_stack = []
        state = 'perfect'
        #for base in sequence:
        for base in sequence :
            if len(base_stack) != 0 and base_stack[len(base_stack)-1] == self.get_complement(base):
                base_stack.pop()
            else:
                base_stack.append(base)
        if len(base_stack) == 0:
            return 'perfect'
        else:
            return base_stack

    def get_extra_base_list(self):
        if len(self.indeces_by_base['C']) != len(self.indeces_by_base['G']):
            if len(self.indeces_by_base['C']) > len(self.indeces_by_base['G']):
                return self.indeces_by_base['C']
            else:
                return self.indeces_by_base['G']
        if (len(self.indeces_by_base['A']) > len(self.indeces_by_base['U'])):
            return self.indeces_by_base['A']
        else:
            return self.indeces_by_base['U']

    def get_sequence_state_with_skip(self,sequence):
        self.load_indeces_lists(sequence)
        extra_base_list = self.get_extra_base_list()
        for i in extra_base_list:
            state = self.get_sequence_state_without_skip(sequence,i)
            if state == 'perfect':
                return 'almost perfect'
        return 'imperfect'

    def load_indeces_lists(self,sequence):
        self.indeces_by_base = {}
        self.indeces_by_base['C'] = []
        self.indeces_by_base['G'] = []
        self.indeces_by_base['A'] = []
        self.indeces_by_base['U'] = []
        for i in range(len(sequence)):
            base = sequence[i]
            self.indeces_by_base[base].append(i)

    def is_stack_almost_perfect(self,base_stack):
        base_stack_len = len(base_stack)
        for i in range(int(base_stack_len/2)):
            end_index = base_stack_len - 1 - i
            if base_stack[i] != self.get_complement(base_stack[end_index]):
                return 'imperfect'
        return 'almost perfect'

    def get_sequence_state(self,sequence):
        #simple check if even length since we can't skip 2
        result = self.get_sequence_state_without_skip(sequence)
        if result == 'perfect':
            return 'perfect'
        if len(sequence) %2 == 1:
            #print(result)
            return self.is_stack_almost_perfect(result)
        return 'imperfect'



def Main():
    solver = Problem2()
    #sequence = 'AGUCU'
    sequence = sys.stdin.readline().strip()
    print(solver.get_sequence_state(sequence))


if __name__ == '__main__':
    Main()