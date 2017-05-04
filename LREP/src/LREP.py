class LREP:
    def __init__(self,DNA_string,k,nodes):
        self.DNA_string = DNA_string
        self.k = int(k)
        self.nodes = {}
        self.root_node = None
        for node in nodes:
            node = node.strip('\n')
            vals = node.split()
            if self.root_node == None:
                self.root_node = vals[0]
            self.nodes[vals[0]] = self.nodes.get(vals[0],[]) + [(vals[1],vals[2],vals[3])]
        self.longest_repeated_substring_k_or_more_times = {}

    def process_tree(self,prefix,node):
        if (node not in self.nodes.keys()):
            #self.longest_repeated_substring_k_or_more_times[prefix] = self.longest_repeated_substring_k_or_more_times.get(prefix,0) + 1
            return 1
        child_node_count = 0
        for edge in self.nodes[node]:
            child_node = edge[0]
            t_location = int(edge[1]) - 1
            t_length = int(edge[2])
            child_node_count += self.process_tree(prefix + self.DNA_string[t_location:t_location+t_length],child_node)
        self.longest_repeated_substring_k_or_more_times[prefix] = child_node_count
        return child_node_count

    def get_longest_substring_repeated_k_or_more_times(self):
        self.process_tree('',self.root_node)
        return self.get_longest_value_repeated_k_or_more_times()

    def get_longest_value_repeated_k_or_more_times(self):
        max_substring = ''
        for substring in self.longest_repeated_substring_k_or_more_times.keys():
            if len(substring) > len(max_substring) and self.longest_repeated_substring_k_or_more_times[substring] >= self.k:
                max_substring = substring
        return max_substring

def Main():
    with open('Dataset3.txt') as input_file:
        lines = [line for line in input_file]
    DNA_string = lines[0].strip('\n')
    k = lines[1].strip('\n')
    nodes = lines[2:]
    lrep = LREP(DNA_string,k,nodes)
    print(lrep.get_longest_substring_repeated_k_or_more_times())
    #print(lrep.longest_repeated_substring_k_or_more_times)

if __name__ == '__main__':
    Main()