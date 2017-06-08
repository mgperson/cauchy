#Matt Person
#Rosalind Problem: SUBS
#source
'''Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.'''

class SUBS():
    def __init__(self,s,t):
        len_s, len_t  = len(s),len(t)
        self.locations = [i + 1 for i in range(len_s-len_t) if s[i:i+len_t] == t]

def Main():
    s,t = 'GATATATGCATATACTT', 'ATAT'
    subs = SUBS(s,t)
    print(*subs.locations)

if __name__ == '__main__':
    Main()
