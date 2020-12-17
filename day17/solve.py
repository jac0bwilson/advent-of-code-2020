from itertools import product

def iterate(grid):
    newGrid = set()
    space = set()

    for cell in grid:
        space.update(product(*[[c - 1, c, c + 1] for c in cell]))

    for cell in space:
        neighbours = 0

        # find the active neighbours of the current spot
        for potential in product(*[[c - 1, c, c + 1] for c in cell]):
            if potential != cell and potential in grid:
                neighbours += 1
        
        # if a location should be active, add it to the next grid
        if cell in grid and (neighbours == 2 or neighbours == 3):
            newGrid.add(cell)
        elif cell not in grid and neighbours == 3:
            newGrid.add(cell)

    return newGrid

def part1(coords):
    # 3D coordinates from 2D grid
    grid = set((x, y, 0) for x in range(len(coords[0])) for y in range(len(coords)) if coords[y][x] == '#')

    for _ in range(6):
        grid = iterate(grid)
    
    print(len(grid))

def part2(coords):
    # 4D coordinates from 2D grid
    grid = set((x, y, 0, 0) for x in range(len(coords[0])) for y in range(len(coords)) if coords[y][x] == '#')

    for _ in range(6):
        grid = iterate(grid)
    
    print(len(grid))

coords = [line.strip() for line in open('day17/input.txt', 'r')]
part1(coords)
part2(coords)