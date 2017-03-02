#failing test 5 wrong answer
class FINALROUND1:
    def __init__(self):
        self.exon_intervals = {}
        self.read_intervals = {}
        self.exon_expression = {}
        self.read_count_by_gene = {}
        pass

    def get_expression_value_of_genes(self,genes,reads):
        for i in reads:
            read = reads[i]
            genes_intersected = self.get_genes_intersected_by_read(genes,read)
            if len(genes_intersected) == 1:
                self.read_count_by_gene[genes_intersected[0]] = self.read_count_by_gene.get(genes_intersected[0],0) + 1
        return [self.read_count_by_gene[i] for i in sorted(self.read_count_by_gene.keys())]

    def get_genes_intersected_by_read(self,genes,read):
        return [i for i in range(len(genes)) if self.is_gene_interesected_by_read(genes[i],read)]

    def is_gene_interesected_by_read(self,gene,read):
        exon_index,read_index = 0,0
        while(exon_index < len(gene) and read_index < len(read)):
            result = self.is_interval_intersected(gene[exon_index],read[read_index])
            if result == 0:
                return True
            elif result == 1:
                exon_index += 1
            else:
                read_index += 1
        return False

    #naive check
    # def is_gene_interesected_by_read(self, gene, read):
    #     for exon_interval in gene:
    #         for read_interval in read:
    #             if self.is_interval_intersected(exon_interval,read_interval) == 0:
    #                 return True
    #     return False

    def is_interval_intersected(self,a,b):
        '''returns 0 if equal, -1 if a is lower, 1 if b is lower'''
        if (b[0] <= a[1] and b[0] >= a[0] or b[1] <= a[1] and b[1] >= a[0] \
                or a[0] <= b[1] and a[0] >= b[0] or a[1] <= b[1] and a[1] >= b[0]):
            return 0
        return 1 if b[0] > a[1] else -1

    def read_input(self):
        n,m = map(int,input().split())
        for i in range(n):
            intervals = input().split()
            self.read_count_by_gene[i] = 0
            self.exon_intervals[i] = [(intervals[j*2],intervals[j*2+1]) for j in range(len(intervals)//2)]
        for i in range(m):
            intervals = input().split()
            self.read_intervals[i] = [(intervals[j*2],intervals[j*2+1]) for j in range(len(intervals)//2)]





def Main():
    solver = FINALROUND1()
    solver.read_input()
    print(*solver.get_expression_value_of_genes(solver.exon_intervals,solver.read_intervals),sep='\n')

if __name__ == '__main__':
    Main()