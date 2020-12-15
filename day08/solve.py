import copy, re

def parseInstructions(instructions):
    output = []

    for instruction in instructions:
        parse = re.match(r'([a-z]{3}) ([-+]\d+)', instruction)
        op = parse.group(1)
        num = int(parse.group(2))
        output.append([op, num])
    
    return output

def runProgram(instructions):
    acc, i = 0, 0
    visited = set()
    
    while i < len(instructions):
        if i in visited:
            return acc, False

        visited.add(i)
        op = instructions[i][0]
        num = instructions[i][1]        

        if op == 'acc':
            acc += num
            i += 1
        elif op == 'jmp':
            i += num
        else:
            i += 1

    return acc, True

def part1(instructions):
    parsed = parseInstructions(instructions)
    print(runProgram(parsed))  

def part2(instructions):
    parsed = parseInstructions(instructions)

    for i in range(len(parsed)):
        # used `copy.deepcopy` to ensure nothing is changed when it shouldn't be
        copyList = copy.deepcopy(parsed)
        if copyList[i][0] == 'jmp' or copyList[i][0] == 'nop':
            if copyList[i][0] == 'jmp':
                copyList[i][0] = 'nop'
            else:
                copyList[i][0] = 'jmp'

            acc, terminated = runProgram(copyList)

            if terminated:
                print(acc)
                return

instructions = [line.strip() for line in open('day08/input.txt', 'r')]
part1(instructions)
part2(instructions)