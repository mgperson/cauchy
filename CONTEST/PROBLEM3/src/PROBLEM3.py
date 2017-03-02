import sys, re, time, itertools

class Problem3:
    def __init__(self,sequence):
        self.original_sequence = sequence
        self.original_sequence_state = {}
        self.reads = []
        self.counter = 0
        pass

    def process_read_match(self,read,match,start_index):
        #print(read, match)
        read_index = 0
        for i in range(len(read)):
            while read[i] != match[read_index]:
                if read_index+start_index in self.original_sequence_state and self.original_sequence_state[read_index+start_index] == 'I':
                    return False
                self.original_sequence_state[read_index+start_index] = 'E'
                read_index += 1
            if read_index + start_index in self.original_sequence_state and self.original_sequence_state[read_index + start_index] == 'E':
                return False
            self.original_sequence_state[read_index+start_index] = 'I'
            read_index += 1
        return True



    def create_re_string(self,read):
        result = read[0]
        bases = 'AGCT'
        for i in range(1,len(read)):
            char = read[i]
            result += '[' + bases.replace(char,'') + ']*' + char
        return result

    def process_reads(self,i):
        #base case out of reads
        #print(time.time() - self.timer)
        if self.counter > 10 or i >= len(self.reads):
            #print(self.original_sequence_state)
            #input()
            return True
        #self.counter += 1

        #print(self.reads[i])
        re_append = '[ACGT]*'
        #re_append =''
        re_string = '(?=(' + re_append.join(self.reads[i]) + '))'
        #re_string = self.create_re_string(self.reads[i])
        #re_string = re_append.join(read)
        #print (re_string)
        matches = re.finditer(re_string,self.original_sequence)
        #print(sum(1 for match in matches))
        #print(matches)
        for match in matches:
            #print(match)
            #print (match.group(1),match.span())
            temp_sequence_state = self.original_sequence_state.copy()
            if self.process_read_match(self.reads[i], match.group(1), match.span()[0]):
                if self.process_reads(i+1):
                    return True
            self.original_sequence_state = temp_sequence_state
        return False

    def generate_superstring_of_two_strings(self,a,b):
        overlap = ''
        len_a,len_b = len(a),len(b)
        min_len = min(len_a,len_b)
        # get overlap portion
        for i in range(min_len):
            if a[len_a - i -1] != b[i]:
                break
            overlap += b[i]
        #return ''.join([a[j] for j in range(len_a-i)]) + overlap + ''.join([b[j] for j in range(i,len_b)])
        return a[:len_a - len(overlap)] + overlap + b[len(overlap):]


    def get_superstring_of_permutation(self,permutation,strings):
        result = strings[permutation[0]]
        #print(result)
        for i in range(1,len(permutation)):
            #print(strings[i])
            result = self.generate_superstring_of_two_strings(result,strings[permutation[i]])
            #print(result)
        return result

    def is_subsequence(self,s,u):
        len_s = len(s)
        s_index = 0
        for i in u:
            while (s[s_index] != i):
                s_index += 1
                if (s_index == len_s):
                    return False
        return True

    def find_shortest_super_string(self,strings):
        shortest_super_string = ''
        shortest_super_string_length = 2**64
        for permutation in itertools.permutations(range(len(strings))):
            #print(permutation)
            super_string = self.get_superstring_of_permutation(permutation,strings)
            #print(super_string)
            if self.is_subsequence(self.original_sequence,super_string) and len(super_string) < shortest_super_string_length:
                shortest_super_string_length = len(super_string)
                shortest_super_string = super_string
        return super_string

    def print_indeces_of_reads_in_string(self,string):
        [print(string.find(read) + 1) for read in self.reads]



# def Main():
#     #solver = Problem3('CAAGGAATCGAGGATAGGCTGTGTCCGTCCATGAGGCCTTTTTCGGTACGGTCTTGATTACTTTTTTC')
#     #solver.reads = ['CTTTTT','AGGCTGG','TACTTTTTT','GGCTGGGCCTTTTCT','GCCTTTTCTTG']
#     #solver = Problem3('')
#     #solver.process_reads(0)
#     #result = [solver.original_sequence[i] for i in sorted(solver.original_sequence_state.keys()) if solver.original_sequence_state[i] != 'E']
#     #clip = ''.join(result)
#     #print(clip)
#     #[print(clip.index(read) + 1) for read in solver.reads]
#
#     #values = []
#     with open('1') as input_data:
#         solver = Problem3(input_data.readline().strip())
#         n = int(input_data.readline())
#         solver.reads = []
#         for i in range(n):
#             solver.reads.append(input_data.readline().strip())
#         solver.process_reads(0)
#         result = [solver.original_sequence[i] for i in sorted(solver.original_sequence_state.keys()) if solver.original_sequence_state[i] != 'E']
#         clip = ''.join(result)
#         print(clip)
#         for read in solver.reads:
#             if read in clip:
#                 print (clip.index(read) + 1)
#             else:
#                 print ('-1')
#
#     pass

def Main():
    with open('3') as input_data:
        solver = Problem3(input_data.readline().strip())
        n = int(input_data.readline())
        solver.reads = []
        for i in range(n):
            solver.reads.append(input_data.readline().strip())
        shortest_super_string = solver.find_shortest_super_string(solver.reads)
        print(shortest_super_string)
        solver.print_indeces_of_reads_in_string(shortest_super_string)

if __name__ == '__main__':
    Main()