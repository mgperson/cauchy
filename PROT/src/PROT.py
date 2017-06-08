#Matt Person
#Rosalind Problem: PROT
#source
'''Given: An RNA string ss corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.'''

import sys

sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class PROT:
    def __init__(self,s):
        self.utils = RosalindUtilities()
        self.protein_string = self.get_AA_codes_from_RNA(s)

    def get_codons_from_RNA(self,RNA):
        return [RNA[i:i+3] for i in range(0,len(RNA),3)]

    def get_AA_codes_from_RNA(self, RNA):
        result = ''
        for codon in self.get_codons_from_RNA(RNA):
            code = self.utils.get_amino_acid_code_for_codon(codon)
            if code == 'Stop':
                return result
            result += code
        return result

def Main():
    RNA = 'AUGGACUGCGGUGACCGUGAUCAAAGUAACCUUAAGCCGUCACUCCCGAGUAUACAACCAUUCACUUGUGGGAGGACAAGUGUAGCCGAAAACACCCCCUGCCGUGAGUACUCGCAGAGCCCCGCGUAUAGAGCCGAGAAGGCUGGUACGAUGCCCUGUAUUAGCAGGUGCGGCCUCGUCCCUGCCCCUUUUCAGAACUUGAUCAAACUUGGUAUAGCUCCUCUGGCACAGAAGGGGGAGAUACCCGUCUCUAUACCCCGACAACGAAUUCUCUGUUCACAUCAGAGGGCUAUCUUCCGGGGGAAUCUUGAGGUGCAAGUGAUGCAGGUUUGCACCAAGGAUCAAAGUUCCUUCGCGCUUUUUGAACGGACCCCCCAUAAAUCGGAGAUAGCGCAGCUAACGCCACCCAUAGUUUUUAACCUGGAUUCUUUUUAUUUCUUAAACGGCAAACUGCAAACGAUGGCCUACAUGAGUGCUCUGGGGAAGCCGCUCGAGUACCAUCUGACUGAGCCGCACCGUCACAGCGCUGACUUUAUAGCACCCUAUCUACCCCUGUGGCGCCGGAAUUGCAAUCACGAGGUGUGUAGCGUUGCAUCGUUGUUAGAGACGCAGCCCUUAUGGGUUGAAUGUUCAGUAUUUGAAUUAUACGGGAAUACGGCGCCCAGAUUAGCCUGGAAGCUUACAGGGGAAACUGCCAUCCUGCGGAGUAGAAUUAAAUAUCAGCCGCCCACUCGUGUGGCAGUCAGAUCGUGCUUUCUGCGCGUGGCCGAAUCCGAUCCGCCUGUUCGUACGGCCUCAUCUGCGAGAGACAGAUUUUCGACUGCAUUCCCCUCGGUCGCGUCCUCUUAUAUGGAAAAGGACAAUAGGGUAGCUACGUCGGAGAAACGUGUGAGAUUAUUGACUUGGGUCCGCACCUUACACCUAGUGGUGGAACAUCCUGAGCAGCCUUUGCCUCGCGAUUUAGUUUUGCCUAUCCUUUGGGGAAAACAAAGGAUGCAACCAUUACCUCGCAUGACGUUCCUUGGGGGAUGCCGUGCGGUACGCCAGGUUGCCGCUUUCACACGAACGAUACUCAAACCUAUCGUACACGGCCCUUCCUUGUAUGCUUGCGAUCACCAGAAAAAGGCCAGCGGGGUGAUGAUCAAAAAACUCAUACGCGAUGGGGCCGCGACUUCCUCACACGUAGCGACGAGGAGAAAGGUACUCGUUAGGGGGAUCCCACAAGUAGUUCCCCGCAGACGAGGAAAGCCCGGGCAAGAUUGGGACCGUGACACGAACACUCCAAGGCUGACGAUUAGGCAGGGGAUGCUCACUAUUGGAAUUGAGACUUUGGUCUGGCGUAUGCUCCGUCCAGUCCUAUGGGCCUUAUUGCGGGUAACUUCGGUAAGCGCCGGAGUGCGAUCGACCGGACACAGAGAUGUAGAACGUUAUCUAAAUGUCUCCUCUCGACACAGUAGUAGCCACCAGCCCCGUAACAAAAAACUUUCUGGGGCAACGACAGAAUACACCGUCGCUCGUCGGCGACACCAUACUCCCUCCAAGUCAGAGACGCAAUCUCUCGAGCCCCGUGAUUCCUUCCAAUUUGAGACUUUCUCGCCACACACCUCGUCACCAGCCCGUCCAUCUAGAGUUACACCCUUGUCUGUGUGUACACAAGCGGUUAAUCUAUACCGUCUUAACUAUUGUGUUCCUGGUCGGACCGUUACCGUUCCUGGAAUGUCGUACCAGUUUUGUCAUGUAGGGCUACUACCAGGAAGCCGUCUGUACGUAGAUCGACCCGUACGGUUCAGAACGCGCCGCUCAUCUGCAAAUCCGGAGCCGAUCUCGGGAGGUAAGGCAGUUUUACGCAAGUGGCCGGGCACGUCUUUGGUUGACAGGCAGGGGUUGAACGGGACACCACCGUCCGCUCCAUACGGUCAAGACGCUGCUGUCGUCGUACCAUUCCUAUGUAAACAAGUGGGCCACAGCCAUCAGUAUGUCUUUGGCGAUUUCCUCACUAACAAAAAUCCCAAUGAGCCAUCUUCUGGAACGACUCUUUGUAGGAUGCUUACGGUUCGCAAGAAUGAACGCUGGCUUGGGGCGCCCAGAUGGUACCGAUCCGUGACAUCGCGCGUGAUCCAAGUACUCAUCCCUGGAUACCACAGGAGUCCGAGCCCUCAUCCAGCACAAGGACGAUAUCUGCUUCACUUCAGGAAUGACAAAUCCGCUAGUCAUCAGACAAAGGGCCCGAUAGUCAGAAUACUCCUCCUGUCUAGUGCUAUGAAGGUUUCAUGUAGAUGCCACGCAGAACUCCUCUGCUCCAAGAGGAUGACGCCCAGAGGUCUCGUUAGCAUACGCCUAUGUCGAUACUGUUUCAUGGGCCCGUGGUGCCUGUUCGCACAGCCGUACACGCUUGUUUCCUCAUUCAGCCUUAACCAUGUUCCAUACUUUUUAUCCUUGUUGUCGGUUGCAAAUCGUAGGGUCGCUACGUUCUUAAAUAGCGGUCUCUACCGACAGUCUGGUCCCGGCGGCUCGGUUUAUCACAGAUUCGCCCGGUACCCGCUUCUUUCUAAAGGAACGAAAAUCGUGUAUGGGGACGUAGCCGGUUCUGCUCCUGAGACGGAUAGUAGAGCGCCGGAUCUCGAAGUAAUAGGACUAUUUAUACGUAAAUCCCCAGACGCAGAAGUUCGGUUGUCUCCAGGAGACGGAGCGCAGCCGUAUGGAGAAUCGGUCAUAAGACUCUUGGACCCGCCGCGUCCUGACCUGCGAUUGCGUCCCAGCCUCGUGACACAACCAAGUCCUUAUGCACAGCCAUCGACCCCUGAACUGAGUGGGAGUUCUGAGAAUAGUGGGGCUUCGAGGCCGUGUCGACUAGCAACUCUUUUGGUUCCCCCGAAUCGAGGGGUUCUUCGCGCAGGGCUUGGCGCCAAGGGUGAAUAUUCCCUCUGUCGCUGCGUGGCUUGCGAAUACCGUUCUCCACGUUUGAUCCUCCGCCACAUGCGCGGUUCAAUGAUUUUACCAUUCGUGAUUAGCAACUGCACUAAACACCAUUGCAGUAGACCUGUAAUGCAUCUGCGAGAUAACCGGGAUGGCUGGACAAUUGAGAGGGCCCUCCUCAAUCUAACCGAAUUAGCAGACUUAUGGCGCUCUUUAAGUACAGUCGAAUCUGCUUUCUUGCGGGUGUUGCGUACGGCCCCGUUAGGGGGUCAUCUAAAAAUUUCGGGGCUGUGUCGGUUCUCAGGCCUGUGUGCAUUGCAAGUAGUGUCUACACCGGUCCGACCAGCUGUUUCUCGUCACGUCUUCCGUCCCAUCGAAAUAAUUAUGGGGGUCCGCCGCCGACCCGCCGCGGAGGCUCGGCUCGGCAGAGGUAACAAGGACGAGCGACGGAGCCUGACCAACUCGUAUAUCAGCCAGCCGGGACCCAUCCGUGGGAAGCAAAAGUUAAUAAGUUCUAAUAGAUGCGUGAUAUCCACGGUUGCCAAUACGAUGCAUUUUGCUCCGCCUUCUACGACAUGCCUAUCGCGUUCACCGAUGGAUCGUUAUAACUGGCCUCGAAACUUCUACGAAACUGUAUAUGCAGGGGGGGAUAUCCGAACUACCGUGGAUUUGGGUUAUAGCAACGAUUGUGUUGAAGGGGAGCAGAGGUUUAUAGAGCGAACUACAGACCAGCUAGCCAGCGGGAUACACAACACGUUGAAGGGAGGGCGCAACAGAGGUUUCGCUGCACGCAAUGCGGUCACCGACCGAGAAUGGGCGUACGAACAGUUGUUAUUUAGGUGCUACCCUCCCCGCGAGUGUACUGAACAGCUCCAUUCCCCGGUCGUCGCAGCAACACGAACCAUCGAACUUUGGGUACCGGAGGUUUUAGUAGUACCGGCGCGUAUUUCCUUCCUUCGACAUGGACUGUCUUCUAGUCAGACCCGGUUGAGCUUAUCAUUUCCCGGCAUGUCACAGAGAAUCAAGAGCCGAUUCGCUGCGGUACCCGUGACGAACGUCAAAAGUAUCAGCUUAUGCUACGUUAGGUCUCCCCUAGUGAUCGGGAGACUCAAAUACUGCCUGCCCUCUCUCGAGGUCUCCAGAGGCUGGGCCCUUUCGAUUUUGCCGAGACUUGUCUACUUUCUAGAGACCCGGCAUAUGCGCUUUAGUUUAUACGUAUUUGAGCUUAUAAACCUUGUGCCCUUACCCUGGAGGAGUAAGGGAGUGUCUACUGGAACGCAGGGCCACACCCGAGACAUUGUGUUUGGUAUAAGGCAAAUUGGUAGAGUCAUUGACGGCAGAUUGUGCCAGCGCAUUAGAUUCACACAUCGUUCACCCAGCCCCAUUAGAAGACUAUGGUUAGUCUUGCGUAAGAUUCUCCCGGGGAUGGAAGACCAAGUGGCCCGGCAAAACGCAUAUGACAAUCUCGACGCUCUUUCCAAUUGCUGUAUUUGGUCCAGCAAUGCGGGCUAUGACUUCAGGCCUGGCGAAAGGCUAUCCCGGGUACUUCCCUGGCAUUCUGUAGUCUCAACAAUUAAGAGCCGAAGUCGCUUCAAGGCAACGAUAAAUUGUGCUCCCGGUUUGCCCUCAGGAACCUUUUCUCCAUCGACGACGACUAGCCUUUUUUCCUGGAGAUCACUUCGGCCGGCUAGCUCGAAGUCUCAUUAUAAAUUGACUGGCGACAGCCAGAACCUUGAUUCCGAGUGCGGGCUCCUGGCAAAGAUUCGAAAAAAACAGUAUAGAUUUUCGGCAGUAGAAAGCUCUAGUUCCGACACAGAAUAUCCAGUGCGGGGUCACAGCCGCAGAUUACGUUUAAUUCACGGUCUUCUUAAAGAUCAAAUGCUGCUAACGCUAUGUACCCCGAUUCGCAGCUACCGAGUUCUGACUUCUCAGUCCAGCCCUAUGCAUUUUACCGGGAUAGAAACUAUUGUAGGGACAGAUGUCCUACACAGGCGGAAACACACGUACAGCCCGGCCUGGUCAACGCGUUGCACGUACGGUUCGGAUCUCUGUUAUCUUAGGGAUGAAUUUAUGUGCGGUACAAAGGGGGACGGGGAUACUGUGGCUGGAAGCACGUACAUCAUUAGGCUGCUUUACUUUAUUCCCCGCACCUACUAUCGAAUGCCUACGCCAAGCUUUGCAGCAGCCGCGCCACUAACGUCUGGCGGACCGGGCCAUGCAGACCACAGACGCGUGUGGCAUGAUCUCAGGAGCAGACUGUGGAUCGACGGACACCAUGGUAGACGUACGAAGCGCAUUACGAACGAUGGGCCCGAGACGUGCGUAACCGCAAGGGACACUUGUGACAAUUAUAAAUCCCUGCUAUGCACCUGCCUAAUCCGAGCGACGACCUUCCGUCCGUUCAAUAGGGUGCCCCGCAGUGUGAUGUAUCACUGGGACUACGCUUCUAUCGGCAAGUACCUGGACAAUCAAGACGGGGGAUCUUACGCACGGGGAGUACUAUUGGUCCUCCGCCGUGACAUAUCACUUCUGCCAGAGAUAGACAGGAGGGUACCGAACAAAACUUAUUCUAAGCCUGAUCACAUCAUUCUUUUAGUACUUAUGCGGGUUAGCUUUACAAAAGAGAGGGUGACUGGUGGCAAUGACCCUUGUGAGCCGAAGGCCUUAUCUCGCAAGUUUGGUUUAGGACGCCACGGGAAUUUACGUUGCACACUAGGCCAUACGUCGAAAGUAGGAUCGAGGAACGAGAUGCACUAUAUGACCAUCACGCGGCUCAGAGGCAAUCUAGCCCGCCAGGCAUGCAUCUCGGAGGAGGCACCCAACGAUUUCUCUACUGUCUUUUCUUCCGAAGUGACGAUCCUCAGGAACCUGGCUAUGCCGAUAACAUGCCCUGAUUACACCCGAGGCGGAAACAUAAUCUGCUUGUCUGUAUCAACAUGCUGGGGACGCGUUUCUUUGAAUCUCAAGGCCGGUGCUGAAGGGCGUCCAGCUAAUUGUGGUCCGCCUUUAAGUUGCCUCAUUAGACCACGAUACUCGUCAAGUCCGCCACCCGCUCGGUUGUGCUUACAUGUCAUUUUUGCCAUUGUACACGAACGAAAAGUGGCAACAGUGACCUUGUUGACGUCACAUGGCGCGACGCGAUUACUGUCUAGGGAGUAUCUCCAUAUGAACUUGUGCAUUACGCCAUCAUUAUGUUUCCACGGGAGCAUACCCUGCCCCAAUUCACACUCGGGGUCUAAUUCGCAAAUCAGGAAUUCAACCCAGAGGCAUAAAGUGAUGCUGAUACGACGGGUCUCGAGGGACUACGGCUUACCGGGUCAAAUUAAUCGUGCAUGCGGCCCACCUUGUCAGGCGCCUUUAGGAGUACCAUCCAGGGCACACGAUGCAUCACGUGUAUGGCGGUCAAAAUGCAAGCUUGAAUGGGGUGCCACCCGAGAAACACCUAAAACCGCGCGAAGCGAUCAUCUGGCGAAGCAAGUCGACUUGGGUCAGCUUCAGAAGGAGUGCUCCGGCUCGCCCGGAUUCAGUGCAUUGAUAACUACCUCCCAUUUAGGGAGACCGUGUGCCAGGCUAAAUCUGUUGCUAUGCUCUAUUGAUUGCUUCGCGCACCCUAACUUGCUACAUGCUCAAAUCAACCGCGCAGAGCUAUUUUGUAGGAUAAUACCCUGGGUUGCUACCGAGGAACCUCACCGAGACCUUGUUGGCUCAAUCACUGUUGACAAUUCCAUCGGCAAUGAUAAAACUCUUGUUCGCUUUCCUCAGGCUCAGAAAUGGGCGAUCUCGGGCUCCCUACUAGCGCGUUGUGCAUGGCGGCUUAUGACACCUCUACAGGGGGGAAACCCGGGCCACGUGUACCAGGGCUUGCUUGUGCUGUCCCGUUUGUCUCACUUACUUCCUUAUGGACGACUUCCGAUACAACGACUGCUUGAAGGGAGGAUGCCACAAGCGGUUACGCUGGGCGACACCCAUGGGGAACCAGCUGACUUUGCACGCUUAACCUAUGGGUGGCGCCUUGCUGAGGCCGGUGCUUACACCUUCACCAUUCCCCACCUCGAAAGUCGAAAUAAAUUGGACGAGGCUCGGUCCCCGGCGCCACACGCAACGAUGACCCAACGAAGGGUCACCGGUACUCUAGCUGCGAUUCCAUACCAGCACGCUGUUCAUUACGCGAACACAUGUGCGGUCCCGUGGGGCGCGAUCCAACGCUUUCAGCUCGCAAACACACUUGGAGGAACGCCAGCACUGACCUGGAAGAUAUCUAUAACUUCGUCGGUCGUGCGCCGAGACCGAACCCAUCGUUCAAGUGGCUGUUCGGAAACUUCAGCUCCUAUGCAUCUGGGGGAUAUUCCGUCGCGUCGCUCAGUGAUCCCGAGACCCCACAUAGCGUUCCGCUCUAAGAGACCAGGGGCACUCGUUCAGAAUCUGACAGGCCCCCCAAUACAUGACACCUGGCCGGAAGAGACGACUUAUGGCCCUCUUUGCACUCCUACAUGUACGGCUGAAGGCUGUACUGACUUCCCCAAUCCAAAGCGCGCUGCAUCGACCCGUUGCGAGCACGCAUUGCCGCGGGGUAAAAAACGCUAUGGUCCUGUAGUCCAGUGUAAACAGCAGCAUCAUAAAUGUUGGGGGGCAUUCAAGCAGAGUCUGACCCGCGUUUUAAUAUGGAGACCACAGCUUUUUUUCACAGUGACCUUACUGGUUCUUGUUCCUAAUAUCCGGGGAUCUAUGUCCUACGGGCCACAAUUCGGUCGACAAAGGUUGGAUACGUCAGUAGCCCUUCUCUUUGUAACGAUCUACGGCAGAGUUCCUGUCGUCGCUGUUCACUCAAUUAACGUUGUCCUUAAGAAGAAGCGGUCUCAUAUUGAUGCGCAACCGUAUCCAUGGCGCCUGCGCAGUACGUGCAAAAAGCUUCCGGAGGUCCGAUCGCAUAAGGGGUGGUGGAUCAGUUGGCCUGACUUAAUAUAUCGGGUCCAUAUGGCCGAUCUGAUUGGCUAUCAGUCAAUAAGUCUAUUCGGCUGGCGACGGUGUGGCUGCGGGGCAGUGAAGGUAACCUAUGAACCCCUGCUAAUUAGGGCCAGAAGCAUAUGUACUUAUGAGUACCAUGCACCCGUUUCUUGUUGGCAUCUUAAGGGAAGUCACAAGCAAAACUUAAGUCGGAGGAAGAUGAACCCAGGUGUGUCGAGGUCGAGACUCGUUAAUCCUGGCCCGUCCGCGGUAGUGACCGCUGUUGCCUCCGGGUCAUCGUGCCACCAAAAACCUGAGUCAACGCCCUACCUGUCAGAGGGGUAUGACGCGGCUGCUAUAACGCUUUGUAAAAUCUUGUGCACUGAUACUGCUCCGUGUUUACUAGCUGGUCGGUGGAUUUCAGUCCCACCCCGCACAUUGGGGGCCUACACAUCUGUAUUUGUCGUUUCGUUUAGUACUGAGAUCUUAUGCUUUAUUGGGGGCCUCGCGAAACAUUUGCCAGCCAUAGGGCCUUUGUCCGGUCUUACUGCUUCUUUAUACGCCAACACGGGGCACGCGCUGACAAUCGGAACCCGUCCAACGCAACAUCUCCCAUUCGCAGUUGUCCUGAUUGAACCCUGCUUAUACGAGGCUUAUCAGGUGGGUUCUUUGCCCGAGCACCGGCUUGCCUUGGCGAUUACCUGUCCUGCUCCGCGUGAGUGGGACCAAUUGGGCAGCCGCCGCCGAGGAAUUGGCCUGACCCACCCCCCCAUACGGCGCCUGCGCUUAAAUCCACUAGCGAACGGGUACGUCCAAAAAUUUCACUUUCCAGUACCCAGAACAAGAAUGGAGGGAAAUACCUGUGUGUGGGUAGGUCUCGAUAUGUGGUGUGUGGACAACCUAAUGCAGCUUCUUCGAUUCCAUUCCGACAAGAGUGUUCCCCGAGUUCGAGGCGUCACUCUCCGGCCUUAUAAUCGAAACCUUUGCGGUCCGUUAGUAGACGGUAGGGUUCCGAGACACCCUAAACCCACAUGGUCAUACGUGGUUGGGCCUGUAGGGAACCCAGCAACCCCCGCAGAAACAUACAAUUUCCUGUCAAAAGUUAGUGGCUUCUGCGAGAUGGUUACCGAACUCUUCCCGACUAGGCUUCGUAGGGGUAUGCCGGUUAUACCGCACACAGUUUGCACCCCCCGGGGCGUCGGACCGUACCUCGCGACAGGGCGUCCAUUCUACAAAGGGCAACCAAAGACAGUGCGAAGUUUUCAACACCGAACAUAA'
    prot = PROT(RNA)
    print (prot.protein_string)


if __name__ == '__main__':
    Main()