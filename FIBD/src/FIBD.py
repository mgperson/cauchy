#Matt Person
#Rosalind Problem: FIBD
#source
'''Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.'''

class FIBD:
    def __init__(self,n,m):
        self.number_of_pairs = self.get_fibd_of_n_m(n,m)

    def get_fibd_of_n_m(self,n,m):
        if m == 0 or n == 0:
            return 0
        pairs_of_rabbits_by_age = {}
        pairs_of_rabbits_by_age[0] = 1
        for i in range(n-1):
            #get duplicate rabbits (age 1 greater)
            to_duplicate = 0
            for j in range(1,m):
                to_duplicate += pairs_of_rabbits_by_age.get(j,0)
            #age rabbits and kill aged m
            prev_mon_count = pairs_of_rabbits_by_age[0]
            for j in range(1,m):
                temp = pairs_of_rabbits_by_age.get(j,0)
                pairs_of_rabbits_by_age[j] = prev_mon_count
                prev_mon_count = temp
            #set duplicated rabbit number
            pairs_of_rabbits_by_age[0] = to_duplicate
        return sum(pairs_of_rabbits_by_age.values())

def Main():
    n, m = 98, 20
    fibd = FIBD(n,m)
    print(fibd.number_of_pairs)

if __name__ == '__main__':
    Main()

