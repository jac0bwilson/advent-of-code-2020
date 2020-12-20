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

tiles = open('day20/input.txt', 'r').read().split('\n\n')
tileList = []

for tile in tiles:
    splitTile = tile.split('\n')
    header = splitTile[0]
    tileID = int(re.match(r'Tile (\d+):', header).group(1))
    tileList.append((tileID, splitTile[1:]))

part1(tileList)