def part1(lines):
    valid = 0

    for line in lines:
        parts = line.split(' ')
        minmax = parts[0].split('-')

        letter = parts[1][0]

        count = 0
        for char in parts[2]:
            if char == letter:
                count += 1
        
        if count >= int(minmax[0]) and count <= int(minmax[1]):
            valid += 1
        
    print(valid)

def part2(lines):
    valid = 0

    for line in lines:
        parts = line.split(' ')
        pos = parts[0].split('-')

        letter = parts[1][0]

        # only one of these should be true - so XOR
        if bool(parts[2][int(pos[0]) - 1] == letter) ^ bool(parts[2][int(pos[1]) - 1] == letter):
            valid += 1

    print(valid)

lines = [line.strip() for line in open('day2/input.txt', 'r')]
part1(lines)
part2(lines)