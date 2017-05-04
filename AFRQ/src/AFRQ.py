class AFRQ():
    def __init__(self):
        pass

    def get_at_least_one_recessive_freq(self,homozygous_rec_freq):
        q = homozygous_rec_freq ** 0.5
        p = 1 - q
        return q**2 + 2*p*q

    def get_at_least_one_recessive_freq_of_values(self,values):
        return [round(self.get_at_least_one_recessive_freq(value),3) for value in values]

def Main():
    #input = '0.1 0.25 0.5'
    input  = '0.278622329386 0.546602440065 0.608565429401 0.296186413903 0.354740098226 0.83221658651 0.648421842659 0.0675824812609 0.768385184064 0.590849051207 0.848900422654 0.575994982088 0.625986457566 0.477141031231 0.216532600264 0.278942362665 0.0980336355867 0.549483635221'
    values = map(float,input.split())
    afrq = AFRQ()
    print(*afrq.get_at_least_one_recessive_freq_of_values(values))

if __name__ == '__main__':
    Main()