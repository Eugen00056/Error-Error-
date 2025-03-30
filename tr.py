def find_in_list(list, text, number=0):
    number = [i for i in range(len(list)) if str(list[i]) == str(text) and i >= number]
    return number 
def run(program, input_data=''):
    cells = [0 for i in range(257)]
    output = ''
    element = 0
    prog = program.replace('\n', '').split('  ')
    prog2 = prog
    command_number = 0
    while command_number < len(prog):
        command = prog[command_number]
        if command == 'NameError':
            output += str(chr(cells[element]))
        elif command == 'TypeError':
            element = (element - 1) % 256
        elif command == 'EOFError':
            element = 0
        elif command == 'MemoryError':
            cells[element] = find_in_list(cells, ord(prog[command_number+1]))[0]
            command_number += 1
        elif command == 'UnicodeEncodeError':
            comand_number = find_in_list(prog[command_number:], 'RecursionError')
            cells[256] = ''.join(prog[command_number+1:command_number])
            command_number += comand_number - command_number
        elif command == 'SystemExit':
            cells, element, text = str(run2(cells[256], cells, element, input_data))
            output += text
        elif command == 'KeyError':
            element = (element + 1) % 256
        elif command == 'ZeroDivisionError':
            cells[element] = (cells[element]-1) % 256
        elif command == 'SyntaxError':
            cells[element] = (cells[element]+1) % 256
        elif command == 'ValueError':
            brecets1 = find_in_list(prog2, 'ValueError', command_number)
            brecets2 = find_in_list(prog2, 'StopIteration', command_number)
            for i in range(len(brecets1)):
                c = True
                if brecets1[i+1:] != []:
                    for j in brecets1[i+1:]:
                        if j < brecets2[i]:
                            c = False
                if c == True:
                    while cells[element] != 0:
                        cells, element, text = run2(prog2[brecets1[0]+1:brecets2[i]], cells, element, input_data)
                        output += text
                    command_number += len(prog2[brecets1[0]+1:brecets2[i]])
                    break

        elif command == 'IndexError':
            cells[element] = ord(input_data[0])
            input_data = input_data[1:]
        command_number += 1
    return output

def run2(program, cells, element, input_data=''):
    prog = program
    prog2 = program
    output = ''    
    command_number = 0
    while command_number < len(prog):
        command = prog[command_number]
        if command == 'NameError':
            output += str(chr(cells[element]))
        elif command == 'TypeError':
            element = (element - 1) % 256
        elif command == 'EOFError':
            element = 0
        elif command == 'MemoryError':
            cells[element] = find_in_list(cells, ord(prog[command_number+1]))[0]
            command_number += 1
        elif command == 'UnicodeEncodeError':
            comand_number = find_in_list(prog[command_number:], 'RecursionError')
            cells[256] = ''.join(prog[command_number+1:command_number])
            command_number += comand_number - command_number
        elif command == 'SystemExit':
            cells, element, text = str(run2(cells[256], cells, element, input_data))
            output += text
        elif command == 'KeyError':
            element = (element + 1) % 256
        elif command == 'ZeroDivisionError':
            cells[element] = (cells[element]-1) % 256
        elif command == 'SyntaxError':
            cells[element] = (cells[element]+1) % 256
        elif command == 'ValueError':
            brecets1 = find_in_list(prog2, 'ValueError', command_number)
            brecets2 = find_in_list(prog2, 'StopIteration', command_number)
            for i in range(len(brecets1)):
                c = True
                if brecets1[i+1:] != []:
                    for j in brecets1[i+1:]:
                        if j < brecets2[i]:
                            c = False
                if c == True:
                    while cells[element] != 0:
                        cells, element, text = run2(prog2[brecets1[0]+1:brecets2[i]], cells, element, input_data)
                        output += text
                    command_number += len(prog2[brecets1[0]+1:brecets2[i]])
                    break

        elif command == 'IndexError':
            cells[element] = ord(input_data[0])
            input_data = input_data[1:]
        command_number += 1
    return cells, element, output