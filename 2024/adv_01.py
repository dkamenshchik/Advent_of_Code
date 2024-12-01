from collections import Counter


def read_data():
    with open('/home/kote/Downloads/input.txt', 'r') as f:
        data = f.read().splitlines()
    return data


def parse(x: str):
    return list(map(int, x.split()))


def process(x: list):
    [l, r] = [sorted(list(t)) for t in zip(*x)]

    pairs = zip(l, r)

    return list(map(lambda t: abs(t[1] - t[0]), pairs))


def process2(x: list):
    [l, r] = [list(t) for t in zip(*x)]

    freq_map = Counter(r)

    return list(map(lambda t: t * freq_map[t], l))


data = read_data()
print(data)
data = list(map(parse, data))
print(data)
data = process2(data)
print(data)
data = sum(data)
print(data)
