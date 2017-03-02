import sys

sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class GC():
    def __init__(self):
        self.utils = RosalindUtilities()
        pass

    def get_GC_of_DNA(self,DNA):
        return (DNA.count('G') + DNA.count('C'))/len(DNA) * 100

    def get_largest_GC_of_file(self,file):
        strings = self.utils.read_input_file(file)
        max_GC = 0
        max_GC_label = ''
        for string in strings:
            GC_of_string = self.get_GC_of_DNA(string[1])
            if GC_of_string > max_GC:
                max_GC = GC_of_string
                max_GC_label = string[0]
        return (max_GC_label,max_GC)

def Main():
    gc = GC()
    file = 'dataset.txt'
    print(*gc.get_largest_GC_of_file(file),sep='\n')

if __name__ == '__main__':
    Main()