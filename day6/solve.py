def part1(answers):
    total = 0
    for answer in answers:
        answer = answer.replace('\n', '')

        characters = set(answer)
        total += len(characters)

    print(total)

def part2(answers):
    total = 0

    for answer in answers:
        individuals = answer.split('\n')
        responses = []
        for individual in individuals:
            responses.append(set(individual))

        total += len(set.intersection(*responses))
    
    print(total)

answers = open('day6/input.txt', 'r').read().split('\n\n')
part1(answers)
part2(answers)