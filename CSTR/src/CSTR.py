class CSTR():
    def __init__(self,DNA_strings):
        self.dna_strings = DNA_strings.split('\n')
        self.character_table = []
        self.generate_character_table()
        pass

    def generate_character_table(self):
        for i in range(len(self.dna_strings[0])):
            character_row = self.get_character_row_of_index(i)
            if character_row != '':
                #print(i)
                self.character_table.append(character_row)

    def get_character_row_of_index(self,index):
        char_one = self.dna_strings[0][index]
        char_one_count, char_two_count = 1,0
        char_row = '1'
        for i in range(1,len(self.dna_strings)):
            if self.dna_strings[i][index] == char_one:
                char_one_count += 1
                char_row += '1'
            else:
                char_two_count += 1
                char_row += '0'
        return char_row if char_one_count > 1 and char_two_count > 1 else ''


def Main():
    with open('input') as input_data:
        dna_strings = ''.join([line for line in input_data])
    cstr = CSTR(dna_strings)
    with open('output.txt','w') as output_data:
        [output_data.write(character_row + '\n') for character_row in cstr.character_table]

if __name__ == '__main__':
    Main()