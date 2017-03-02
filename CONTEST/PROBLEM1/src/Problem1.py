import sys

def Main():    
#     inp = '''4
# 4+6->1
# 2->3+5
# 4->6
# 6+4->5'''

    inp = sys.stdin.readlines()
    #print(inp)

    lines = list(map(lambda x: x.strip(),inp))
    #lines = inp.split('\n')

    #possible_chemicals = lines[0].split()
    possible_chemicals = set(lines[0].split())
    #possible_chemicals = lines[0].split()

    lines_tested = set()

    for i in range(1,len(lines)):
        lines_tested.add(i)


    while len(lines_tested) != 0:
        #print(lines_tested)
        #inp()
        lines_to_remove = []
        for i in lines_tested:
            left,right = lines[i].split('->')
            reactants = left.split('+')
            if all(reactant in possible_chemicals for reactant in reactants):
                lines_to_remove.append(i)
                products = right.split('+')
                [possible_chemicals.add(product) for product in products]
        #print(lines_tested)
        if len(lines_to_remove) == 0:
            break;
        [lines_tested.remove(j) for j in lines_to_remove]
        #input()

    print(*set(possible_chemicals))

if __name__ == '__main__':
    Main()