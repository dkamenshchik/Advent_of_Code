import itertools
import math
from enum import Enum
from functools import reduce
import re
from operator import neg


def parse_data(data):
    path = data[0]
    map = {}
    for row in data[2:]:
        # XKM = (FRH, RLM)
        map[row[0:3]] = (row[7:10], row[12:15])
    return path, map


def least_common_multiple(path_lengths):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    return reduce(lcm, path_lengths)

def calc(path, map):
    currs = list(filter(lambda x: x[2] == 'A', map.keys()))
    path_lengths = [0]*len(currs)
    for i in range(len(currs)):
        while currs[i][2] != 'Z':
            for p in path:
                currs[i] = map[currs[i]][p == 'R']
                path_lengths[i] += 1
                if currs[i][2] == 'Z':
                    break
    return math.lcm(*path_lengths)


def read_data():
    with open('/home/kote/Downloads/input_8.txt', 'r') as f:
        data = f.read().splitlines()
    return data


data = read_data()
print(data)
path, map = parse_data(data)
print(path)
print(map)
data = calc(path, map)
print(data)
