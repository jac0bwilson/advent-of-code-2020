from copy import deepcopy

def simulate(seats, maxOccupied, tolerance):
    nextSeats = [['#' if seat == 'L' else '.' for seat in line] for line in seats]
    height = len(seats)
    width = len(seats[0])
    checkRange = lambda col, row: 0 <= col < height and 0 <= row < width # checks that coordinates are within range

    while nextSeats != seats:
        seats = nextSeats
        nextSeats = deepcopy(seats)

        for col in range(height):
            for row in range(width):
                if seats[col][row] == '.':
                    continue
                
                nearby = 0

                for j in range(-1, 2):
                    for i in range(-1, 2):
                        newCol, newRow = col + j, row + i

                        if (j == 0 and i == 0) or not(checkRange(newCol, newRow)):
                            continue

                        if tolerance:
                            while checkRange(newCol + j, newRow + i) and seats[newCol][newRow] == '.':
                                newCol += j
                                newRow += i

                        if seats[newCol][newRow] == '#':
                            nearby += 1
                
                if seats[col][row] == 'L' and nearby == 0:
                    nextSeats[col][row] = '#'
                elif seats[col][row] == '#' and nearby >= maxOccupied:
                    nextSeats[col][row] = 'L'

    return sum([row.count('#') for row in seats])

seats = [line.strip() for line in open('day11/input.txt', 'r')]
print(f'Part 1: {simulate(seats, 4, False)}')
print(f'Part 2: {simulate(seats, 5, True)}')