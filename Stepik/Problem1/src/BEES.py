from math import fabs

class BEES:
    def __init__(self,n,a,b):
        self.initial_n = n
        self.a = a
        self.b = b
        res = self.find_limit()
        if res == -1:
            self.limit = -1
        elif res == 0:
            self.limit = 0

    def __str__(self):
        if self.limit == -1:
            return str(-1)
        return str(0 if self.limit < 0 else round(self.limit,4))

    def find_limit(self):
        n_i, n_i_plus_1 = -1,self.initial_n
        iter_limit = 1000000
        current_iter = 0
        while(not self.is_limit_reached(n_i,n_i_plus_1)):
            n_i = n_i_plus_1
            n_i_plus_1 = self.calculate_next_generation_n(n_i_plus_1)
            current_iter += 1
            if n_i_plus_1 < 0.0001:
                return 0
            if current_iter > iter_limit or n_i_plus_1 > 100000000:
                if current_iter > iter_limit:
                    self.limit = n_i_plus_1
                    return n_i_plus_1
                else:
                    return -1
        self.limit = n_i_plus_1
        return self.limit

    def is_limit_reached(self,n_1,n_2):
        limit_reached = n_1 == n_2 or abs(n_1 - n_2) <= 0.000001
        return limit_reached

    def calculate_next_generation_n(self,n_i):
        return self.a*n_i - self.b * (n_i ** 2)


def Main():
    input = '''3
0.5 1 1
10 1 2
0.5 1.5 1
'''.split('\n')

    input = '''50
0.500 1.000 1.000
10.000 1.000 2.000
0.500 1.500 1.000
0.100 2.000 2.000
0.500 1.500 0.500
0.500 3.000 1.000
0.500 3.000 2.000
1.717 1.121 1.439
0.679 1.636 1.189
4.593 1.357 1.232
0.076 0.364 0.308
2.759 2.018 0.691
1.047 1.071 0.000
0.000 0.000 2.446
1.728 2.909 1.622
0.291 2.182 2.231
0.307 0.727 1.598
6.418 1.155 2.908
0.648 1.455 1.604
0.679 1.273 1.292
0.272 2.455 1.799
0.718 2.364 1.592
0.093 0.636 1.668
0.813 2.636 2.769
0.340 0.909 2.370
0.024 0.091 2.514
0.287 1.000 1.664
0.133 1.364 2.018
2.321 1.545 0.513
0.456 2.000 2.328
1.473 2.818 1.266
0.049 1.091 0.995
0.048 0.182 1.938
0.103 0.818 1.495
0.348 0.545 0.678
0.372 1.818 2.625
2.345 2.091 0.567
0.264 0.273 0.635
0.157 1.909 2.847
0.391 0.455 0.881
2.233 2.545 0.902
0.258 1.182 1.103
0.394 2.464 0.000
1.695 0.420 0.000
0.530 2.273 1.758
0.153 1.747 0.000
3.987 0.437 2.068
1.037 1.727 0.692
1.783 1.981 0.000
0.448 2.727 2.132
'''.split('\n')

    input_b = '''1
    1.047 1.071 0.000
    '''.split('\n')


    with open('solution.txt','w') as output:
        for i in range(int(input[0])):
            line = input[i+1].split()
            line = map(float,line)
            line = list(line)
            result = BEES(line[0],line[1],line[2]).limit
            #print('case:' + str(i))
            output.write(str(BEES(line[0],line[1],line[2])) + '\n')
            #print(BEES(line[0],line[1],line[2]))

if __name__ == '__main__':
    Main()
