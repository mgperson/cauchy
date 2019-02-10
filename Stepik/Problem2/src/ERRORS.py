import math
import numpy

class ERRORS:
    def __init__(self, L, n, p, k, cache):
        self.L = L
        self.n = n
        self.p = p
        self.k = k
        self.cache = cache
        self.probability_read_array = self.initialize_probability_read_array()
        self.probability_of_reads_array = self.series(1-self.n/self.L,self.n/self.L,self.k)
        self.answer = self.calculate_expected_misreads()
        #print(self.probability_of_reads_array)

    def __str__(self):
        return str(self.answer)

    def calculate_expected_misreads(self):
        return sum([self.calculate_probability_incorrect(i)*self.probability_of_reads_array[i] for i in range(self.k+1)])*self.L

    def calculate_probability_incorrect(self,num_reads):
        if num_reads == 0:
            return 0.75
        distribution_probability = self.series(1-self.p,self.p,num_reads)
        #print(distribution_probability)
        result = 0
        for num_incorrect in range(num_reads+1):
            num_correct_reads = num_reads - num_incorrect
            is_incorrect = self.get_is_incorrect_decision(num_correct_reads,num_incorrect)*distribution_probability[num_incorrect]
            result += is_incorrect
        return result

    # def get_is_incorrect_decision(self,correct_reads,incorrect_reads):
    #     if correct_reads == incorrect_reads:
    #         return 0.5
    #     return incorrect_reads > correct_reads

    def get_probability_distribution_of_incorrect_reads(self,incorrect_reads,buckets):
        k,N = incorrect_reads,buckets
        key = str(k)+':'+str(N)
        if key in self.cache.keys():
            return self.cache[key]
        answer = [self.calculate_multinomial_probability(N,k,x) for x in range(k+1)]
        self.cache[key] = answer
        return answer


    def calculate_multinomial_probability(self,N,k,x):
        term_one = (math.factorial(k)/(math.factorial(x)*math.factorial(k-x)))
        term_two = ((N-1) ** (k-x))/N**k
        return term_one*term_two

    def get_is_incorrect_decision(self,correct_reads,incorrect_reads):
        #if more correct reads, obviously we chose the correct one
        if correct_reads > incorrect_reads:
            return 0
        #pigeonhole principle, if at least one incorrect nucleotide HAS to have more reads than the correct one it's incorrect
        if (incorrect_reads - 1) // 3 + 1 > correct_reads:
            return 1
        #brute_force_probability = self.get_brute_force_probability(correct_reads,incorrect_reads)
        #brute_force_probability = self.get_brute_force_probability(correct_reads,2)
        #return brute_force_probability
        probability = self.get_probability_incorrect_decision(correct_reads,incorrect_reads)
        return probability

    def get_probability_incorrect_decision(self,correct_reads,incorrect_reads):
        incorrect_probability = 0
        prob_incorrect_reads_for_C = self.get_probability_distribution_of_incorrect_reads(incorrect_reads,3)
        for incorrect_C_reads in range(len(prob_incorrect_reads_for_C)):
            prob_incorrect_reads_for_G = self.get_probability_distribution_of_incorrect_reads(incorrect_reads-incorrect_C_reads,2)
            for incorrect_G_reads in range(len(prob_incorrect_reads_for_G)):
                prob_incorrect_reads_for_T = self.get_probability_distribution_of_incorrect_reads(incorrect_reads-incorrect_C_reads-incorrect_G_reads,1)
                for incorrect_T_reads in range(len(prob_incorrect_reads_for_T)):
                    probability_of_distribution = prob_incorrect_reads_for_C[incorrect_C_reads]*prob_incorrect_reads_for_G[incorrect_G_reads]*prob_incorrect_reads_for_T[incorrect_T_reads]
                    error_probability_with_distribution = self.get_error_probability_with_distribution(correct_reads,incorrect_C_reads,incorrect_G_reads,incorrect_T_reads)
                    incorrect_probability += probability_of_distribution*error_probability_with_distribution

        # distributions = self.get_distributions(incorrect_reads)
        # for distribution in distributions:
        #     c_count,g_count,t_count = distribution[0],distribution[1],distribution[2]
        #     error_probability_with_distribution = self.get_error_probability_with_distribution(correct_reads,c_count,g_count,t_count)
        #     probability_of_distribution = prob_incorrect_reads_per_bucket[c_count]*prob_incorrect_reads_per_bucket[g_count]*prob_incorrect_reads_per_bucket[t_count]
        #     incorrect_probability += error_probability_with_distribution*probability_of_distribution
        return incorrect_probability


    def get_distributions(self,total_reads):
        distributions = []
        for c_count in range(total_reads,-1,-1):
            for g_count in range(total_reads-c_count,-1,-1):
                for t_count in range(total_reads-c_count-g_count,total_reads-c_count-g_count-1,-1):
                    distributions.append([c_count,g_count,t_count])
        return distributions

    def get_brute_force_probability(self,correct_reads,incorrect_reads):
        key = str(correct_reads) + ':' + str(incorrect_reads)
        if key in self.cache.keys():
            return self.cache[key]
        #let's assume the correct read is 'A' and 'C','G','T' incorrect
        error_count = 0
        possibilities = self.generate_distributions(incorrect_reads)
        num_count = len(possibilities)
        for possibility in possibilities:
            counts = sorted([possibility.count('G'),possibility.count('C'),possibility.count('T')])
            error_count += self.get_error_probability_with_distribution(correct_reads, counts[0],counts[1],counts[2])
        answer = error_count / num_count
        self.cache[key] = answer
        #print(key + ' : ' + str(answer))
        return answer


    def get_error_probability_with_distribution(self,correct_reads,G_count,C_count,T_count):
        number_equal_to_correct_reads = (1 if C_count == correct_reads else 0) + (
            1 if G_count == correct_reads else 0) + (1 if T_count == correct_reads else 0)
        if C_count > correct_reads or G_count > correct_reads or T_count > correct_reads:
            return 1
        elif number_equal_to_correct_reads > 0:
            return (number_equal_to_correct_reads) / (number_equal_to_correct_reads + 1)
        return 0

    def generate_distributions(self,number):
        if number == 0:
            return ['']
        distributions = []
        remaining_distributions = self.generate_distributions(number-1)
        for remaining_distribution in remaining_distributions:
            distributions.append('C' + remaining_distribution)
            distributions.append('G' + remaining_distribution)
            distributions.append('T' + remaining_distribution)
        return distributions


    #basic binomial expansion
    def calculate_probability_of_reads_array(self):
        result = [None]*(self.k+1)
        a = 1 - self.n/self.L
        b = self.n/self.L
        term = a**self.k
        result[0] = term
        for i in range(1,self.k+1):
            term = term * b * (self.k - i + 1) / (i * a)
            result[i] = term
        return result

    def series(self,A, X, n):
        term = pow(A, n)
        result = [None] * (n+1)
        result[0] = term
        # Computing and printing remaining terms
        for i in range(1, n + 1):
            term = term * X * (n - i + 1) / (i * A)
            result[i] = term

        return result

    #def calculate_expected_misreads(self):
     #   return sum([self.calculate_expected_misread(i) for i in self.probability_read_array])

    def calculate_expected_misread(self,probability_read):
        return (1-probability_read)*0.75

    def initialize_probability_read_array(self):
        non_first_read_percentage = self.get_non_first_read_percentage()
        return [1 if i < self.n else non_first_read_percentage for i in range(self.L)]

    def get_non_first_read_percentage(self):
        return 1 - ((self.L - self.n)/self.L)**(self.k-1)

def Main():
    #L,n,p,k = 4,2,0,1
    #L, n, p, k = 10, 3, 0, 4
    input = '''10
3 2 0.000 1
3 2 0.000 2
15 6 0.005 10
15 3 0.027 18
31 5 0.054 43
81 17 0.085 80
210 11 0.034 156
4341 23 0.016 3681
8573 31 0.088 100
8093 43 0.007 2511
'''.split('\n')

    input = '''10
3 2 0.000 1
3 2 0.000 2
15 6 0.005 10
15 3 0.027 18
31 5 0.054 43
81 17 0.085 80
210 11 0.034 92
321 60 0.016 99
711 36 0.088 120
1693 62 0.001 150
'''.split('\n')

    input_t = '''3
4 2 0.000 1
4 2 0.000 2
10 3 0.050 4
'''.split('\n')

    brute_force_cache = {}

    with open('solution.txt','w') as output:
        #for i in range(int(input[0])):
        for i in range(10):
            line = input[i+1].split()
            L,n,p,k = int(line[0]),int(line[1]),float(line[2]),int(line[3])
            error = ERRORS(L,n,p,k,brute_force_cache)
            print(error)
            output.write(str(error.answer) + '\n')

if __name__ == '__main__':
    Main()