import itertools
from functools import reduce
import re
from operator import neg


def read_data():
    with open('/home/kote/Downloads/input_3.txt', 'r') as f:
        data = f.read().splitlines()
    return data


reg = re.compile('\d+|[^.]')


def parse(data: str, i: int):
    for match in reg.finditer(data):
        yield (i, match.start(), match.start() + len(match.group())), match.group()


def is_symbol_number(pair):
    l, r = pair
    return l[1].isdigit() != r[1].isdigit() and (l[1] == '*' or r[1] == '*')


def are_adjacent(cog, num):
    if abs(cog[0][0] - num[0][0]) > 1:
        return False
    l = cog if cog[0][1] <= num[0][1] else num
    r = num if l == cog else cog
    # ( [ ] )
    if l[0][2] >= r[0][2]:
        return True
    # ( [ ) ]
    if l[0][2] >= r[0][1]:
        return True
    return False


def get_digit(pair):
    l, r = pair
    s = l[1] if l[1].isdigit() else r[1]
    return int(s)


def has_same_cog(pairs):
    groups = {}
    for pair in pairs:
        cog = next(filter(lambda x: x[1] == '*', pair))
        number = next(filter(lambda x: x[1].isdigit(), pair))
        if cog in groups:
            groups[cog].append(number)
        else:
            groups[cog] = [number]

    groups = {k: v for k, v in groups.items() if len(v) == 2}

    return groups


def get_power(pair):
    l, r = pair
    return int(l[1]), int(r[1])


def get_adjacent(data):
    adjacent = []
    cogs = list(filter(lambda x: x[1] == '*', data))
    print(cogs)
    numbers = list(filter(lambda x: x[1].isdigit(), data))
    print(numbers)

    for cog in cogs:
        for num in numbers:
            if are_adjacent(cog, num):
                adjacent.append((cog, num))

    print(adjacent)
    adjacent = has_same_cog(adjacent)
    print(adjacent)
    adjacent = list(map(get_power, adjacent.values()))
    print(adjacent)
    adjacent = map(lambda x: x[0] * x[1], adjacent)
    return adjacent


data = read_data()
print(data)
data = list(map(lambda x: list(parse(x[1], x[0])), enumerate(data)))
print(data)
data = list(itertools.chain.from_iterable(data))
print(data)
data = list(get_adjacent(data))
print(data)
data = sum(data)
print(data)
