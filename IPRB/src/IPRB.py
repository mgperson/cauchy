#Matt Person
#Rosalind Problem: IPRB
#source
'''Given: Three positive integers k, m, and n, representing a population containing k+m+nk+m+n organisms: k
individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing
 a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.'''

class IPRB:
    def __init__(self,k,m,n):
        self.total_prob = self.get_probability_of_dominant_phenotype(k, m, n)
        pass

    def get_probability_of_dominant_phenotype(self, k, m, n):
        total_num = k+m+n

        prob_given_first_k = 1

        prob_given_first_m_dominant = 1
        prob_given_first_m_recessive = k/(total_num-1) + (m-1)/(total_num-1)*1/2
        #print(prob_given_first_m_recessive)

        prob_given_first_m = .5*prob_given_first_m_dominant + .5*prob_given_first_m_recessive
        #print(prob_given_first_m)

        prob_given_first_n = (k + m/2)/(total_num-1)
        #print(prob_given_first_n)

        total_prob = (k*prob_given_first_k + m*prob_given_first_m + n*prob_given_first_n)/total_num
        return total_prob

def Main():
    iprb = IPRB(17,26,25)
    print(iprb.total_prob)

if __name__ == '__main__':
    Main()