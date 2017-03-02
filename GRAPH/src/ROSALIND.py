class ROSALIND():
    def __init__(self):
        pass

    def read_input_file(file):
        values = []
        with open(file) as input_data:
            current_line = ''
            for line in input_data:
                if line[0] == '>':
                    label = line[1:]
                    if not current_line == '':
                        values.append((label,current_line))
                    current_line = ''
                else:
                    current_line += line.rstrip('\n')
            values.append(current_line)
        return values