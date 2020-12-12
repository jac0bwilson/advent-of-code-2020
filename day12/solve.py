import re

def parseInstructions(instructions):
    output = []
    for instruction in instructions:
        parse = re.match(r'(\w)(\d+)', instruction)
        output.append((parse.group(1), int(parse.group(2))))

    return output

def part1(instructions):
    x, y = 0, 0
    currentDir = 90 # angle relative to north

    for action, amount in instructions:
        if action == 'N':
            y += amount
        elif action == 'S':
            y -= amount
        elif action == 'E':
            x += amount
        elif action == 'W':
            x -= amount
        elif action == 'L':
            currentDir = (currentDir - amount) % 360
        elif action == 'R':
            currentDir = (currentDir + amount) % 360
        elif action == 'F':
            if currentDir == 0:
                y += amount
            elif currentDir == 90:
                x += amount
            elif currentDir == 180:
                y -= amount
            elif currentDir == 270:
                x -= amount

    print(abs(x) + abs(y))

def part2(instructions):
    shipX, shipY = 0, 0
    wayX, wayY = 10, 1 # 10 units east and 1 north

    for action, amount in instructions:
        if action == 'N':
            wayY += amount
        elif action == 'S':
            wayY -= amount
        elif action == 'E':
            wayX += amount
        elif action == 'W':
            wayX -= amount
        elif action == 'L':
            for _ in range(amount // 90):
                wayX, wayY = -wayY, wayX
        elif action == 'R':
            for _ in range(amount // 90):
                wayX, wayY = wayY, -wayX
        elif action == 'F':
            for _ in range(amount):
                shipX += wayX
                shipY += wayY
        
    print(abs(shipX) + abs(shipY))

instructions = [line.strip() for line in open('day12/input.txt', 'r')]
parsed = parseInstructions(instructions)
part1(parsed)
part2(parsed)