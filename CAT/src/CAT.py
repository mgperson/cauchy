class CAT:
    def __init__(self):
        self.combinations_by_n = {}
        self.combinations_by_RNA_string = {}
        pass

    def get_RNA_complement(self,base):
        if base == 'U': return 'A'
        if base == 'A': return 'U'
        if base == 'G': return 'C'
        if base == 'C': return 'G'

    def find_ccurences(self,s,ch):
        return [i for i, letter in enumerate(s) if letter == ch]

    def get_catalan_by_RNA_string(self,RNA_string):
        if RNA_string in self.combinations_by_RNA_string:
            return self.combinations_by_RNA_string[RNA_string]

        if len(RNA_string) == 0:
            return 1

        first_base = RNA_string[0]
        comp_base = self.get_RNA_complement(first_base)
        comp_base_indeces = self.find_ccurences(RNA_string,comp_base)
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
    RNA_string = 'GAAUAUAAUUUAUCGGCCGCAUGAUGCCUAGAAUUAUGCAGCGCUAGAUUACUAUGCGUAGCGCAUAUCGCAUCUUCAGCCGUGAUCGAUGCCUGCAGAAUUCGCGUUAACGCUAGGCGCAGGUACGCGCGGCUACCUUGCGCAUAAUAUGCACUAAUGUAUAUAUCCAUGGAUGCAGUACACUAGACGUCGCUGCCUAUAGCGCAUGUUUGCAAGCGCGCCGAAGUACGCAUGGCGUAGAUCCUA'
    print(solver.get_catalan_by_RNA_string(RNA_string) % 1000000)

if __name__ == '__main__':
    Main()


