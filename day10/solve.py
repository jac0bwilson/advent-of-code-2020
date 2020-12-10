def part1(numbers):
    differences = [numbers[i] - numbers [i - 1] for i in range(1, len(numbers))]
    print(sum([1 for diff in differences if diff == 1]) * sum([1 for diff in differences if diff == 3]))

def part2(numbers):
    solutions = [1]
    for i in range(1, len(numbers)):
        opt = 0
        for j in range(i):
            if numbers[i] <= numbers[j] + 3:
                opt += solutions[j]
        solutions.append(opt)
    
    print(solutions[-1])

numbers = [int(line.strip()) for line in open('day10/input.txt', 'r')]
sort = sorted([0] + numbers + [max(numbers) + 3])
part1(sort)
part2(sort)