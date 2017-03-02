class RosalindUtilities():
    def __init__(self):
        self.amino_acid_codes_for_codons = {}
        self.load_amino_acid_codes_for_codons()
        pass

    def load_amino_acid_codes_for_codons(self):
        values = [('UUU', 'F'), ('UUC', 'F'),('UUA', 'L'), ('UUG', 'L'),
                  ('UCU', 'S'), ('UCC', 'S'), ('UCA', 'S'), ('UCG', 'S'),
                  ('UAU', 'Y'), ('UAC', 'Y'), ('UAA', 'Stop'), ('UAG', 'Stop'),
                  ('UGU', 'C'), ('UGC', 'C'), ('UGA', 'Stop'), ('UGG', 'W'),

                  ('CUU', 'L'), ('CUC', 'L'), ('CUA', 'L'), ('CUG', 'L'),
                  ('CCU', 'P'), ('CCC', 'P'), ('CCA', 'P'), ('CCG', 'P'),
                  ('CAU', 'H'), ('CAC', 'H'), ('CAA', 'Q'), ('CAG', 'Q'),
                  ('CGU', 'R'), ('CGC', 'R'), ('CGA', 'R'), ('CGG', 'R'),

                  ('AUU', 'I'), ('AUC', 'I'), ('AUA', 'I'), ('AUG', 'M'),
                  ('ACU', 'T'), ('ACC', 'T'), ('ACA', 'T'), ('ACG', 'T'),
                  ('AAU', 'N'), ('AAC', 'N'), ('AAA', 'K'), ('AAG', 'K'),
                  ('AGU', 'S'), ('AGC', 'S'), ('AGA', 'R'), ('AGG', 'R'),

                  ('GUU', 'V'), ('GUC', 'V'), ('GUA', 'V'), ('GUG', 'V'),
                  ('GCU', 'A'), ('GCC', 'A'), ('GCA', 'A'), ('GCG', 'A'),
                  ('GAU', 'D'), ('GAC', 'D'), ('GAA', 'E'), ('GAG', 'E'),
                  ('GGU', 'G'), ('GGC', 'G'), ('GGA', 'G'), ('GGG', 'G')]

        for val in values:
            self.amino_acid_codes_for_codons[val[0]] = val[1]

    def get_amino_acid_code_for_codon(self,codon):
        return self.amino_acid_codes_for_codons.get(codon)

    def read_input_file(file):
        values = []
        with open(file) as input_data:
            current_line = ''
            for line in input_data:
                if line[0] == '>':
                    label = line[1:]
                    if not current_line == '':
                        values.append((label,current_line))
                    current_line = ''
                else:
                    current_line += line.rstrip('\n')
            values.append(current_line)
        return values