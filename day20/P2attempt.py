import re
from math import sqrt

def getBorders(tile):
    borders = [tile[0], tile[-1]]
    borders.append("".join([tile[i][0] for i in range(len(tile))]))
    borders.append("".join([tile[i][-1] for i in range(len(tile))]))
    reverse = []
    
    for border in borders:
        reverse.append(border[::-1])

    borders.extend(reverse)

    return borders

def getOuter(tiles):
    tileBorders = {}

    for tileID, tile in tiles:
        borders = getBorders(tile)
        tileBorders[tileID] = borders

    allBorders = []

    for borders in tileBorders.values():
        allBorders.extend(borders)

    corners = []
    edges = []

    for tileID, borders in tileBorders.items():
        unique = 0

        for border in borders:
            if allBorders.count(border) == 1:
                unique += 1
        
        # 2 unique sides per corner, plus reversed representations
        if unique == 4:
            corners.append(tileID)
        elif unique == 2:
            edges.append(tileID)

    return corners, edges

def part1(tiles):
    corners, _ = getOuter(tiles)
    product = 1

    for corner in corners:
        product *= corner

    print(product)

def rotate(tile):
    newTile = []
    for i in range(len(tile)):
        newTile.append("".join([tile[j][len(tile) - 1 - i] for j in range(len(tile))]))

    return newTile

def assemble(tileList):
    sides = int(sqrt(len(tileList)))
    corners, edges = getOuter(tileList)
    outer = corners + edges
    inner = filter(lambda x: x[0] not in outer, tileList)
    assembled = [[None for _ in range(sides)] for _ in range(sides)]

    if len(inner) == 0:
        toUse = filter(lambda x: x[0] in outer, tileList)
        
        itemCount = 0
        for i in range(sides):
            for j in range(sides):
                if itemCount == 0:
                    assembled[i][j] = toUse[1]
                else:
                    ...
                
                itemCount += 1

    else:
        ...

    return

def part2(tileList):
    # create the layout
    assembled = assemble(tileList)
    # remove the outer edges
    # create overall map
    # replace sea monsters
    seaMonster = """\
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
    """
    # count number of '#'s

    return

tiles = open('day20/input.txt', 'r').read().split('\n\n')
tileList = []

for tile in tiles:
    splitTile = tile.split('\n')
    header = splitTile[0]
    tileID = int(re.match(r'Tile (\d+):', header).group(1))
    tileList.append((tileID, splitTile[1:]))

part1(tileList)

# part2(tileList)

# print("\n".join(tileList[0][1]))
# print("-------------------------")
# print("\n".join(rotate(tileList[0][1])))