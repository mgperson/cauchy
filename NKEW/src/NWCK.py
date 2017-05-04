'''Revised NWCK works for both NKEW and NWCK with weighted edges, otherwise default 1'''

class NWCK:
    def __init__(self,NWCK_tree):
        self.nwck_tree = NWCK_tree
        self.edges = {}
        self.GUID = 0
        self.i = 0
        self.load_all_edges()
        pass

    def load_all_edges(self):
        next_token = self.get_next_token()
        while next_token != ';':
            if next_token == '(':
                self.load_edges()
                next_token = self.get_next_token()
        #print(self.edges)

    def get_GUID(self):
        self.GUID += 1
        return self.GUID

    def load_edges(self):
        nodes_at_level = []
        next_token = self.get_next_token()
        while next_token != ')' and next_token != ';':
            if next_token == '(':
                nodes_at_level.append(self.load_edges())
            elif next_token not in '(,':
                nodes_at_level.append(next_token)
            next_token = self.get_next_token()
        next_token = self.get_next_token()
        root_node_weight = ''
        if self.is_special_character(next_token.split(':')[0]):
            next_token_values = next_token.split(':')
            node = str(self.get_GUID())
            if len(next_token_values) > 1:
                root_node_weight = ':' + next_token_values[1]
            else:
                self.i -= 1
        else:
            node = next_token
        #print(node)
        self.add_edges(nodes_at_level,node)
        return node + root_node_weight

    def add_edges(self,nodes,root_node):
        for node in nodes:
            node_values = node.split(':')
            node_name = node_values[0]
            edge_weight = int(node_values[1]) if len(node_values) > 1 else 1
            #self.edges[node_name] = self.edges.get(node_name,[]) + [root_node]
            #self.edges[root_node] = self.edges.get(root_node, []) + [node_name]
            self.edges[node_name] = self.edges.get(node_name, []) + [(root_node,edge_weight)]
            self.edges[root_node] = self.edges.get(root_node, []) + [(node_name,edge_weight)]

    def get_distance_between_nodes(self, node_a, node_b):
        # BFS of edges
        queue = [((node_a,0),0)]
        visited = set()

        while len(queue) > 0:
            node = queue.pop()
            node_name,edge_distance,node_distance = node[0][0],node[0][1],node[1]
            visited.add(node_name)
            if node_name == node_b:
                return node_distance + edge_distance
            for adjacent_node in self.edges[node_name]:
                if adjacent_node[0] not in visited:
                    queue.insert(0, (adjacent_node, node_distance + edge_distance))
        return -1

    def is_special_character(self,char):
        return char in '(),;'

    def get_next_token(self):
        start_pos = self.i
        if start_pos >= len(self.nwck_tree):
            return ''
        end_pos = start_pos + 1
        if self.is_special_character(self.nwck_tree[start_pos]):
            self.i = end_pos
            return self.nwck_tree[start_pos]
        while not self.is_special_character(self.nwck_tree[end_pos]):
                end_pos +=1
        self.i = end_pos
        return ''.join([self.nwck_tree[i] for i in range(start_pos,end_pos)])


def Main():
    with open('Dataset') as input_data:
        values = [line for line in input_data]
    result = []
    for i in range(len(values)//3+1):
        nwck = NWCK(values[i*3])
        #print(nwck.edges)
        nodes = values[i*3+1].split()
        node_a,node_b = nodes[0],nodes[1]
        #print(node_a,node_b)
        result.append(nwck.get_distance_between_nodes(node_a,node_b))
    print(*result)
'''6 18 25 6 76 60 9 13 2 8 9 63 6 14 13 27 9 2 2 13 2 2 19 9 2 2 21 11 4 16 26 2 23 7 8 10 9'''
if __name__ == '__main__':
    Main()