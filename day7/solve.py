import re

rules = [line.strip() for line in open('day7/input.txt', 'r')]
ruleDict = {}
for rule in rules:
    parts = rule.split(' bags contain ')
    contained = [re.match(r'(\d+) (\w+ \w+)', section.strip()) for section in parts[1].split(',')]
    ruleDict[parts[0]] = [(int(matched.group(1)), matched.group(2)) for matched in contained if matched]

def part1(bagType):
    return bagType == 'shiny gold' or any([part1(bag[1]) for bag in ruleDict[bagType]])

def part2(bagType):
    return sum([b[0] + b[0] * part2(b[1]) for b in ruleDict[bagType]])

print(sum([any([part1(topLevelBag[1]) for topLevelBag in ruleDict[rule]]) for rule in ruleDict]))
print(sum([subBag[0] + subBag[0] * part2(subBag[1]) for subBag in ruleDict['shiny gold']]))