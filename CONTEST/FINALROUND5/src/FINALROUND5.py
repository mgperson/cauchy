import sys
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\CONTEST\\FINALROUND5\\SRC')

class FINALROUND5:
    def __init__(self,chemicals_file,proteins_file):
        self.reactions = []
        self.proteins = []
        self.proteins_by_reaction_activated = {}
        self.all_chemicals = set()
        reaction_index = 0
        with open(chemicals_file) as input_data:
            for line in input_data:
                line = line.strip('\n')
                left_side,right_side = line.split(' <=> ')
                left_chems = left_side.split(' + ')
                right_chems = right_side.split(' + ')
                self.all_chemicals.update(left_chems)
                self.all_chemicals.update(right_chems)
                self.reactions.append(((left_chems),(right_chems)))
                #self.reactions.append(((right_chems.split(' + ')), (left_chems.split(' + '))))
                reaction_index += 1
       # print(self.reactions)
        with open(proteins_file) as input_data:
            for line in input_data:
                line = line.strip('\n')
                self.proteins = line.split()
        #print(self.proteins)

    def print_all_proteins(self):
        print(*self.proteins)

    def get_new_chemicals(self,start_chems,avail_chems):
        new_chems = set(avail_chems.split()).symmetric_difference(set(start_chems.split()))
        return new_chems

    def get_reactions_that_happened(self,start_chemicals,avail_chems):
        start_chemicals = start_chemicals.split()
        avail_chems = avail_chems.split()
        return[i for i in range(len(self.reactions)) if self.did_reaction_happen(i,start_chemicals,avail_chems) == 'YES']

    def did_reaction_happen(self,reaction_num,start_chems,avail_chems):
        reaction = self.reactions[reaction_num]
        reaction_chems = set(reaction[0] + reaction[1])
        #print(reaction_chems,avail_chems)
        if not reaction_chems.issubset(avail_chems):
            return 'NO'
        if not reaction_chems.issubset(start_chems):
            return 'YES'
        return 'MAYBE'

    def generate_get_all_possible_reactions(self):
        print(*self.all_chemicals)
        print(*self.proteins)

    def generate_get_chemicals_right_side_all_proteins(self):
        print(*set([chem for reaction in self.reactions for chem in reaction[1]]))
        print(*self.proteins)

    def generate_get_chemicals_left_side_all_proteins(self):
        print(*set([chem for reaction in self.reactions for chem in reaction[0]]))
        print(*self.proteins)

    def generate_individual_proteins_for_start_list(self,start_list):
        for protein in self.proteins:
            print(start_list)
            print (protein)

    def generate_start_list(self,first_reaction_num):
        start_chemicals = set()
        reaction = self.reactions[first_reaction_num]

    def generate_experiments(self,start_list):
        print('?')
        self.generate_individual_proteins_for_start_list(start_list)
        #self.generate_get_all_possible_reactions()
        #self.generate_get_chemicals_left_side_all_proteins()
        #self.generate_get_chemicals_right_side_all_proteins()

    def get_reactions_that_happened_for_multi_lines(self,start_chems,multi_lines):
        for i in range(len(multi_lines)):
            line = multi_lines[i]
            #print(self.proteins[i])
            for reaction in self.get_reactions_that_happened(start_chems, line):
                #print(reaction)
                self.proteins_by_reaction_activated[reaction] = self.proteins_by_reaction_activated.get(reaction,[]) + [self.proteins[i]]
            #print(self.get_reactions_that_happened(start_chems,line))
        for i in range(len(self.reactions)):
            print(i+1)
            if i in self.proteins_by_reaction_activated.keys():
                print (*self.proteins_by_reaction_activated[i])
            else:
                print('-')



def Main():
    solver = FINALROUND5('6','6.proteins')
    #print(solver.get_reactions_that_happened('c8 c4 c10 c14 c9 c2 c6 c1 c18 c15 c5','c7 c2 c17 c14 c3 c11 c12 c8 c5 c10 c9 c15 c4 c1 c16 c13 c6 c18'))
    #print(solver.get_reactions_that_happened('c13 c8 c3 c4 c14 c11 c7 c6 c16 c17 c12 c5','c13 c8 c3 c4 c14 c11 c7 c6 c16 c17 c12 c5'))
    lines = '''c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c42 c35 c9 c163 c142 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c12 c13 c35 c9 c163 c11 c10 c165
c162 c7 c8 c6 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c6 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c12 c13 c35 c9 c163 c11 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c164 c135 c35 c9 c163 c166 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c164 c135 c35 c9 c163 c166 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c6 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165
c162 c7 c8 c35 c9 c163 c10 c165'''.split('\n')
    start_chem ='c7 c8 c9 c10 c162 c163 c165 c35'
    #solver.generate_experiments(start_chem)
    solver.get_reactions_that_happened_for_multi_lines(start_chem,lines)
    #print(solver.proteins[12])


if __name__ == '__main__':
    Main()
