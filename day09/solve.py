from itertools import combinations

def part1(numbers):
    for i in range(len(numbers)):
        twentyFive = numbers[i:i+25]
        comb = combinations(twentyFive, 2)
        sums = [sum(opt) for opt in comb]
        if numbers[i + 25] not in sums:
            print(numbers[i + 25])
            return numbers[i + 25]

def part2(numbers, target):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if sum(numbers[i:j+1]) == target:
                sort = sorted(numbers[i:j+1])
                print(sort[0] + sort[-1])
                return

numbers = [int(line.strip()) for line in open('day09/input.txt', 'r')]
target = part1(numbers)
part2(numbers, target)