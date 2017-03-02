'''Problems Tree, Sset and Inod'''
class TREE:
    def __init__(self):
        self.edges = []
        self.subtrees = []
        self.missing_nodes = set()
        pass

    def get_count_of_powerset_elements_of_set_length_n(self,n):
        return 2**n % 1000000

    def get_internal_nodes_to_create_unrooted_tree_for_n_leaves(self,n):
        return n-2

    def add_edge_to_sub_tree(self,edge,tree):
        tree.add(edge[0])
        tree.add(edge[1])

    def consolidate_trees(self,tree_a,tree_b):
        tree_a = tree_a.union(tree_b)
        return tree_a

    def generate_sub_trees(self,edges):
        for edge in edges:
            appended_to_subtree = False
            for subtree in self.subtrees:
                if self.is_edge_in_tree(edge,subtree):
                    self.add_edge_to_sub_tree(edge,subtree)
                    appended_to_subtree = True
            if not appended_to_subtree:
                self.subtrees.append(set([edge[0],edge[1]]))

    def consolidate_all_trees(self,trees):
        new_trees = []
        while len(trees) > 0:
            tree = trees.pop()
            trees_to_remove = []
            for other_tree in trees:
                if len(tree.intersection(other_tree)) > 0:
                    tree = tree.union(other_tree)
                    trees_to_remove.append(other_tree)
            for tree_to_remove in trees_to_remove:
                trees.remove(tree_to_remove)
            new_trees.append(set(tree))
        return new_trees

    def generate_unique_sub_trees(self,edges):
        self.generate_sub_trees(edges)
        #this indicates an imperfect consolidation method, but DOES get the job done
        while (not self.edges_belong_to_one_subtree(self.edges,self.subtrees)):
            self.subtrees = self.consolidate_all_trees(self.subtrees)


    # def generate_sub_trees(self,edges):
    #     for edge in edges:
    #         subtree_added = None
    #         for i in range(len(self.subtrees)):
    #             subtree = self.subtrees[i]
    #         #for subtree in self.subtrees:
    #             if self.is_edge_in_tree(edge,subtree):
    #                 self.add_edge_to_sub_tree(edge,subtree)
    #                 if subtree_added != None:
    #                     subtree_added = self.consolidate_trees(subtree_added,subtree)
    #                     self.subtrees.remove(subtree)
    #                     break
    #                 subtree_added = subtree
    #         if subtree_added == None:
    #             self.subtrees.append({edge[0],edge[1]})

    def are_edges_connected(self,edge_a,edge_b):
        return edge_a[0] in edge_b or edge_a[1] in edge_b

    def is_edge_in_tree(self, edge, tree):
        return edge[0] in tree or edge[1] in tree

    # def subtrees_are_unique(self,subtrees):
    #     numbers_checked = set(subtrees[0])
    #     for i in range(1,len(subtrees)):
    #         for j in subtrees[i]:
    #             if j in numbers_checked:
    #                 return False
    #         numbers_checked = numbers_checked.union(subtrees[i])
    #     return True

    def edges_belong_to_one_subtree(self,edges,subtrees):
        for edge in edges:
            edge_belongs_count = 0
            for subtree in subtrees:
                if self.is_edge_in_tree(edge,subtree):
                    edge_belongs_count += 1
            if edge_belongs_count != 1:
                #print (edge,edge_belongs_count)
                return False
        return True

    def subtrees_are_unique(self,subtrees):
        for i in range(len(subtrees)-1):
            if len(subtrees[0].intersection(subtrees[1])) != 0:
                return False
        return True

    def get_num_nodes_to_connect(self):
        return len(self.subtrees) - 1 + len(self.missing_nodes)

    def read_data(self,file):
        with open(file) as input_data:
            n = int(input_data.readline())
            self.missing_nodes = set(map(str,range(1,n+1)))
            while True:
                line = input_data.readline().strip('\n')
                if line == '':
                    break
                values = line.split()
                if values[0] in self.missing_nodes: self.missing_nodes.remove(values[0])
                if values[1] in self.missing_nodes: self.missing_nodes.remove(values[1])
                self.edges.append(values)

def Main():
    solver = TREE()
    #solver.read_data('sample.txt')
    #print(solver.edges)
    #solver.generate_unique_sub_trees(solver.edges)
    #print(solver.get_num_nodes_to_connect())
    #print(solver.get_internal_nodes_to_create_unrooted_tree_for_n_leaves(4))
    print(solver.get_count_of_powerset_elements_of_set_length_n(858))

if __name__ == '__main__':
    Main()