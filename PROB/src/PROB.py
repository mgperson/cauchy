#Matt Person
#Rosalind Problem: PROB
#source
'''Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.
Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a
random string constructed with the GC-content found in A[k] will match ss exactly.'''
import math

class PROB:
    def __init__(self,s,A):
        self.B = self.calculate_all_probs_of_string_with_log(A,s)

    def calculate_GorC_and_AorT_prob(self,GC_content):
        return (GC_content/2,(1-GC_content)/2)

    def calculate_prob_of_string(self,gorc_content,aort_content,s):
        prob = 1
        for base in s:
            prob *= gorc_content if base in 'GC' else aort_content
        return round(math.log(prob,10),3)

    def calculate_all_probs_of_string_with_log(self,probs,s):
        results = []
        values = map(float,probs.split())
        for value in values:
            gorc,aort = self.calculate_GorC_and_AorT_prob(value)
            results.append(self.calculate_prob_of_string(gorc,aort,s))
        return results

def Main():
    GCs = '0.066 0.110 0.162 0.244 0.286 0.343 0.396 0.431 0.500 0.536 0.614 0.644 0.714 0.738 0.819 0.868 0.914'
    s = 'CGCCTGTGGTGTGATCTGAATCTTAATGGACGCTCCTACTGAGGACGCCCTATTTAAATCGCCCTGCACTTACGCGTTTGCTTTAGATCCAAACGCATCG'
    solver = PROB(s,GCs)
    print(*solver.B)

if __name__ == '__main__':
    Main()