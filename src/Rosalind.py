class Haystack:
    def __init__(self,DNAStrings):
        self.DNAStrings = DNAStrings


    def generate_substrings_of_length_n(self,string,n):
        substrings = [string[i:(i+n)] for i in range(len(string) - n + 1)]
        return substrings

    def generate_all_substrings(self,string):
        substrings = []
        for i in range(len(string),0,-1):
            [substrings.append(j) for j in self.generate_substrings_of_length_n(string,i)]
        return substrings

    def find_substring_in_string(self,string,substring):
        return substring in string

    def solve_for_longest_common_substring(self,DNAStrings):
        longest_substing = ''
        first_string = DNAStrings[0]
        found_in_all = True
        #Generate lengths to check
        #touching
        # for i in range (len(first_string),1,-1):
        #     #Iterate substrings of length i
        #     for substring in self.generate_substrings_of_length_n(first_string,i):
        #         #Check substring in each of remaining strings
        #         is_substring_in_remaining_strings = True
        #         for j in range(1,len(DNAStrings)):
        #             if (not self.find_substring_in_string(DNAStrings[j],substring)):
        #                 is_substring_in_remaining_strings = False
        #                 break
        #         if (is_substring_in_remaining_strings):
        #             return substring
        # return longest_substing
        for substring in self.generate_all_substrings(first_string):
            found_in_all = True
            for i in range(1,len(DNAStrings)):
                if not self.find_substring_in_string(DNAStrings[i],substring):
                    found_in_all = False;
                    break;
            if found_in_all:
                return substring
        return longest_substing

def read_input_file(file):
    values = []
    with open(file) as input_data:
        current_line = ''
        for line in input_data:
            if line[0] == '>':
                if not current_line == '':
                    values.append(current_line)
                current_line = ''
            else:
                current_line += line.rstrip('\n')
        values.append(current_line)
    return values


def main():
    DNAStrings = read_input_file('input/rosalind_lcsm.txt')
    haystack = Haystack(DNAStrings)
    print(Haystack.solve_for_longest_common_substring(haystack,haystack.DNAStrings))

if __name__ == '__main__':
    main()


