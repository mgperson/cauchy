import sys
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')
from RUtils.src.RosalindUtilities import RosalindUtilities

class FINALROUND3:
    def __init__(self,file):
        self.ru = RosalindUtilities()
        with open(file) as input_file:
            for line in input_file:
                self.DNA = line
        #print(self.DNA)

    def get_protein(self,DNA):
        return [self.ru.get_aa_from_DNA_codon(DNA[i*3:i*3+3]) for i in range(len(DNA) //3)]

    def get_None_count_of_protein(self,protein):
        return sum([1 for aa in protein if aa == None])

    def get_aa_count_of_protein(self,protein):
        return sum([1 for aa in protein if aa != None])

    def get_maximum_num_aa(self):
        best_aa = 0
        best_i,best_j = 0,len(self.DNA)-1
        best_none_count = 30000
        start_protein = self.get_protein(self.DNA)
        print(len(start_protein))
        print(len(self.DNA))
        print(''.join(start_protein))
        #first_None = start_protein.index(None)
        #i = first_None
        #codon = self.DNA[i:i+80]
        #print(codon)
        #find first time next codon is not junk
        # j = i
        # while(self.ru.get_aa_from_DNA_codon(self.DNA[j:j+3]) == None):
        #     codon = self.DNA[j:j+3]
        #     print(codon)
        #     j += 1
        # print(j)
        # for j in range(i*3,len(self.DNA)):
        #     count = self.get_None_count_of_protein(self.get_protein(self.DNA[j:]))
        #     if count < best_none_count:
        #         best_none_count = count
        #     if j%100 == 0:
        #         print(j,best_none_count)

    # naive
    # def get_maximum_num_aa(self):
    #     best_aa = 0
    #     best_i,best_j = 0,len(self.DNA)-1
    #     for i in range(len(self.DNA)):
    #         for j in range(i+1,len(self.DNA)):
    #             test = self.DNA[:i] + self.DNA[j:]
    #             count = self.get_aa_count_of_protein(self.get_protein(test))
    #             if count > best_aa:
    #                 #print(count)
    #                 best_aa = count
    #                 best_i = i
    #                 best_j = j
    #             #print(test)
    #             #print(self.get_None_count_of_protein(self.get_protein(test)))
    #             if j%100 == 0:
    #                 print (j)
    #         if i%10 == 0:
    #             print(i)
    #     print(best_aa)
    #     print(best_i,best_j)


def Main():
    solver = FINALROUND3('Test_1')
    #test = solver.DNA[:8] + solver.DNA[32114:]
    #print(test)
    #print(solver.get_aa_count_of_protein(solver.get_protein(test)))
    solver.get_maximum_num_aa()

if __name__ == '__main__':
    Main()