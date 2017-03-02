class REVP:
    #TODO pass in test case, add instance variable of complement
    def __init__(self,input):
        self.input = input
        self.input_complement = self.get_complement_of_string(input)
        pass

    def get_all_intervals_of_length_m_of_string_of_length_n(self,m,n):
        return [(i,n) for i in range(n-m+1)]

    def get_all_subsequences_of_length_n(self,input,n):
        return [input[i:i+n] for i in range(len(input)-n+1)]

    def get_reverse_of_sequence(self,input):
        return input[::-1]

    def get_complement_of_letter(self,letter):
        if letter == 'C':
            return 'G'
        if letter == 'G':
            return 'C'
        if letter == 'A':
            return 'T'
        if letter == 'T':
            return 'A'
        pass

    def get_complement_of_string(self,input):
        result = "".join([self.get_complement_of_letter(letter) for letter in input])
        return result

    def is_reverse_palindrome(self,input):
        return self.get_complement_of_string(input) == self.get_reverse_of_sequence(input)

    def get_reverse_palindromes_of_length_n(self,input,n):
        subsequences = self.get_all_subsequences_of_length_n(input,n)
        return [(i+1,n) for i in range(len(subsequences))if self.is_reverse_palindrome(subsequences[i])]

    def get_reverse_palindromes_of_length_4_to_12(self,input):
        return [item for n in range(4,13) for item in self.get_reverse_palindromes_of_length_n(input,n)]

    #[item for sublist in l for item in sublist]

    #TODO: Use intervals to get complement from preprocessed complement instead of each time

def Main():
    input = 'CGCGGCTTCCGGGGCTGTTTTTAAAATATGGGTTTTGTCCTAGTTCCAGCCTGATAGGTAGAACCGCAAGGAGCTAGTACCACCCGGAGTCGGACTCACGTCCCTACATCACTATTAGGTACTAGCCTTTGGTATTGTGCTCGGGCAACTTAGACCGTCTATCAGGGATATAGGGTATTATGCCGCCCGATGGAAAAGCAAGATTCGTACAATCACCTTAAGATTGTGTCCGGGGCTCGCGACCCAGCAAGAAGGCGGGATCTTACCGTTTAACCGCATAGGAGAGACTTGACGTGGATTCGCTGTCTTACCTCAGGGCCGCTGTGGCCGCGGTTGAAAAGCCCAGTTACATATTCGGAGCAGATGTGATGGACAATCACTCACTCGTATAAGCTGCACCACCCCAATTACGCACTCATGCTATCTATCACCTTGAAGTTTACGTCTTATTGAACGTGGACCTCAGACACCTTGACACGCGCGCGTGTGGCCCACTACCAAGGACTCAGTAAATTACCACAGACGCACATGTAAAAAACGTGATTAGCCACTCACTGGCGTGAGCAGATTGTTCAATGTTCACAATCTCTTCGGACTGGGTTCGAAACGACCGTCTCGTGTGCGAAGAGCAATCGTGTGTCTGAGGTACGGCGCGTAAAATACAGAGGCAACCATTCCCCGAGTAAAAAACATGGATTTATTCCACCGGCTCTCATTGATATGCTGACTAGGAGGGAAGCCGCGGTTCCAGTATGGCGTTCTGTTGCCTCCGTAGACCGTTGGTATCTCAGACAGGAAAATGTACTGCATTCGCTGAACCTCGTTTCCGCATTGCTAGTAGTGCGTAAAGACTCATCAATTGCAAGGTCAACTGCAAAATGAGATTAAACAAGTACCTGGTCGGCATAGTAGTATCGAGATTTTGCAAAGAGAGACCAGCCTTTGTTCGAAGACATGCTATA'
    revp = REVP(input)
    print(*revp.get_reverse_palindromes_of_length_4_to_12(input))

if __name__ == '__main__':
    Main()