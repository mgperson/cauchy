from itertools import combinations
from itertools import product

class QRT:
    def __init__(self,taxa_input,table_input):
        self.taxa = taxa_input.split()
        self.table = table_input.split('\n')
        self.quartet_hashes = set()
        self.quartets = []
        self.generate_all_quartets()

    def get_indices_of_characters_and_not_characters_in_split(self,split):
        character_indices = []
        not_character_indices = []
        for i in range(len(split)):
            if split[i] == '1':
                character_indices.append(i)
            elif split[i] == '0':
                not_character_indices.append(i)
        return (character_indices,not_character_indices)

    def generate_quartets_of_split(self, split):
        results = []
        indices = self.get_indices_of_characters_and_not_characters_in_split(split)
        character_indices, not_character_indices = indices[0],indices[1]
        character_duplet_combinations = combinations(character_indices,2)
        not_character_duplet_combinations = combinations(not_character_indices, 2)
        return list(product(character_duplet_combinations,not_character_duplet_combinations))

    def generate_all_quartets(self):
        for split in self.table:
            quartets = self.generate_quartets_of_split(split)
            for quartet in quartets:
                self.quartet_hashes.add(self.generate_numeric_quartet_hash(quartet))
            #self.quartets += ['{' + self.taxa[quartet[0][0]] + ', ' + self.taxa[quartet[0][1]] +'} {' + self.taxa[quartet[1][0]] + ', ' + self.taxa[quartet[1][1]] +'}' for quartet in quartets]
        for hash in self.quartet_hashes:
            indices = hash.split(':')
            self.quartets.append('{' + self.taxa[int(indices[0])] + ', ' + self.taxa[int(indices[1])] + '} {' + self.taxa[int(indices[2])] + ', ' + self.taxa[int(indices[3])] + '}')
        #self.quartets += ['{' + self.taxa[int(hash[0])] + ', ' + self.taxa[int(hash[1])] + '} {' + self.taxa[int(hash[2])] + ', ' + self.taxa[int(hash[3])] + '}' for hash in self.quartet_hashes]

    def generate_numeric_quartet_hash(self,quartet):
        first_duplet, second_duplet = sorted(quartet[0]), sorted(quartet[1])
        first_val = ':'.join([str(i) for i in first_duplet])
        second_val = ':'.join([str(j) for j in second_duplet])
        if first_val < second_val:
            return first_val+ ':' + second_val
        else:
            return second_val+ ':' + first_val

def Main():
    taxa_input = 'cat dog elephant ostrich mouse rabbit robot'
    table_input = '''01xxx00
x11xx00
111x00x'''
    taxa_input = 'Acanthoscurria_cioides Allobates_similis Ardea_macrops Bradypodion_grunniens Chlamydotis_nelsonii Ethmostigmus_salamandra Gallinago_leporosum Gypaetus_carinata Holaspis_subcinctus Lampropeltis_subglobosa Nyctixalus_stagnalis Nyroca_monedula Opheodrys_fimbriatus Ophisops_mysticetus Oxyura_medici Phoca_bimaculata Pterocles_rufus Ptyodactylus_valliceps Rangifer_nigrolineatus Trapelus_mexicana'
    table_input = '''1x10x1xxxxx0111x1xx1
xx1xxxxxx0xx1x1xxx1x
1xx1x11xx1x1x001111x
x0xxx1xxxxx1xxxx1xx1
xxxxxxxxxx100xxxxxxx
xxxxxx01xxx10xxxx1x1
00000xxx0xx0x1100xxx
xxx0x11x00xxx11101xx
xxx0xxxx0xxx1110x000
x1111x1x000x111101x0
0x11000x1x11000x10x1
0001000011x1xxx11xxx
11111111x11111111x10
0x000xx100x01x1000x0
x01x00x0x11xxx0xx0xx
x0010000000100000010
00x0x00x00x00110x0xx'''
    qrt = QRT(taxa_input, table_input)
    print(qrt.quartets)
    with open('output.txt','w') as output_file:
        #[ouput_file.write(quartet) for quartet in qrt.quartets]
        for quartet in qrt.quartets:
            output_file.write(quartet)
            output_file.write('\n')
        #[output_file.write(quartet + '\n') for quartet in qrt.quartet_hashes]

if __name__ == '__main__':
    Main()