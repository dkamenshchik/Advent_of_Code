from collections import Counter
from itertools import pairwise

from numpy import sign


def read_data():
    with open('/home/kote/Downloads/input.txt', 'r') as f:
        data = f.read().splitlines()
    return data


def parse(x: str):
    return list(map(int, x.split()))


def process(x: list):
    for r in x:
        yield process_single(r)


def process_single(r):
    pairs = pairwise(r)
    diff = list(map(lambda p: p[1] - p[0], pairs))
    return 1 if all(map(lambda d: sign(d) == sign(diff[0]) and abs(d) <= 3, diff)) else 0


def process2(x: list):
    for r in x:
        res = process_single(r)
        if res == 1:
            yield 1
        else:
            for i in range(len(r)):
                # k - r without ith element
                k = r[:i] + r[i + 1:]
                if process_single(k) == 1:
                    yield 1
                    break
        yield 0


data = read_data()
print(data)
data = list(map(parse, data))
print(data)
data = process2(data)
print(data)
data = sum(data)
print(data)
