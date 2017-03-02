import itertools

#also including lexf because it's short and sweet, and sign for same reason
class TRAN:
    def __init__(self):
        pass

    def get_signed_permutations_of_n(self,n):
        # nums = [i for i in range(-n,0)] + [i for i in range(1,n+1)]
        # results = []
        # for i in list(itertools.permutations(nums,r=n)):
        #     results.append(' '.join([str(j) for j in i]))
        permutations = []
        self.get_signed_permutations(list(range(1,n+1)),'',permutations)
        return permutations

    def get_signed_permutations(self,nums,permutation,permutations):
        #print(nums)
        if len(nums) == 0:
            permutations.append(permutation)
            return
        #for i in range(len(nums)):
        for num in nums:
            nums.remove(num)
            self.get_signed_permutations(nums,permutation + (' ' if permutation != '' else '') + str(num),permutations)
            self.get_signed_permutations(nums, permutation + (' ' if permutation != '' else '') + str(-num), permutations)
            nums.insert(0,num)
        return permutations


    def get_lexicographical_order_of_alphabet(self,a,n):
        results = []
        for iter in itertools.product(sorted(a),repeat=n):
            result = ''
            for letter in iter:
                result += letter
            results.append(result)
        return results

    def get_mutation_type(self,a,b):
        if a == b:
            return 'none'
        if ((a == 'G' or a =='A') and (b == 'C' or b == 'T')) or \
                ((b == 'G' or b == 'A') and (a == 'C' or a =='T')):
            return 'transversion'
        return 'transition'

    def get_transition_transversion_ratio(self,a,b):
        transitions,transversions = 0,0
        for i in range(len(a)):
            mutation_type = self.get_mutation_type(a[i],b[i])
            if mutation_type == 'transition':
                transitions += 1
            elif mutation_type == 'transversion':
                transversions += 1
        return round(transitions/transversions,11)



def Main():
    solver = TRAN()
    a = 'ATGTAGCAATGTTCCGGCTGGGGTTACGAAAGCTGCTGAGCATGTCGACAGCAACCCTGTACGTCGGAGGTTAGGATGGTTAGATAGACATGCTGGGGCTGAGACAGACGTCAAAGAAAGACAGGCAGTGCGCCGCACAAACCAAATACAGATTCACTGGCTAATTGGTCGAGAGTCGATTCAGCAGAAGGAGCCCCACACATCTTTATGCATCATTCCGTATGATAATCGGCTCTGAACCGTACTTGATCATAATGTCAAATTCTGTGATGTGCAAGTGCTAACAATGCTTTTTACAGATCCGCAATCCGGCATAATCGAAGGTCTTATGTGGGCGCCTGTATGACAAATCCTCCTGTCTGTTGTGAGGTGCCTATGGTTGTTGCTTCCGAAGAGCTCGGTGGATACTATCAACTCTCAGGAAAAGGACTCCTGAGGCACAGTTCCGTGAGATCCTTCGCTTGTGAAGGTGGACGAAGTATGTTTTGCCTACTATTCCCGAACCGGCCCGTATCAAGGAACTCGTTCTAAGTAAGAATCAGTCTTTTGAGGTGTTCCAGGAGCCGAACCCTTTTAAAAGTAGATTTTCAATACGTATTCAAAATCACGCTGAGCCCGTTCGTATACGGCTAGCATCTTGGTTATGGAGTTCCCCAGCGCCTGATTAGAGGACTCCTGTGAGAGTAATCCATCTGCACTACAAAATCTCCGGCCCGTCTGCTCCCCTGTAAAACCTAGCAACATTATTCTACCGGACCCCAGGCGAGAATATGAGGGAGATTTCACTGTCCATTAGGCTCATAAATGCCCTATCCTCAGCAGCGTGTGAGGCGCTTTTCCACAGTGGCCTGGGTTGTCTTACTCACCCTAAGCCAACATTAGAAGACTACCTTTTGTACAGCTTTGGCCTCGCCAGTATAGC'
    b = 'ATGTAGCAAGGCTTTGCTCAGGGTCATGGAGGCTCCTTCGCGCGTCGACAGTAACCCTGTACTTCGGAGATTAGGAGGGTATGATAGATATCCCCGGACTGAGACAGCTATCGAATAAAAACAGGGAGCGCATCGCGCAAGTCGAACACAGATTTACTAGACACCAGTCCGAGTGTTGATCCTGCAAAAGGAGTCTCACACTTACTCGTGCATTATATTACTTGATAACAGGCTCTTAACCGTGCTTGATTAAAAAGTCCAATCCTTTGATACACAGATTTTAAAACTACCCTCTGCGGACCCACAATCTTCCATATTCGTAGATTTTATATAGCTGCCTGTGTAACAAGCCCACCCGTGTGATGTAGGGTTTCTATTGTTATTGCTTCCGAAGAGTCCCATGGGAACTATCAACCCTCAGGGTAGGGCCCCCCAAGGCACAGTTTCGTGAGATCCGTCAATTGTGAAGGTGGACAAAGCATGCTTTACCGGCCATAGCGGAACCGGCCCGGGTTAAGGGACTTACAACGGGCTTGGATTAGTCGTCTGAGGTGTTCTAGGAGCCAGGGCCCCCAAACTGTCGATTCTCAACACGTGTCCGAAATCATGTTGAGCGCGCCCATGTAAAGCCGGTATCTCTGTTAAGGAGTTACCCTGCGCCTATTTGGAGATCTCCTATAGTAGTAAACCATCTGCATTGTAAGGTTTTCGGCCCGTCTTTTCACCGGGGGAGCCTAACGATATTAGTTTGCCGGCCCCAAGCCGAGAATGCGAGAGCAATGTTACTCTTCACTAGGCCCACAGATGCCTTATCCCCGGCAGCCTATGAGACGTCGCTTTACAGTTACATAGGTTGGCTTGCTCGCCTCGAGCCAACATTAGGGTTTCATGCCTTCTACAGCCTTTATCTCGCCAATAAACC'
    print(solver.get_transition_transversion_ratio(a,b))
    a = 'A B C D E F G H'.split()
    n = 3
    print(*solver.get_lexicographical_order_of_alphabet(a,n))
    n = 3
    output = solver.get_signed_permutations_of_n(n)
    with open('output',"w") as output_data:
        output_data.write(str(len(output)) + '\n')
        output_data.write('\n'.join(output))


if __name__ == '__main__':
    Main()