def solver(numbers, target):
    said = {}
    last = 0

    for i, val in enumerate(numbers):
        said[val] = i
        last = val

    for i in range(len(said), target):
        last_added = last
        if last in said.keys():
            last = i - 1 - said[last]
            said[last_added] = i - 1
        else:
            said[last] = i - 1
            last = 0

    print(last)

solver([10, 16, 6, 0, 1, 17], 2020)
solver([10, 16, 6, 0, 1, 17], 30000000)