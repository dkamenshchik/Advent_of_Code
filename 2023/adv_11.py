def read_data():
    with open('/home/kote/Downloads/input_11.txt', 'r') as f:
        data = f.read().splitlines()
    return data


def expand_universe(data):
    galaxies = set()
    y = 0
    for i in range(len(data)):
        if len(set(data[i])) == 1:
            y += 1_000_000 - 1
        x = 0
        for j in range(len(data[i])):
            if len(set(x[j] for x in data)) == 1:
                x += 1_000_000 - 1
            if data[i][j] == '#':
                galaxies.add((i + y, j + x))
    return galaxies


def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def calculate(galaxies):
    total = 0
    while galaxies:
        current = galaxies.pop()
        total += sum(map(lambda x: get_distance(current, x), galaxies))
    return total


data = read_data()
print(data)
data = expand_universe(data)
print(data)
data = calculate(data)
print(data)
