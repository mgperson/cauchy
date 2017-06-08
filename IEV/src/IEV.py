#Matt Person
#Rosalind Problem: IEV
#source
'''Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.'''

class IEV:
    def __init__(self,nums_of_couples):
        self.expected_number = self.get_expected_number(nums_of_couples)

    def get_expected_number(self,num_couples):
        #hard coding each expected result per parents' genotype
        #expected result is 2 for couples with a homozygous dominant parent (couples 1,2,3)
        # 1.5 for heterozygous both parents, 1 for heterozygous parent A, homozygous recessive,
        # and 0 for homozygous both recessive
        return num_couples[0] * 2 + num_couples[1] * 2 + num_couples[2] * 2 \
            + num_couples[3] * 1.5 + num_couples[4] * 1

def Main():
    sample = list(map(int, '19749 17773 19746 18722 16032 19051'.split()))
    iev = IEV(sample)
    print(iev.expected_number)

if __name__ == '__main__':
        Main()