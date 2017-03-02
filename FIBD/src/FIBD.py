class FIBD:
    def __init__(self):
        pass

    def get_fibd_of_n_m(self,n,m):
        if m == 0 or n == 0:
            return 0
        rabbits_by_age = {}
        rabbits_by_age[0] = 1
        for i in range(n-1):
            #get duplicate rabbits (age 1 greater)
            to_duplicate = 0
            for j in range(1,m):
                to_duplicate += rabbits_by_age.get(j,0)
            #age rabbits and kill aged m
            prev_mon_count = rabbits_by_age[0]
            for j in range(1,m):
                temp = rabbits_by_age.get(j,0)
                rabbits_by_age[j] = prev_mon_count
                prev_mon_count = temp
            #set duplicated rabbit number
            rabbits_by_age[0] = to_duplicate
            print(rabbits_by_age)
        return sum(rabbits_by_age.values())

def Main():
    fibd = FIBD()
    n,m = 98,20
    print(fibd.get_fibd_of_n_m(n,m))

if __name__ == '__main__':
    Main()

