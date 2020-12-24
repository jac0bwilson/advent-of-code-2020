import re

# a set of (x, y) changes for each instruction, using axial coordinates
instructions = {
    'e': (1, 0),
    'se': (0, 1),
    'sw': (-1, 1),
    'w': (-1, 0),
    'nw': (0, -1),
    'ne': (1, -1)
}

def part1(references):
    flipped = set()

    for reference in references:
        x, y = 0, 0

        # iterate through the reference finding each instruction and applying it
        while len(reference) > 0:
            token = re.match(r'^(e|se|sw|w|nw|ne)', reference).group(1)
            dx, dy = instructions[token]

            x += dx
            y += dy

            reference = reference[len(token):]

        # if the location is already in the black tiles, remove it, if not, add it
        if (x, y) in flipped:
            flipped.remove((x, y))
        else:
            flipped.add((x, y))

    return flipped

# returns the set of all tiles surrounding the given one
def getNeighbours(tile):
    neighbours = set()

    for dx, dy in instructions.values():
        x, y = tile
        neighbours.add((x + dx, y + dy))

    return neighbours

# starts with the set of black tiles from part 1
def part2(black):
    for day in range(1, 101):
        nextBlack, nextWhite, toCheck = set(), set(), set()

        for tile in black:
            toCheck.add(tile)
            toCheck = toCheck.union(getNeighbours(tile))

        for tile in toCheck:
            neighbours = getNeighbours(tile)
            blackNeigh = len(black.intersection(neighbours))

            if tile in black:
                if blackNeigh != 1 and blackNeigh != 2:
                    nextWhite.add(tile)
            else:
                if blackNeigh == 2:
                    nextBlack.add(tile)
        
        for tile in nextBlack:
            black.add(tile)
        
        for tile in nextWhite:
            black.remove(tile)

    print(len(black))

references = [line.strip() for line in open('day24/input.txt', 'r')]
initial = part1(references)
print(len(initial))
part2(initial)