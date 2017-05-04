class PCOV():
    def __init__(self,kmers):
        self.kmers = kmers.split('\n')
        self.prefix_length = len(self.kmers[0]) - 1
        self.superstring_length = len(self.kmers)
        self.generate_superstring()

    def generate_superstring(self):
        self.superstring = self.kmers.pop()
        while len(self.superstring) < self.superstring_length:
            next_kmer_to_append = self.get_next_kmer_to_append(self.superstring)
            self.kmers.remove(next_kmer_to_append)
            self.superstring += next_kmer_to_append[-1:]

    def get_next_kmer_to_append(self,current_string):
        prefix = current_string[-self.prefix_length:]
        for kmer in self.kmers:
            if kmer.startswith(prefix):
                return kmer

def Main():
    with open('input.txt') as input_data:
        lines = ''.join([line for line in input_data])
    pcov = PCOV(lines)
    print (pcov.superstring)

if __name__ == '__main__':
    Main()


