import sys

class PROBLEM2:
    def __init__(self):
        pass

    def initialize_sequence(self,sequence):
        #print('testing: ' + sequence)
        self.length = len(sequence)
        self.sequence = sequence
        self.is_index_mapped = [False for i in range(len(sequence))]
        self.mapped_pairs = {}
        self.indeces_by_base = {}
        self.indeces_by_base['C'] = []
        self.indeces_by_base['G'] = []
        self.indeces_by_base['A'] = []
        self.indeces_by_base['U'] = []
        self.load_indeces_lists()

    def load_indeces_lists(self):
        for i in range(len(self.sequence)):
            base = self.sequence[i]
            self.indeces_by_base[base].append(i)

    def is_complement(self,base_one,base_two):
        return (base_one == 'G' and base_two == 'C' or base_one == 'C' or base_two =='G' \
                or base_one == 'A' and base_two == 'U' or base_one == 'U' and base_two == 'A')

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

    def is_pair_perfect(self,i1,i2,j1,j2):
        return i1 < i2 < j1 < j2 or i1 < j1 < j2 < i2

    #O(n2) test, don't like it
    def get_mapping_state(self,num_unmapped):
        #check for even and unmapped
        perfect_state = 'perfect'
        #print(num_unmapped)
        if num_unmapped > 1:
            return 'imperfect'
        if num_unmapped == 1:
            perfect_state = 'almost perfect'
        # save state of mapping prior to testing
        marker = self.mapped_pairs.copy()
        # view keys in order
        for key in sorted(self.mapped_pairs.keys()):
            i1,i2 = key, self.mapped_pairs[key]
            self.mapped_pairs.pop(key)
            #check against all other keys
            for second_key in self.mapped_pairs.keys():
                j1,j2 = second_key, self.mapped_pairs[second_key]
                #print(i1, i2, j1, j2)
                if not self.is_pair_perfect(i1,i2,j1,j2):
                    self.mapped_pairs = marker
                    return 'imperfect'
        self.mapped_pairs = marker
        return perfect_state




    def map_pair(self,base,complement,i,j):
        self.mapped_pairs[i] = j
        self.indeces_by_base[base].remove(i)
        self.indeces_by_base[complement].remove(j)
        self.is_index_mapped[i] = True
        self.is_index_mapped[j] = True

    def unmap_pair(self,base,complement,i,j):
        self.mapped_pairs.pop(i)
        self.indeces_by_base[base].append(i)
        self.indeces_by_base[complement].append(j)
        self.is_index_mapped[i] = False
        self.is_index_mapped[j] = False

    #first attempt, non recursive
    def map_all_pairs_and_get_state(self):
        number_unmapped = 0
        for i in range(len(self.is_index_mapped)):
            if not self.is_index_mapped[i]:
                base = self.sequence[i]
                complement = self.get_complement(base)
                # will need to check this step for Imperfect/Fail
                if len(self.indeces_by_base[complement]) > 0:
                    j = self.indeces_by_base[complement][0]
                    self.map_pair(base,complement,i,j)
                else:
                    number_unmapped += 1
                    if (number_unmapped > 1):
                        state = 'imperfect'
        state = self.get_mapping_state(number_unmapped)
        return(state)

    # generate all possible mappings
    # generates first mapping
    # recursive call for each decision of mapping
    # base case when no more indeces to be mapped
    # test mapping almost perfect/perfect = return
    # if nothing return imperfect
    def map_pairs_and_get_state(self,state):
        number_unmapped = 0
        #base case nothing left to map or only one left to map
        #if all(self.is_index_mapped):
        num_unmapped = sum([1 for i in self.is_index_mapped if not i])
        if num_unmapped == 0 or num_unmapped == 1:
            print(self.mapped_pairs)
            state = self.get_mapping_state(num_unmapped)
            return state

        for i in range(len(self.is_index_mapped)):
            if not self.is_index_mapped[i]:
                base = self.sequence[i]
                complement = self.get_complement(base)
                if len(self.indeces_by_base[complement]) > 0:
                    for j in self.indeces_by_base[complement]:
                    #j = self.indeces_by_base[complement][0]
                        if j > i:
                            self.map_pair(base, complement, i, j)
                            state = self.map_pairs_and_get_state(state)
                            if state == 'perfect' or state == 'almost perfect':
                                return state
                            self.unmap_pair(base,complement,i,j)
                #else:
                 #   number_unmapped += 1
                  #  if (number_unmapped > 1):
                   #     state = 'imperfect'
        #state = self.get_mapping_state(num_unmapped)
        #return (state)
        return state




def Main():
    #sequence = sys.stdin.readline().strip()
    #sequence = 'CAGUU'
    sequence = 'AGUCU'
    problem2 = PROBLEM2()
    problem2.initialize_sequence(sequence)
    #print(problem2.map_pairs_and_get_state('perfect'))
    # sequence = 'UGCA'
    # problem2.initialize_sequence(sequence)
    # print(problem2.map_pairs_and_get_state('perfect'))


if __name__ == '__main__':
    Main()