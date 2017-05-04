class RNAS:
    def __init__(self):
        self.wobble_matching_num_by_RNA_string = {}

    def get_RNA_complements_with_wobble_pairs(self, base):
        if base == 'U': return ('A', 'G')
        if base == 'A': return ('U')
        if base == 'G': return ('C', 'U')
        if base == 'C': return ('G')

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

def Main():
    rnas = RNAS()
    RNA_string = 'AGGCAUGUAGUAGCAGCGACGCUUAGUUCUGACCUCCCUGUCUAGUCGGCUCUGGAAUUCUCCGUGAAAGUGGUUGUCGUGGACACGGAUGAAUCUUCCUACAUCAGCAACAGCCGGGCGCCCCGUCCUGCCAACUUGUCGCGAAUCUUGAGAGACGGCACGUGGG'
    print (rnas.get_wobble_matching_by_RNA_string(RNA_string))

if __name__ == '__main__':
    Main()