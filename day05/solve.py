def getSeatID(seat):
    mapping = {
        'F': '0',
        'B': '1',
        'L': '0',
        'R': '1'
    }
    newstr = ''
    for char in seat:
        newstr += mapping[char]
    
    return int(newstr, 2)

def part1(seats):
    print(max(map(getSeatID, seats)))

def part2(seats):
    seatIDs = list(map(getSeatID, seats))
    sortedIDs = sorted(seatIDs)

    for i in range(len(sortedIDs)):
        if sortedIDs[i + 1] - sortedIDs[i] == 2:
             print(sortedIDs[i + 1] - 1)
             break

seats = [line.strip() for line in open('day05/input.txt', 'r')]
part1(seats)
part2(seats)