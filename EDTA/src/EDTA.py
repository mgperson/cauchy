import os
import sys,difflib
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from EDIT.src.EDIT import EDIT

class EDTA:
    def __init__(self,s,t):
        self.s = s
        self.t = t
        self.s_prime = ''
        self.t_prime = ''
        self.len_s = len(s)
        self.len_t = len(t)
        self.alignment_score_matrix = {}
        self.next_direction_matrix = {}
        self.create_alignment_score_matrix()
        #self.print_matrix()
        #print(self.next_direction_matrix)
        self.find_optimal_alignment()
        #print(self.s_prime)
        #print(self.t_prime)
        pass

    def print_matrix(self):
        for i in range(self.len_s+1):
            print(*[self.get_matrix_value(i,j) for j in range(self.len_t+1)])

    def find_optimal_alignment(self):
        #self.optimal_alignment_length = self.get_matrix_value(self.len_s,self.len_t) * -1
        i,j = self.len_s,self.len_t
        while (i != 0 or j != 0):
            key = str(i) + ':' + str(j)
            next_direction = self.next_direction_matrix[key]
            #print(next_direction)
            #print(self.s_prime, self.t_prime)
            #print(self.s, self.t)
            #print(i, j)
            if next_direction == 'up':
                self.s_prime += self.s[i-1]
                self.t_prime += '-'
                i -= 1
            elif next_direction == 'left':
                self.s_prime += '-'
                self.t_prime += self.t[j-1]
                j -= 1
            else :
                self.s_prime += self.s[i-1]
                self.t_prime += self.t[j-1]
                i -= 1
                j -= 1
        self.s_prime = self.s_prime[::-1]
        self.t_prime = self.t_prime[::-1]
        edit = EDIT(self.s_prime,self.t_prime)
        self.optimal_alignment_length = edit.answer

    def find_next_direction(self,i,j,match_score):
        direction_up_score = self.get_matrix_value(i -1,j) - 1
        direction_left_score = self.get_matrix_value(i, j-1) - 1
        direction_upleft_score = self.get_matrix_value(i-1, j - 1) + match_score
        if direction_up_score > direction_left_score and direction_up_score > direction_upleft_score:
            return 'up'
        elif direction_left_score > direction_upleft_score:
            return 'left'
        else:
            return 'upleft'


    def create_alignment_score_matrix(self):
        self.initialize_matrix()
        self.process_matrix()
        pass

    def initialize_matrix(self):
        self.alignment_score_matrix['0:0'] = 0
        for i in range(1,self.len_s+1):
            self.alignment_score_matrix[str(i)+':0'] = -i
            #self.alignment_score_matrix[str(i) + ':' + str(self.len_t + 1)] = -100000
        for j in range(1,self.len_t+1):
            self.alignment_score_matrix['0'+':'+str(j)] = -j
            self.next_direction_matrix[str(self.len_s) + ':' + str(j)] = 'right'

        #print(self.alignment_score_matrix)

    def get_matrix_value(self,i,j):
        key = str(i)+':'+str(j)
        if key not in self.alignment_score_matrix.keys():
            return -10000
        return self.alignment_score_matrix[key]

    def process_matrix(self):
        for i in range(1,self.len_s+1):
            for j in range(1,self.len_t+1):
                match_score = 1 if self.s[i-1] == self.t[j-1] else -1
                next_direction = self.find_next_direction(i,j,match_score)
                if next_direction == 'up':
                    self.next_direction_matrix[str(i)+':'+str(j)] = 'up'
                    self.alignment_score_matrix[str(i) + ':' + str(j)] = self.get_matrix_value(i-1,j) - 1
                elif next_direction == 'left':
                    self.next_direction_matrix[str(i) + ':' + str(j)] = 'left'
                    self.alignment_score_matrix[str(i) + ':' + str(j)] = self.get_matrix_value(i, j-1) - 1
                elif next_direction == 'upleft':
                    self.next_direction_matrix[str(i) + ':' + str(j)] = 'upleft'
                    self.alignment_score_matrix[str(i) + ':' + str(j)] = self.get_matrix_value(i - 1, j - 1) + match_score

