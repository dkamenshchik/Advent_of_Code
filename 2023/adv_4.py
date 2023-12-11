import itertools
from functools import reduce
import re
from operator import neg


def read_data():
    with open('/home/kote/Downloads/input_4.txt', 'r') as f:
        data = f.read().splitlines()
    return data


reg = re.compile('\d+|[^.]')


def parse_num(s: str):
    return list(map(int, filter(None, s.split(' '))))


def parse(data: str):
    card = data.split(':')
    num = int(card[0].split(' ')[-1])
    data = card[1].split('|')
    return num, parse_num(data[0]), parse_num(data[1]), 1


def calc_card(card):
    win = set(card[1])
    cnt = len(list(filter(lambda x: x in win, card[2])))
    return cnt


def calc(cards):
    for i in range(len(cards)):
        cnt = calc_card(cards[i])
        for j in range(cards[i][0], cards[i][0] + cnt):
            cards[j][3] += cards[i][3]
    return cards


data = read_data()
print(data)
data = list(map(lambda x: list(parse(x)), data))
print(data)
data = calc(data)
print(data)
data = sum(map(lambda x: x[3], data))
print(data)
