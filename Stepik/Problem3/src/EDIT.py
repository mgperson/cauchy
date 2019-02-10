class EDIT():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.len_a = len(a)
        self.len_b = len(b)
        self.edit_distance_dictionary = {}
        self.answer = self.__get_edit_distance()

    def __get_edit_distance(self):
        self.__initialize_distances()
        for i in range(1,self.len_a+1):
            for j in range(1,self.len_b+1):
                penalty = 1 if self.a[i - 1] != self.b[j - 1] else 0
                self.edit_distance_dictionary[str(i)+':'+str(j)] = min(self.__get_distance(i - 1, j) + 1,
                                                                       self.__get_distance(i, j - 1) + 1,
                                                                       self.__get_distance(i - 1, j - 1) + penalty)
        return self.__get_distance(self.len_a, self.len_b)

    def __get_distance(self, i, j):
        return self.edit_distance_dictionary[str(i)+':'+str(j)]

    def __initialize_distances(self):
        for i in range(self.len_a+1):
            self.edit_distance_dictionary[str(i)+':0'] = i
        for j in range(1,self.len_b+1):
            self.edit_distance_dictionary['0'+':'+str(j)] = j

def Main():
    a,b = 'YLCLWIPDSNWMQGSGCPGAKFQGSTLINIHAWFETTPTGFQFWKDCHYCCMPDFVECLHFEYCHFMPCYSHPQAEFGRIFDYCACTWYYCHSLSMGQQEEPYNLMPFRLGRCHTQMWGCCHMYFGYYNNYQSHCISGSLMYIFTVNFTLQLISEARNLLRRQRRVMWMIMPNWQDVWRIIVNKMTADELNQEYAICPKLCWAPLDWRSTAYKAIRGCWSNAMTPFVTNEYQAEVPFGYQWYFVNSMYLNDWRHGSWKITDLVDWKEKHNPLAFRFMSDQKNMKPSTMQDWILRRNVERFIPQIVTKENYPFSPESWMQVTTRCSCGSSSCPFFKPDHMPYRKFDMGFHKFAAHPDYKSPQNDFFRMYFFHGAAKLCTHHMNIQPTRYMGVLCTRWLLKHADDICYDWLQFGHCIKFHMRLRFVKMMWAYEYDAAQEVQMNKMRLPHDPELGIGQCFNQCHVTPGFPNTIWTAEGLVYSAGGHVNKRKISIMQCKPLNFKMLHDLIWIWEEEFWTQPKWGRHSTFRYSANWYSKQGGCFDLPLDAMYDGPKMFNRMKKHMLFGKQCLWNPNAEFAWRQAADKPANPAKRSGSTPKLHLRHQMDQFETDDQECVNACNYNYYVKESVFAVYQPSDWQDGENENINDVIVTWELGLTIHLGPMCAYRYTSWTCHWSKQCITHPTEFKRSWGADQFNGNYWTANWSKKTMQIQNWIARGNHYEEFGTYMNTHRSLTTDRFLRQCIRGRKYAYKEVWL',\
          'YLILWEPDSNWMQCSGCPPALQDHKFQGSTLHRNCCFMFETTNSKFAEDYQLIWTWRFQTISWVWKEQYEYCHYYRKNVGPTECRTGMGRPDVVTTQWCMNECLHHEYCHFFPCYSHPQAEFGRIFDYRQECTKEYYWDAWHKHERQQEELYGRCHTQMDLCQLEHYHMYFGYNNYQSHCSLIYIPWWTVNFTLKRNLYPMRRQRRVMWMIDVERPEDYIVYKSTFVTRDELNQENAICVKLCWAPLDWRSHAYKAIRGCWSNCMTPFVTNEYQAEQPFGYQWYFGHFLSMYLNDWRQGCHCTHHFWKITDLVDKQNPLAFREHRIEMSDQKDMKPSTMQCWILRRIVTKENYHCFMQYTTRCSCGSSSCFKPDHMPYRKFDMGFHKFVCHPDYKSPGNDFHWKPARPYFFHWAAVTFQLCTHHMNIQPTAYMGCFHTNRQPRADDICYDWCQPGHCIKLHGSAAQSVQMNKCTTGLKPRLPHDPELGIFQGIMKRHVRPGFPNTIWRLVYSNTGHVNKRKISIVQNENFHMLHDLWIWFEEFWTQHKWGMHSFFRYPEGRKLSKQGGCFDPLDAMMDGPKMFYPRPGVPMKKHMLFMPLWKWVRGDQNCQMAWRWARYTVNYMAICLATMLEEKKANPLWMYKRSPVASEISGESFVHRTTASYYVHKLHLETENSDQECVNACNYNYYVKESVFATHYCGPIPPDWQDGCINEEKTGVPYIMVTWELTSWTMHWLCKQCIIFLQITYDPTEFKRSCGADQFNGNYWTAKEVEMQWRWFKKTMQIQNWIARNNHYEEFGTHMSTVRSLFLRQHIIEDDDNHDVGRKYAYGYEVWV'
    a = 'CAAGCATTTCCTGTGGGGGAGG'
    b = 'CCCCCGGACCCTGCTGAATTC'
    solver = EDIT(a,b)
    print(solver.answer)

if __name__ == '__main__':
    Main()
