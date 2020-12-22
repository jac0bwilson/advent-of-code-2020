from collections import deque
from copy import deepcopy

def calculateScore(winner):
    multiplier = 1
    total = 0
    # take a copy to ensure nothing messes with original card sets
    winner = deepcopy(winner)

    while len(winner) > 0:
        total += multiplier * winner.pop()
        multiplier += 1

    return total

def part1(playerOne, playerTwo):
    queueOne = deque(playerOne)
    queueTwo = deque(playerTwo)

    while len(queueOne) > 0 and len(queueTwo) > 0:
        pOne, pTwo = queueOne.popleft(), queueTwo.popleft()
        if pOne > pTwo:
            queueOne.append(pOne)
            queueOne.append(pTwo)
        else:
            queueTwo.append(pTwo)
            queueTwo.append(pOne)

    winner = queueOne if len(queueTwo) == 0 else queueTwo
    print(calculateScore(winner))

def part2(playerOne, playerTwo):
    playedRounds = set()
    queueOne = deque(playerOne)
    queueTwo = deque(playerTwo)

    while len(queueOne) > 0 and len(queueTwo) > 0:
        scores = (calculateScore(queueOne), calculateScore(queueTwo))

        if scores in playedRounds:
            return scores[0]
        
        playedRounds.add(scores)
        pOne, pTwo = queueOne.popleft(), queueTwo.popleft()

        if pOne <= len(queueOne) and pTwo <= len(queueTwo):
            listOne, listTwo = list(queueOne), list(queueTwo)
            if part2(listOne[:pOne], listTwo[:pTwo]) > 0:
                queueOne.append(pOne)
                queueOne.append(pTwo)
            else:
                queueTwo.append(pTwo)
                queueTwo.append(pOne)
        elif pOne > pTwo:
            queueOne.append(pOne)
            queueOne.append(pTwo)
        else:
            queueTwo.append(pTwo)
            queueTwo.append(pOne)
    
    # negative score if player two wins so that the recursive results can be checked
    score = calculateScore(queueOne) if len(queueTwo) == 0 else -1 * calculateScore(queueTwo)
    return score

inputFile = open('day22/input.txt', 'r').read().split('\n\n')
playerOne = list(map(int, inputFile[0].split('\n')[1:]))
playerTwo = list(map(int, inputFile[1].split('\n')[1:]))

part1(playerOne, playerTwo)
print(part2(playerOne, playerTwo))