def Main():
    #s = 'PRETTY'
    #t = 'PRTTEIN'
    s = 'ALICDNDMHLGCGNMEMVQNQDLSKYPAHESLTVQQIETQESTLKLWWSRWRFLYFIFCQEKIELLFSLKLPDFVNWKIWLNCQDRLHILGSPWNMTTNNGPSQPMTLCDHACGKHVWFMPEDWQDNAGEVLYIDRYDKIKNTDPPQHMDHQSEYHPEPARAATDATNMAMDRWQQMHMYVVTWLILPANIIPAAIRQAMDRDREARWNQHCYCKECNPKIWATVTKPRIMFWPGWGILKVDMADRLMEPYGDPTNNEHYNPHLCKRYYPHVFQDTGVNFNPPMVLCTKNSTGVPVHHGMTIQPTRCPPKHEDKEERAMDKVFRVHIRSWHCCYNWFQDCQNGECAYWKYQLKYGCQACMKTNYMDLSHCMKHCEWNMHNWYDDITSIALSKCEQQKIMEVVFGTDDNPCTDRFDCFHTHPVICDKWQMTLEIRSTVQAFKNWPSKYRMYPWGSDQGECCIYFMVNNFVGRERQQANSKKWDMGSSSVTVFLNHFEIGVNVQSTVVSWLQYMNHESYESYMFDSNHPVNFMPEVWLDDMLVWDWECRKHIGQEVFDWWEPYFNPRRHVTMWIYCVRWRRYWDTEAEMTWMQFWAVCNNYAFHCDRPNCRMSARFADKWKPGVLWMIVGDYRHVGKEDIFPQNDFMMRDKDWPNKSLKERDATMNSIFFITLWILHSRNFNIVYTYDITWIGYLEKMQDAPRNGKVNRVIVTHTRHAHCCFELMWQCIYFHEWFQYDPLMQHQNDVWNWHPWYPMSNYEYFCGDFCPATRDKYCDWAFANLVDRMQDQQEETLWHARFFSWLGCYI'
    t = 'ALIHLGCGNMEMVQMQDLSKYPTQESTLELWWYFIFYQEKIELLFSLHIQRCKITKEIWLNCQARHPLGSPEIPSGNFPQTPTLCDHACGKHVWGRVLYIDRYKGRASKEIKKLLHETDPPQHRETDPTCFHQSEYHPEPSRADATNRWQCYHFAEVDIIPAAIRQAMDRDRSARWNQHCYCKECNPKIWATVTKPRDHCHTGILKRDMTPYDDPTNNEHYNPRYMPHVFQDTGVNFNPPMVLLTKNSTGFTVRGHGMTIKHEDKRTDNMEGYERAMSWHCCEGEFHDKYFQQNGECHYWKYQLVLGCACMKTNYMDLSHCMKHCEWNVHNWYNDITSIALSKCEQQVIMEVNPQTDRFDCFHTHPVICDKLTPDLEVQMFKNWDSRYRMYPWGSDQGECCIAHFMVNYFCGRERQQANSKKWDMGLSSVTVFLNHPEIGVSTVVSWHDAGESYMVVNFMLEDWLDIMLVWDQTRNHECKHDEQEVFDWWEPYQNPREHVTMWIYCVRWRRYWDTEAEMTKMQVHNIPRNNRPNCRKWKPDYLWNRIVGDRHVGTDTYVGDWPNKATMNSIFFITLWILHSRNFNIVYTYDITWIGYLEKMSQYCCPHFDAPRNCKVNRDIVYHTRHAHCCFGLMWQCFHEWFQYDPLMQHQLEVMADVWNWHPWYPMSYYCYFCGDIACPATRDTYCDWAFCLFGTPKDQDQLEEFSWLHCYI'
    edta = EDTA(s,t)
    print(edta.optimal_alignment_length)
    print(edta.s_prime)
    print(edta.t_prime)

if __name__ == '__main__':
    Main()




