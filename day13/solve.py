def part1(time, routes):
    minimum = max([route for _, route in routes])
    minBus = 0

    for _, route in routes:
        wait = route - (time % route)

        if wait < minimum:
            minimum = wait
            minBus = route

    print(minimum * minBus)

def part2(routes):
    product, time = 1, 0

    for diff, route in routes:
        while True:
            if (diff + time) % route == 0:
                break
            
            time += product
        product *= route

    print(time)

times = [line.strip() for line in open('day13/input.txt', 'r')]
time = int(times[0])
routes = [(i, int(x)) for i, x in enumerate(times[1].split(',')) if x != 'x']
part1(time, routes)
part2(routes)