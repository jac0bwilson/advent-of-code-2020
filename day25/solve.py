def part1(pubKeys):
    loop = 0
    val = 1

    while val != pubKeys[0]:
        val = (val * 7) % 20201227
        loop += 1

    key = pow(pubKeys[1], loop, 20201227)
    print(key)

pubKeys = [int(line.strip()) for line in open('day25/input.txt', 'r')]
part1(pubKeys)