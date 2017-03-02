class IPRB:
    def __init__(self):
        pass

    def get_probability(self,k,m,n):
        total_num = k+m+n

        prob_given_first_k = 1

        prob_given_first_m_dominant = 1
        prob_given_first_m_recessive = k/(total_num-1) + (m-1)/(total_num-1)*1/2
        print(prob_given_first_m_recessive)

        prob_given_first_m = .5*prob_given_first_m_dominant + .5*prob_given_first_m_recessive
        print(prob_given_first_m)

        prob_given_first_n = (k + m/2)/(total_num-1)
        print(prob_given_first_n)

        total_prob = (k*prob_given_first_k + m*prob_given_first_m + n*prob_given_first_n)/total_num
        return total_prob

def Main():
    iprb = IPRB()
    k,m,n = 17,26,25
    print(iprb.get_probability(k,m,n))

if __name__ == '__main__':
    Main()