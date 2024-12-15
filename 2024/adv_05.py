import itertools
from collections import Counter
from itertools import pairwise

from numpy import sign


def read_data():
    with open('/home/kote/Downloads/input.txt', 'r') as f:
        data = f.read().splitlines()
    return data


def parse(x: [str]):
    pipe_list = []
    comma_list = []

    for s in x:
        if '|' in s:
            pipe_list.append(s)
        elif ',' in s:
            comma_list.append(list(map(int, s.split(','))))

    return pipe_list, comma_list


def process(data: ([str], [[int]])):
    rules, numbers = data
    rules = set(rules)
    for number_set in numbers:
        yield process_single(number_set, rules)


def process2(data: ([str], [[int]])):
    rules, numbers = data
    rules = set(rules)
    for number_set in numbers:
        yield process_single2(number_set, rules)


def process_single(numbers, rules):
    pairs = get_ordered_permutations(numbers)
    pairs = list(map(lambda p: f"{p[1]}|{p[0]}", pairs))
    for pair in pairs:
        if pair in rules:
            return 0
    return numbers[(len(numbers) // 2)]


def process_single2(numbers, rules):
    middle = len(numbers) // 2
    was_fixed = False
    should_be_fixed = True
    while should_be_fixed:
        pairs = get_ordered_permutations(numbers)
        pairs = list(pairs)
        should_be_fixed = False
        for pair in pairs:
            if f"{pair[1]}|{pair[0]}" in rules:
                should_be_fixed = True
                was_fixed = True
                numbers[pair[2]] = pair[1]
                numbers[pair[3]] = pair[0]
                break

    return numbers[middle] if was_fixed else 0


def get_ordered_permutations(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            yield numbers[i], numbers[j], i, j


data = read_data()
print(data)
data = list(parse(data))
print(data)
data = process2(data)
print(data)
data = sum(data)
print(data)
