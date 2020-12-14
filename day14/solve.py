import re

def part1(lines):
    curMask = ""
    outputs = {}
    for line in lines:
        if line.startswith('mask'):
            curMask = re.match(r'mask = ([X01]+)', line).group(1)
        else:
            memMatch = re.match(r'mem\[(\d+)\] = (\d+)', line)
            content = (int(memMatch.group(1)), int(memMatch.group(2)))
            binary = "{0:036b}".format(content[1])
            masked = int(''.join([val if val != 'X' else binary[i] for i, val in enumerate(curMask)]), 2)
            outputs[content[0]] = masked
    
    print(sum(outputs.values()))

def setValues(out, address, value):
    if address.count('X') == 0:
        out[address] = value
        return
    setValues(out, address.replace('X', '1', 1), value)
    setValues(out, address.replace('X', '0', 1), value)

def part2(lines):
    curMask = ""
    maskCount = 0
    outputs = {}
    for line in lines:
        if line.startswith('mask'):
            curMask = re.match(r'mask = ([X01]+)', line).group(1)
            maskCount = curMask.count('X')
        else:
            memMatch = re.match(r'mem\[(\d+)\] = (\d+)', line)
            content = (int(memMatch.group(1)), int(memMatch.group(2)))
            binary = "{0:036b}".format(content[0])
            masked = ''.join([val if val != '0' else binary[i] for i, val in enumerate(curMask)])
            setValues(outputs, masked, content[1])
    
    print(sum(outputs.values()))

inputs = [line.strip() for line in open('day14/input.txt', 'r')]
part1(inputs)
part2(inputs)