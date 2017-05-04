class SORT():
    def __init__(self):
        self.visited = []
        self.previous_vertex_map = {}
        pass

    def flip_interval(self,list,start_index,end_index):
        #actually won't need this as the flip works for start >= index
        if start_index >= end_index:
            raise IndexError
        return list[:start_index] + (list[end_index:start_index-1:-1] if start_index > 0 else list[end_index::-1]) + list[end_index+1:]

    def get_number_of_steps_from_start(self, start, previous_vertex_map, end):
        count = 0
        current_node = end
        while current_node[0] != start:
            print(current_node)
            current_node = previous_vertex_map[tuple(current_node[0])]
            count += 1
        return count

    def print_list_of_flips(self,start,previous_vertex_map,end):
        flips = []
        count = 0
        current_node = end
        while current_node[0] != start:
            flips.append((current_node[1],current_node[2]))
            current_node = previous_vertex_map[tuple(current_node[0])]
            count += 1
        print(count)
        for flip in flips[::-1]:
            print(*flip)

    def get_position_of_first_difference(self,list_one,list_two):
        i = 0
        for a,b in zip(list_one,list_two):
            if a!=b:
                return i
            i+=1
        return -1

    def get_all_possible_flips_starting_at_position_i(self,vertex,i):
        list = vertex[0]
        distance = vertex[3]
        list_length = len(list)
        result = []
        for start_index in range(i, list_length - 1):
            for end_index in range(start_index + 1, list_length):
                result.append((self.flip_interval(list, start_index, end_index),start_index+1,end_index+1,distance+1))
        return result

    def find_reversal_distance_with_bfs(self, start, goal):
        vertex = (start, -1, -1, 0)
        queue = [vertex]
        found = False
        while queue and vertex[0] != goal and vertex[3] < 4:
            vertex = queue.pop(0)
            if vertex[0] not in self.visited:
                self.visited.append(vertex[0])
                i = self.get_position_of_first_difference(vertex[0], goal)
                new_vertices = self.get_all_possible_flips_starting_at_position_i(vertex, i)
                for new_vertex in new_vertices:
                    if new_vertex[0] not in self.visited:
                        queue.append(new_vertex)
                        self.previous_vertex_map[tuple(new_vertex[0])] = vertex
        #print(previous_vertex_map)
        # print(previous_vertex_map[tuple(vertex)])
        # return vertex
        self.print_list_of_flips(start, self.previous_vertex_map, vertex)
        return vertex[0] == goal

def Main():
    #a = list(map(int,'1 2 3 4 5 6 7 8 9 10'.split()))
    #b = list(map(int, '1 8 9 3 2 7 6 5 4 10'.split()))
    a = list(map(int, '6 5 8 1 9 10 4 3 2 7'.split()))
    b = list(map(int, '4 6 2 5 9 7 3 1 10 8'.split()))
    solver = SORT()
    print(solver.find_reversal_distance_with_bfs(a,b))


if __name__ == '__main__':
    Main()