#Contains solutions for CAT and MOTZ (Catalan and Motzkin numbers)

class CAT:
    def __init__(self):
        self.combinations_by_n = {}
        self.combinations_by_RNA_string = {}
        self.motzkin_num_by_RNA_string = {}
        self.wobble_matching_num_by_RNA_string = {}
        pass

    def get_RNA_complement(self,base):
        if base == 'U': return 'A'
        if base == 'A': return 'U'
        if base == 'G': return 'C'
        if base == 'C': return 'G'

    def get_RNA_complements_with_wobble_pairs(self, base):
        if base == 'U': return ('A','G')
        if base == 'A': return ('U')
        if base == 'G': return ('C','A')
        if base == 'C': return ('G')

    def find_occurences(self, s, ch):
        return [i for i, letter in enumerate(s) if letter == ch]

    def find_occurences_with_wobble_pairs(self,s,ch_tuple):
        return [i for i, letter in enumerate(s) if letter in ch_tuple and i >= 4]

    def get_wobble_matching_by_RNA_string(self,RNA_string):
        if RNA_string in self.wobble_matching_num_by_RNA_string:
            return self.wobble_matching_num_by_RNA_string[RNA_string]

        if len(RNA_string) == 0:
            return 1

        first_base = RNA_string[0]
        comp_bases = self.get_RNA_complements_with_wobble_pairs(first_base)
        comp_base_indices = self.find_occurences_with_wobble_pairs(RNA_string,comp_bases)

        #wobble number NOT matching first base
        wobble_matching_num = self.get_wobble_matching_by_RNA_string(RNA_string[1:])

        #wobble number WITH matching first base
        for i in comp_base_indices:
            wobble_matching_num +=  self.get_wobble_matching_by_RNA_string(RNA_string[1:i]) * self.get_wobble_matching_by_RNA_string(RNA_string[i+1:])

        self.wobble_matching_num_by_RNA_string[RNA_string] = wobble_matching_num
        return wobble_matching_num

    def get_motzkin_by_RNA_string(self,RNA_string):
        if RNA_string in self.motzkin_num_by_RNA_string:
            return self.motzkin_num_by_RNA_string[RNA_string]

        if len(RNA_string) == 0:
            return 1
        # Always one possibility, the empty set

        first_base = RNA_string[0]
        comp_base = self.get_RNA_complement(first_base)
        comp_base_indeces = self.find_occurences(RNA_string, comp_base)

        # motzkin number NOT matching the first base
        motzkin_num = self.get_motzkin_by_RNA_string(RNA_string[1:])

        #motzkin number WITH matching first base
        for i in comp_base_indeces:
            motzkin_num += self.get_motzkin_by_RNA_string(RNA_string[1:i]) * self.get_motzkin_by_RNA_string(RNA_string[i+1:])

        self.motzkin_num_by_RNA_string[RNA_string] = motzkin_num
        return motzkin_num

    def get_catalan_by_RNA_string(self,RNA_string):
        if RNA_string in self.combinations_by_RNA_string:
            return self.combinations_by_RNA_string[RNA_string]

        if len(RNA_string) == 0:
            return 1

        first_base = RNA_string[0]
        comp_base = self.get_RNA_complement(first_base)
        comp_base_indeces = self.find_occurences(RNA_string, comp_base)
        len_comp_base_indeces = len(comp_base_indeces)

        if len_comp_base_indeces == 0:
            return len_comp_base_indeces

        catalan_num = 0
        for i in comp_base_indeces:
            catalan_num += self.get_catalan_by_RNA_string(RNA_string[1:i]) * self.get_catalan_by_RNA_string(RNA_string[i+1:])
        self.combinations_by_RNA_string[RNA_string] = catalan_num
        return catalan_num


    def get_catalan_by_n(self,n):
        if n == 0:
            return 1
        if n in self.combinations_by_n:
            return self.combinations_by_n[n]
        catalan_n = 0
        for k in range(1,n+1):
            catalan_n += self.get_catalan_by_n(k-1) * self.get_catalan_by_n(n-k)
        self.combinations_by_n[n] = catalan_n
        return catalan_n

def Main():
    solver = CAT()
    #RNA_string = 'GAAUAUAAUUUAUCGGCCGCAUGAUGCCUAGAAUUAUGCAGCGCUAGAUUACUAUGCGUAGCGCAUAUCGCAUCUUCAGCCGUGAUCGAUGCCUGCAGAAUUCGCGUUAACGCUAGGCGCAGGUACGCGCGGCUACCUUGCGCAUAAUAUGCACUAAUGUAUAUAUCCAUGGAUGCAGUACACUAGACGUCGCUGCCUAUAGCGCAUGUUUGCAAGCGCGCCGAAGUACGCAUGGCGUAGAUCCUA'
    RNA_string = 'UACCUGGAGGGCUUUUUUGUACUCGGGCCUUCCAUCGAUUCACUGACGCUGGACGCACUGUCAAUUCCAAUCAAUUUCUCCAACGGCAAUUAAACCGUCAAGGACUGGAUUUGAGGCGGGAUUGCGACUAACGUGGCCAAAUGAAUGUUCGAGUUAUCGUAUAUGCGCAUUGUCCGGAUCUAUGUCUUCCGAAUUACCGUGUACAUACGAUCACUUGAAAGGGUCUAGAGAAAUUCUAAAGGGACAUUUAUAUCUCCUAUCGCCGUCGAUUUGGUAGCACCCGAAGAAUU'
    print(solver.get_motzkin_by_RNA_string(RNA_string) % 1000000)
    print(solver.get_catalan_by_RNA_string(RNA_string) % 1000000)

if __name__ == '__main__':
    Main()


