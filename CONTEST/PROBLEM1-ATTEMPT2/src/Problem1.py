import sys

class Problem1:
    def __init__(self):
        self.lines = {}
        pass

    def load_initial_chemicals(self,line):
        self.chemicals = set(line.split())
        pass

    def load_line(self,line):
        #print(line)
        left, right = line.split('->')
        reactants = left.split('+')
        products = right.split('+')
        for reactant in reactants:
            if reactant in self.lines:
                self.lines[reactant].append((reactants,products))
            else:
                self.lines[reactant] = [(reactants,products)]
        #self.lines.append((reactants,products))

    def process_lines(self):
        #line_processed = True
        #process initial chemicals
        process_queue = [chemical for chemical in self.chemicals]
        #print(process_queue)

        while process_queue:
            chemical = process_queue.pop(0)
            if chemical in self.lines:
                self.process_chemical(chemical,process_queue)

        #for chemical in list(self.chemicals):
#            self.process_chemical(chemical)

        #chemical_processed = True
        #while chemical_processed:

        # while line_processed:
        #     #print(self.lines)
        #     line_processed = False
        #     for line in self.lines:
        #         line_processed = line_processed or self.process_line(line)
        print(*self.chemicals)

    def process_chemical(self,chemical,queue):
        for line in list(self.lines[chemical]):
            if all([reactant in self.chemicals for reactant in line[0]]):
                for product in line[1]:
                    if product not in self.chemicals:
                        self.chemicals.add(product)
                        if product in self.lines:
                            queue.append(product)
                            #self.process_chemical(product)
                for reactant in line[0]:
                    self.lines[reactant].remove(line)

    def process_line(self,line):
        #print(line[0])
        if all([reactant in self.chemicals for reactant in line[0]]):
            [self.chemicals.add(product) for product in line[1]]
            self.lines.remove(line)
            return True
        return False


def Main():
    # inp = '''4
    # 4+6->1
    # 2->3+5
    # 4->6
    # 6+4->5'''

    inp = sys.stdin.readlines()

    lines = list(map(lambda x: x.strip(), inp))

#     inp = '''1 2
# 1+2->4
# 1+2->3
# 3->4+5
# 4->4'''
#     lines = inp.split('\n')

    solver = Problem1()
    solver.load_initial_chemicals(lines[0])
    for i in range(1,len(lines)):
        solver.load_line(lines[i].strip())
    #print(solver.lines)

    solver.process_lines()


if __name__ == '__main__':
    Main()