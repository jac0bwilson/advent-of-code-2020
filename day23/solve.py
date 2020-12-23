def part1(cups, moves):
    current = 0
    length = len(cups)

    for _ in range(moves):
        cup1, cup2, cup3 = cups[(current + 1) % length], cups[(current + 2) % length], cups[(current + 3) % length]
        curCup = cups[current]
        dest = curCup - 1

        cups.remove(cup1)
        cups.remove(cup2)
        cups.remove(cup3)

        while dest not in cups:
            dest = dest - 1 if dest > min(cups) else max(cups)

        # recombine with the 3 cups back in the right place
        destIndex = cups.index(dest)
        cups = cups[:destIndex + 1] + [cup1, cup2, cup3] + cups[destIndex + 1:]

        current = (cups.index(curCup) + 1) % length

    # get the list of cups starting at 1, and looping back around
    oneIndex = cups.index(1)
    cups = cups[oneIndex + 1:] + cups[:oneIndex]

    print("".join(map(str, cups)))

def part2(cups):
    minCup = min(cups)
    cupDict = {}

    # generate all the extra values
    maxCup = 1000000
    extra = list(range(max(cups) + 1, maxCup + 1))
    cups = cups + extra

    # use a dictionary to link every cup to it's clockwise neighbour
    for i in range(1, len(cups)):
        cupDict[cups[i - 1]] = cups[i]

    # complete the circle
    cupDict[cups[i]] = cups[0]
    cupDict[-1] = cups[0]
    current = -1

    for i in range(10000000):
        curCup = cupDict[current]
        cup1 = cupDict[curCup]
        cup2 = cupDict[cup1]
        cup3 = cupDict[cup2]
        nextCup = cupDict[cup3]
        dest = curCup - 1

        while True:
            if dest < minCup:
                dest = maxCup
            
            if dest in [curCup, cup1, cup2, cup3]:
                dest -= 1
            else:
                temp = cupDict[dest]
                cupDict[dest] = cup1
                cupDict[cup3] = temp
                break
        
        cupDict[curCup] = nextCup
        current = curCup

    target = cupDict[1]
    target2 = cupDict[target]

    print(target * target2)

# just a list based solution, runs basically instantly for this input size
part1([1,3,7,8,2,6,4,9,5], 100)

# changed to a dictionary based approach, every key's value is the cup after
part2([1,3,7,8,2,6,4,9,5])