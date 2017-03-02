import itertools

class FINALROUND2:
    def __init__(self,input_file):
        self.kmers = []
        self.read_input_cases(input_file)

    def print_output(self):
        print(*[0 for i in range(2,len(self.kmers))],sep='\n')

    def read_input_cases(self,input_file):
        with open(input_file) as input_data:
            while True:
                line = input_data.readline()
                if not line:break
                n,k = map(int,line.split())
                self.kmers.append([input_data.readline().strip('\n') for i in range(n)])

    def try_solve_for_one_superstring(self,kmer):
        super_len = len(kmer[0]) + len(kmer) - 1
        #Generate all strings len(super_len)
        if super_len > 10:
            return
        bases = ['A','C','G','T']
        print(kmer)
        strings = [''.join(p) for p in itertools.product(bases,repeat=super_len)]
        for string in strings:
            if all([read in string for read in kmer ]):
                print (string)
                break;



    def solve_all(self):
        for kmer in self.kmers:
            self.try_solve_for_one_superstring(kmer)

def Main():
    solver = FINALROUND2('Easy')
    solver.solve_all()
    solver.try_solve_for_one_superstring(solver.kmers[0])
    #solver.print_output()

if __name__ == '__main__':
    Main()