from itertools import combinations
import math

expenses = [int(line) for line in open('day01/input.txt', 'r')]

for i in {2,3}:
    combination = combinations(expenses, i)
    answer = math.prod([combo for combo in combination if sum(combo) == 2020][0])
    print(answer)