import math

class EVAL():
    def __init__(self,n,DNA_string,gc_content_array):
        self.n = n
        self.s = DNA_string
        self.gc_content_array = gc_content_array

    def get_expected_s_in_n(self):
        return [round(self.calculate_prob_of_string(self.gc_content_array[i]/2,(1-self.gc_content_array[i])/2) * (self.n-1),3) for i in range(len(self.gc_content_array))]

    def calculate_prob_of_string(self, gorc_content, aort_content):
        prob = 1
        for base in self.s:
            prob *= gorc_content if base in 'GC' else aort_content
        return prob

def Main():
    n = 983148
    DNA_string = 'CATCCATGT'
    GC_content_array = list(map(float,'0.000 0.074 0.121 0.161 0.202 0.273 0.339 0.393 0.436 0.470 0.501 0.577 0.640 0.673 0.744 0.787 0.819 0.888 0.949 1.000'.split()))
    solver = EVAL(n,DNA_string,GC_content_array)
    print(*solver.get_expected_s_in_n())

if __name__ == '__main__':
    Main()