import itertools
from functools import reduce
import re
from operator import neg


class CompressedMap:
    def __init__(self, data):
        self.data = list(map(lambda x: (x[0], x[1], x[1] + x[2] - 1), data))

    def __getitem__(self, item):
        b1, c1 = item
        seg = [(b1, c1)]
        result = []
        for d in self.data:
            new_seg = []
            for s in seg:
                remaining, intersection = self.subtract(s, d)
                new_seg.extend(remaining)
                result.extend(intersection)
            seg = new_seg
        result.extend(seg)
        return result

    def __repr__(self):
        return str(self.data)

    # subtract segments and apply mapping
    def subtract(self, s, d):
        # [] () or () []
        if s[0] > d[2] or s[1] < d[1]:
            return [s], []
        #  [   (   )   ]
        # d1  s0  s1  d2
        if s[0] >= d[1] and s[1] <= d[2]:
            return [], [(d[0] + s[0] - d[1], d[0] + s[1] - d[1])]
        #  [  (    ]   )
        # d1  s0  d2  s1
        if s[0] >= d[1] and s[1] > d[2]:
            return [(d[2] + 1, s[1])], [(d[0] + s[0] - d[1], d[0] + d[2] - d[1])]
        #  (   [   )   ]
        # s0  d1  s1  d2
        if s[0] < d[1] and s[1] < d[2]:
            return [(s[0], d[1] - 1)], [(d[0], d[0] + s[1] - d[1])]
        #  (   [   ]   )
        # s0  d1  d2  s1
        return [(s[0], d[1] - 1), (d[2] + 1, s[1])], [(d[0], d[0] + d[2] - d[1])]


def create_map(data):
    return CompressedMap(data)


def parse_data(data):
    seeds = list(map(int, filter(str.isdigit, data[0].split(' '))))
    maps = []
    curr = []
    for i in range(2, len(data)):
        if len(data[i]) == 0:
            maps.append(curr)
            curr = []
            continue
        if ':' in data[i]:
            continue
        curr.append(list(map(int, filter(str.isdigit, data[i].split(' ')))))
    maps = list(map(create_map, maps))

    return seeds, maps


def calc(seeds, maps):
    ranges = map(lambda x: (x[0], x[0] + x[1] - 1), (zip(seeds[::2], seeds[1::2])))
    for fmap in maps:
        ranges = list(itertools.chain.from_iterable(list(map(lambda x: fmap[x], ranges))))
    min_loc = min(map(lambda x: x[0], ranges))
    return min_loc


def read_data():
    with open('/home/kote/Downloads/input_5.txt', 'r') as f:
        data = f.read().splitlines()
    return data


data = read_data()
# print(data)
seeds, maps = parse_data(data)
# print(seeds)
# print(maps)
data = calc(seeds, maps)
print(data)
