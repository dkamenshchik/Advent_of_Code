import re
from collections import Counter
from itertools import pairwise

from numpy import sign


def read_data():
    with open('/home/kote/Downloads/input.txt', 'r') as f:
        data = f.read().splitlines()
    return data


def parse(x: str):
    [total, components] = x.split(':')
    return int(total), list(map(int, components.split()))


def process(x: list):
    for r in x:
        yield process_single(r)


def process_single(r):
    total, components = r
    return total if can_be_combined(total, components) else 0


def can_be_combined(total, components):
    curr = {components[0]}
    for c in components[1:]:
        new = set()
        for v in curr:
            new.add(v + c)
            new.add(v * c)
            new.add(int(f"{v}{c}"))
        curr = new
    return total in curr


data = read_data()
print(data)
data = list(map(parse, data))
print(data)
data = process(data)
print(data)
data = sum(data)
print(data)
