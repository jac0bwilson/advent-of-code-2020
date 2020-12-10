def trees(x, y, grid):
    curX, curY, count = 0, 0, 0
    gridWidth, gridHeight = len(grid[0]), len(grid)

    while curY < gridHeight:
        if grid[curY][curX] == '#':
            count += 1
        
        curX = (curX + x) % gridWidth
        curY += y

    return count

def part1(grid):
    print(trees(3, 1, grid))

def part2(grid):
    product = trees(1, 1, grid) * trees(3, 1, grid) * trees(5, 1, grid) * trees(7, 1, grid) * trees(1, 2, grid)
    print(product)

forest = [line.strip() for line in open('day03/input.txt', 'r')]

part1(forest)
part2(forest)