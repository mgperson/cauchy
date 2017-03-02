class REAR:
    def __init__(self):
        pass

    def get_hamming_distance(self,list_one,list_two):
        return sum(1 for a,b in zip(list_one,list_two) if a != b)

    def flip_interval(self,list,start_index,end_index):
        #actually won't need this as the flip works for start >= index
        if start_index >= end_index:
            raise IndexError
        return list[:start_index] + (list[end_index:start_index-1:-1] if start_index > 0 else list[end_index::-1]) + list[end_index+1:]

    def get_all_possible_flips(self,list):
        list_length = len(list)
        result = []
        for start_index in range(0,list_length-1):
            for end_index in range(start_index+1,list_length):
                result.append(self.flip_interval(list,start_index,end_index))
        return result

    def get_all_possible_flips_starting_at_position_i(self,list,i):
        list_length = len(list)
        result = []
        for start_index in range(i, list_length - 1):
            for end_index in range(start_index + 1, list_length):
                result.append(self.flip_interval(list, start_index, end_index))
        return result

    def get_result_with_lowest_hamming_distance(self,results,goal,tried):
        min_ham_distance = len(goal) + 1
        min_result = None
        for result in results:
             distance = self.get_hamming_distance(result,goal)
             # if (result in tried):
             #    print (result)
             #    print(tried)
             #    print (result in tried)
             if distance < min_ham_distance and result not in tried:
                min_ham_distance = distance
                min_result = result
        tried.append(min_result)
        return [min_ham_distance,min_result]
        #return min([self.get_hamming_distance(result,goal) for result in results])

    def get_flip_with_lowest_hamming_distance_of_all_possible_flips(self,start,goal,tried):
        flips = self.get_all_possible_flips(start)
        return self.get_result_with_lowest_hamming_distance(flips,goal,tried)

    def get_flip_with_lowest_hamming_distance_of_all_possible_flips_starting_at_point_i(self,start,goal,tried,i):
        flips = self.get_all_possible_flips_starting_at_position_i(start,i)
        return self.get_result_with_lowest_hamming_distance(flips, goal, tried)

    def get_position_of_first_difference(self,list_one,list_two):
        i = 0
        for a,b in zip(list_one,list_two):
            if a!=b:
                return i
            i+=1
        return -1

    def get_flip_with_correct_number_at_position_i(self,start,goal,i):
        end_index = start.index(goal[i])
        return self.flip_interval(start,i,end_index)

    def get_flip_with_correct_number_at_first_position_with_difference(self,start,goal):
        i = self.get_position_of_first_difference(start,goal)
        return self.get_flip_with_correct_number_at_position_i(start,goal,i)

    def find_reversal_distance_with_bfs(self,start,goal):
        visited,queue,previous_vertex_map = [], [start], {}
        vertex = start
        while queue and vertex != goal:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                i = self.get_position_of_first_difference(vertex,goal)
                new_vertices = self.get_all_possible_flips_starting_at_position_i(vertex,i)
                for new_vertex in new_vertices:
                    if new_vertex not in visited:
                        queue.append(new_vertex)
                        previous_vertex_map[tuple(new_vertex)] = vertex
        #print(previous_vertex_map)
        #print(previous_vertex_map[tuple(vertex)])
        #return vertex
        return self.get_number_of_steps_from_start(start,previous_vertex_map,vertex)

    def get_number_of_steps_from_start(self,start,previous_vertex_map,end):
        count = 0
        current_node = end
        while current_node != start:
            print (current_node)
            current_node = previous_vertex_map[tuple(current_node)]
            count += 1
        return count

    def find_reversal_distance(self,start,goal):
        current_hamming_distance = self.get_hamming_distance(start,goal)
        step_permutation = start
        step_permutations_tried = []
        starting_index_step_differs_at = self.get_position_of_first_difference(step_permutation,goal)
        step_count = 0

        while step_permutation != goal:
            lowest_hamming_distance_flip = \
                self.get_flip_with_lowest_hamming_distance_of_all_possible_flips_starting_at_point_i(step_permutation, goal,
                                                                                 step_permutations_tried,starting_index_step_differs_at)
                #self.get_flip_with_lowest_hamming_distance_of_all_possible_flips(step_permutation,goal,step_permutations_tried)
            if lowest_hamming_distance_flip[0] < current_hamming_distance:
                step_permutation = lowest_hamming_distance_flip[1]
                current_hamming_distance = lowest_hamming_distance_flip[0]
            else:
                step_permutation = self.get_flip_with_correct_number_at_first_position_with_difference(step_permutation,goal)
                current_hamming_distance = self.get_hamming_distance(step_permutation,goal)
            print(step_permutation)
            starting_index_step_differs_at = self.get_position_of_first_difference(step_permutation,goal)
            step_count += 1
            print(step_count)
        return step_count

def Main():
    rear = REAR()
    #perm = [8,6,7,9,4,1,3,10,2,5]
    #goal = [8,2,7,6,9,1,5,3,10,4]
    #perm = [3, 10, 8, 2, 5, 4, 7, 1, 6, 9]
    #goal = "5 2 3 1 7 4 10 8 6 9".split()
    #print(rear.find_reversal_distance(perm,goal))
    #perm = [10,3,5,1,4,6,7,9]
    #goal = [7,6,9,1,5,3,10,4]
    #perm = [10,3,5,1]
    #goal = [1,5,3,10]
    perm = [10, 2, 3,4,5,6,7,8,9,1]
    goal = [1,2,3,4,5,6,7,8,9,10]
    # tried = []
    # n = 0
    # while perm != goal:
    #     result = rear.get_flip_with_lowest_hamming_distance_of_all_possible_flips(perm,goal,tried)
    #     n+=1
    #     perm = result[1]
    #     print(result[1])
    #     print(result[0])
    #     print(n)
    #     input()
    print (rear.find_reversal_distance_with_bfs(perm,goal))
    #print(rear.find_reversal_distance(perm,goal))

if __name__ == "__main__":
    Main()