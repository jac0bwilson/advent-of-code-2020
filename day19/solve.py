import re

def check(rules, ruleID, message, start):
    rule = rules[ruleID]

    checkRuleForChar = re.match(r'\"(\w)\"', rule)

    if checkRuleForChar:
        return {start + 1} if start < len(message) and checkRuleForChar.group(1) == message[start] else set()
    else:
        limits = set()

        # break up the 'OR' rules
        for subRule in rule.split(' | '):
            reserves = {start}

            # get each part of the rule's order
            for part in subRule.split(' '):
                temp = set()

                for index in reserves:
                    temp = temp | check(rules, int(part), message, index)
                
                reserves = temp

            limits = limits | reserves
        
        return limits

def part1(ruleDict, inputs):
    count = 0

    for message in inputs:
        if len(message) in check(ruleDict, 0, message, 0):
            count += 1

    print(count)

def part2(ruleDict, inputs):
    ruleDict[8] = '42 | 42 8'
    ruleDict[11] = '42 31 | 42 11 31'
    count = 0

    for message in inputs:
        if len(message) in check(ruleDict, 0, message, 0):
            count += 1

    print(count)

# process the input
inputFile = open('day19/input.txt', 'r').read().split('\n\n')
rules = inputFile[0].split('\n')
inputs = inputFile[1].split('\n')
ruleDict = {}

for rule in rules:
    parts = rule.split(': ')
    ruleDict[int(parts[0])] = parts[1]

part1(ruleDict, inputs)
part2(ruleDict, inputs)