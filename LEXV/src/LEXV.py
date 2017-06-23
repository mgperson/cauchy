#Matt Person
#Rosalind Problem: LEXV
#source
'''Given: Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4).
Return: All strings of length at most n formed from A, ordered lexicographically.
(Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)'''

class LEXV():
    def __init__(self,A,n):
        self.lexicographically_ordered_strings = []
        self.get_strings_length_n_from_A(self.lexicographically_ordered_strings,A,'',n)

    def get_strings_length_n_from_A(self,output,A,prefix,n):
        if n == 0:
            output.append(prefix)
            return
        if (prefix != ''):
            output.append(prefix)
        for i in range(len(A)):
            self.get_strings_length_n_from_A(output,A,prefix+A[i],n-1)

    def print_output(self,output_file):
        with open(output_file, 'w') as output_data:
            for output in self.lexicographically_ordered_strings:
                output_data.write(output + '\n')

def Main():
    n = 3
    A = ''.join('Q F D M H L G B J W U'.split())
    solver = LEXV(A,n)
    solver.print_output('output.txt')


if __name__ == '__main__':
    Main()

