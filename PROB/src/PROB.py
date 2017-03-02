'''Solutions for PROB and RSTR'''

import math

class PROB:
    def __init__(self):
        pass

    def calculate_prob_of_string_in_n_given_gc(self,s,n,gc_content):
        G_or_C_content,A_or_C_content = self.calculate_GorC_and_AorT_prob(gc_content)
        #print(G_or_C_content,A_or_C_content)
        prob_one_string_equal = 1
        for base in s:
            prob_one_string_equal *= G_or_C_content if base in 'GC' else A_or_C_content
            #print(prob_one_string_equal)
        #print(prob_one_string_equal)
        return round((1 - (1-prob_one_string_equal)**n),3)

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
        print(values)
        for value in values:
            gorc,aort = self.calculate_GorC_and_AorT_prob(value)
            results.append(self.calculate_prob_of_string(gorc,aort,s))
        return results

def Main():
    GCs = '0.066 0.110 0.162 0.244 0.286 0.343 0.396 0.431 0.500 0.536 0.614 0.644 0.714 0.738 0.819 0.868 0.914'
    s = 'CGCCTGTGGTGTGATCTGAATCTTAATGGACGCTCCTACTGAGGACGCCCTATTTAAATCGCCCTGCACTTACGCGTTTGCTTTAGATCCAAACGCATCG'
    solver = PROB()
    #print(*solver.calculate_all_probs_of_string_with_log(GCs,s))
    gc = 0.423093
    s = 'TTGGATCCTT'
    n = 92492
    print(solver.calculate_prob_of_string_in_n_given_gc(s,n,gc))

if __name__ == '__main__':
    Main()