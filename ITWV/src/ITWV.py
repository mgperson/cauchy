class ITWV:
    def __init__(self,values):
        self.s = values[0]
        self.patterns = values[1:]
        self.n = len(self.patterns)
        self.matrix = {}
        for i in range(self.n):
            self.matrix[i] = {}
        self.get_matrix_of_interwoven_possibilities()

    def get_matrix_of_interwoven_possibilities(self):
        for i in range(self.n):
            for j in range(i,self.n):
                result = 1 if self.can_t_and_u_be_interwoven_into_s(self.s,self.patterns[i],self.patterns[j]) else 0
                self.matrix[i][j] = result
                if i != j:
                    self.matrix[j][i] = result
        return self.matrix

    def print_matrix(self):
        for i in range(self.n):
            print(*[self.matrix[i][j] for j in range(self.n)])



    def get_all_interwoven_strings_of_t_and_u(self,prefix,t,u):
        interwoven_strings = []
        if len(t) == 0:
            interwoven_strings.append(prefix + u)
        elif len(u) == 0:
            interwoven_strings.append(prefix + t)
        else :
            interwoven_strings += self.get_all_interwoven_strings_of_t_and_u(prefix + t[0], t[1:],u)
            interwoven_strings += self.get_all_interwoven_strings_of_t_and_u(prefix + u[0], t, u[1:])
        return interwoven_strings

    def can_t_and_u_be_interwoven_into_s(self,s,t,u):
        interwoven_strings = self.get_all_interwoven_strings_of_t_and_u('',t,u)
        for interwoven_string in interwoven_strings:
            if interwoven_string in s:
                return True
        return False

def Main():
    with open('Dataset1.txt') as input_data:
        lines = [line.strip('\n') for line in input_data]
    itwv = ITWV(lines)
    itwv.print_matrix()

if __name__ == '__main__':
    Main()