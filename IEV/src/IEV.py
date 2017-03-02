class IEV:
    def __init__(self):
        pass

    def get_expected_number(self,num_couples):
        #hard coding each expected result per parents' genotype
        #expected result is 2 for couples with a homozygous dominant parent (couples 1,2,3)
        # 1.5 for heterozygous both parents, 1 for heterozygous parent A, homozygous recessive,
        # and 0 for homozygous both recessive
        return num_couples[0] * 2 + num_couples[1] * 2 + num_couples[2] * 2 \
            + num_couples[3] * 1.5 + num_couples[4] * 1

def Main():
       iev = IEV()
       sample = list(map(int, '19749 17773 19746 18722 16032 19051'.split()))
       print(iev.get_expected_number(sample))

if __name__ == '__main__':
        Main()