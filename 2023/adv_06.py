import itertools
from functools import reduce
import re
from operator import neg



def parse_data(data):
    time = int(str.join('', data[0].split()[1:]))
    distance = int(str.join('', data[1].split()[1:]))
    return time, distance


def get_ways(time, distance):
    for t in range(time + 1):
        d = t * (time - t)
        if d > distance:
            yield 1


def calc(time, distance):
    ways_to_win = 1
    for time, distance in zip([time], [distance]):
        ways_to_win *= sum(get_ways(time, distance))
    return ways_to_win

def read_data():
    with open('/home/kote/Downloads/input_6.txt', 'r') as f:
        data = f.read().splitlines()
    return data


data = read_data()
print(data)
time, distance = parse_data(data)
print(time)
print(distance)
data = calc(time, distance)
print(data)
