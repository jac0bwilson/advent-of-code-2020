import re

def part1(sections):
    rules = sections[0].split('\n')
    otherTickets = sections[2].split('\n')
    invalid = 0
    validOptions = set()

    # create a set of valid values to check against
    for rule in rules:
        values = re.match(r'\w+(?: \w+)?: (\d+)-(\d+) or (\d+)-(\d+)', rule)
        validOptions.update(range(int(values.group(1)), int(values.group(2)) + 1))
        validOptions.update(range(int(values.group(3)), int(values.group(4)) + 1))

    # find the invalid values and sum them up
    for ticket in otherTickets:
        found = re.findall(r'(\d+)', ticket)

        for match in found:
            val = int(match)

            if val not in validOptions:
                invalid += val

    print(invalid)

def part2(sections):
    rules = sections[0].split('\n')
    ruleRanges = {}
    myTicket = list(map(int, sections[1].split('\n')[1].split(',')))
    otherTickets = sections[2].split('\n')
    validOptions = set()
    validTickets = []

    # create the set of valid values, and store the rule bounds
    for rule in rules:
        values = re.match(r'\w+(?: \w+)?: (\d+)-(\d+) or (\d+)-(\d+)', rule)
        validOptions.update(range(int(values.group(1)), int(values.group(2)) + 1))
        validOptions.update(range(int(values.group(3)), int(values.group(4)) + 1))
        ruleRanges[rule.split(':')[0]] = [(int(values.group(1)), int(values.group(2)) + 1), (int(values.group(3)), int(values.group(4)) + 1)]

    # create a new list of only valid tickets
    for ticket in otherTickets:
        found = re.findall(r'(\d+)', ticket)
        found = list(map(int, found))

        if all([match in validOptions for match in found]):
            validTickets.append(found)

    # remove a blank ticket at the start of the list
    validTickets = validTickets[1:]

    # get the potential columns where a rule could be applied
    potential = {}
    for name, rule in ruleRanges.items():
        allValid = lambda x: all((valid[x] in range(rule[0][0], rule[0][1]) or valid[x] in range(rule[1][0], rule[1][1])) for valid in validTickets)
        potential[name] = {i for i in range(20) if allValid(i)}

    # match rules to rows and calculate the product
    prod = 1
    used = set()
    for opt in sorted(potential, key=lambda x: len(potential[x])):
        if opt.startswith('departure'):
            prod *= myTicket[(potential[opt]-used).pop()]

        used.update(potential[opt])

    print(prod)

sections = open('day16/input.txt', 'r').read().split('\n\n')
part1(sections)
part2(sections)