import unittest

from ..FINALROUND1 import FINALROUND1

class TestFINALROUND1(unittest.TestCase):
    def setUp(self):
        #self.genes = {0: [('1000', '1200'), ('2000', '2400')], 1: [('3000', '3300')]}
        #self.reads = {0: [('1100', '1160')], 1: [('1190', '1200'), ('2000', '2050')],
         #        2: [('3280', '3300'), ('3500', '3550')], 3: [('1500', '1560')]}
        self.genes = {0: [('1100', '1100'), ('2000', '2400')], 1: [('3000', '3300')]}
        self.reads = {0: [('1100', '1160')], 1: [('1190', '1200'), ('2000', '2050')], 2: [('3280', '3300'), ('3500', '3550')],
         3: [('1500', '1560')]}
        self.solver = FINALROUND1()

    def test_get_genes_intersected_by_read(self):
        #self.assertEqual(self.solver.get_genes_intersected_by_read(self.genes,self.reads[0]),[0])
        #self.assertEqual(self.solver.get_genes_intersected_by_read(self.genes, self.reads[2]), [1])
        self.assertEqual(self.solver.get_genes_intersected_by_read(self.genes,self.reads[1]),[0])
        self.assertEqual(self.solver.get_genes_intersected_by_read(self.genes, self.reads[0]), [0])
        self.assertEqual(self.solver.get_genes_intersected_by_read(self.genes, self.reads[2]), [1])

    def test_get_expression_value_of_genes(self):
        #self.assertEqual(self.solver.get_expression_value_of_genes(self.genes,self.reads),[2,1])
        self.assertEqual(self.solver.get_expression_value_of_genes(self.genes, self.reads), [2, 1])

    def test_is_interval_intersected(self):
        interval_a = (1000,1200)
        interval_b = (1100,1600)
        self.assertEqual(self.solver.is_interval_intersected(interval_a,interval_b),0)
        interval_a = (2000, 3000)
        interval_b = (1500, 3500)
        self.assertEqual(self.solver.is_interval_intersected(interval_a, interval_b),0)

    def test_is_gene_interesected_by_read(self):
        gene = [(1000,1200),(2000,2400)]
        read = [(1100,1160)]
        self.assertTrue(self.solver.is_gene_interesected_by_read(gene,read))
        gene = [(3000,3300)]
        read = [(1190, 1200) ,(2000, 2050)]
        self.assertFalse(self.solver.is_gene_interesected_by_read(gene, read))
        gene = [(1100, 1100),(2000,2400)]
        read = [(1190, 1200), (2000, 2050)]
        self.assertTrue(self.solver.is_gene_interesected_by_read(gene, read))

    def test_is_input_correct(self):
        #self.solver.read_input()
        print(self.solver.exon_intervals)
        print(self.solver.read_intervals)
        pass