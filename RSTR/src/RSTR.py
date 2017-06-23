#Matt Person
#Rosalind Problem: RSTR
#source
'''Given: A positive integer N≤100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.
Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x
(see “Introduction to Random Strings”), then at least one of the strings equals s. We allow for the same random string to be created more than once.'''

import math

class RSTR:
    def __init__(self,N,x,s):
        self.probability_one_string_equals_s = self.calculate_prob_of_string_in_n_given_gc(s,N,x)

    def __str__(self):
        return str(self.probability_one_string_equals_s)

    def calculate_prob_of_string_in_n_given_gc(self,s,n,gc_content):
        G_or_C_content,A_or_C_content = self.calculate_GorC_and_AorT_prob(gc_content)
        prob_one_string_equal = 1
        for base in s:
            prob_one_string_equal *= G_or_C_content if base in 'GC' else A_or_C_content
        return round((1 - (1-prob_one_string_equal)**n),3)

    def calculate_GorC_and_AorT_prob(self,GC_content):
        return (GC_content/2,(1-GC_content)/2)

    def calculate_prob_of_string(self,gorc_content,aort_content,s):
        prob = 1
        for base in s:
            prob *= gorc_content if base in 'GC' else aort_content
        return round(math.log(prob,10),3)

def Main():
    GCs = '0.066 0.110 0.162 0.244 0.286 0.343 0.396 0.431 0.500 0.536 0.614 0.644 0.714 0.738 0.819 0.868 0.914'
    s = 'CGCCTGTGGTGTGATCTGAATCTTAATGGACGCTCCTACTGAGGACGCCCTATTTAAATCGCCCTGCACTTACGCGTTTGCTTTAGATCCAAACGCATCG'
    gc = 0.423093
    s = 'TTGGATCCTT'
    n = 92492
    solver = RSTR(n,gc,s)
    print(solver)

if __name__ == '__main__':
    Main()