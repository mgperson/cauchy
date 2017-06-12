#Matt Person
#Rosalind Problem: MPRT
#source
'''Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string
where the motif can be found.'''

import sys, re

sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class MPRT:
    def __init__(self,motif,protein_list):
        self.ru = RosalindUtilities()
        self.accessID_and_locations = self.get_locations_for_motif_in_uniprotid_list(motif,protein_list)

    def get_FASTA_for_uniprotid(self,uniprot_id):
        url_base = 'http://www.uniprot.org/uniprot/'
        url = url_base + uniprot_id + '.fasta'
        return self.ru.get_from_url(url).decode('utf-8')

    def get_protein_string_for_uniprotid(self,uniprot_id):
        result = self.get_FASTA_for_uniprotid(uniprot_id)
        return ''.join(result.split('\n')[1:])

    def get_locations_for_motif_in_protein(self,motif,protein):
        re_string = '(?=(' + motif + '))'
        matches = re.finditer(re_string,protein)
        return [match.span()[0]+1 for match in matches]

    def get_locations_for_motif_in_uniprotid_list(self,motif,uniprotid_list):
        results = []
        for uniprotid in uniprotid_list:
            print(uniprotid)
            protein = self.get_protein_string_for_uniprotid(uniprotid)
            locations = self.get_locations_for_motif_in_protein(motif,protein)
            if len(locations) > 0:
                results.append((uniprotid,locations))
        return results



def Main():
    motif = 'N[^P][ST][^P]'
    protein_list = '''P02725_GLP_PIG
P00304_ARA3_AMBEL
A4J5V5
O08537_ESR2_MOUSE
P07725_CD8A_RAT
Q8P5E4
Q90X23
Q66GC7
B8CH81
Q6A9W5
P98119_URT1_DESRO
P08709_FA7_HUMAN
Q68J42
B0RU89
Q8CE94'''.split('\n')
    mprt = MPRT(motif,protein_list)
    for entry in mprt.accessID_and_locations:
        print(entry[0])
        print(*entry[1])

if __name__ == '__main__':
    Main()