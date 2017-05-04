class LEXV():
    def __init__(self):
        pass

    def get_strings_length_n_from_A(self,output,A,prefix,n):
        #print(prefix,n)
        if n == 0:
            output.append(prefix)
            return
        if (prefix != ''):
            output.append(prefix)
        for i in range(len(A)):
            self.get_strings_length_n_from_A(output,A,prefix+A[i],n-1)

def Main():
    solver = LEXV()
    output = []
    A = ''.join('Q F D M H L G B J W U'.split())
    solver.get_strings_length_n_from_A(output,A,'',3)
    with open('output.txt','w') as output_data:
        for output in output:
            output_data.write(output + '\n')


if __name__ == '__main__':
    Main()

