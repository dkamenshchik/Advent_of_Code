import itertools
import math
from enum import Enum
from functools import reduce
import re
from operator import neg


def parse_data(data):
    return list(map(lambda x: list(map(int, x.split())), data))


def predict(data):
    if all(map(lambda x: x == 0, data)):
        return 0
    diff = list(map(lambda x: x[1] - x[0], zip(data[:-1], data[1:])))
    # print(diff)
    res = predict(diff)
    return data[0] - res

def calc(data):
    return sum(map(predict, data))


def read_data():
    with open('/home/kote/Downloads/input_9.txt', 'r') as f:
        data = f.read().splitlines()
    return data


data = read_data()
print(data)
data = parse_data(data)
print(data)
data = calc(data)
print(data)
