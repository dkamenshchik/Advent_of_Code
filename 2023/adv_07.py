import itertools
from enum import Enum
from functools import reduce
import re
from operator import neg


class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


class Hand:
    _strength = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
        'J': 1,
    }

    def __init__(self, data):
        self.cards = data[0]
        self.bid = int(data[1])
        self.kind = self._kind()

    def __repr__(self):
        return f"{self.cards}-{self.bid}-{self.kind.name}"

    def __lt__(self, other):
        if self.kind.value == other.kind.value:
            return self._compare(other)
        return self.kind.value < other.kind.value

    def _kind(self):
        frequencies = {}
        for card in self.cards:
            if card not in frequencies:
                frequencies[card] = 0
            frequencies[card] += 1
        frequencies_list = list(frequencies.items())
        frequencies_list.sort(reverse=True, key=lambda x: x[1])
        if 'J' in frequencies and len(frequencies_list) > 1:
            j_frequency = frequencies.pop('J')
            if frequencies_list[0][0] == 'J':
                frequencies[frequencies_list[1][0]] += j_frequency
            else:
                frequencies[frequencies_list[0][0]] += j_frequency
        frequencies = list(frequencies.values())
        frequencies.sort(reverse=True)
        if frequencies[0] == 5:
            return HandType.FIVE_OF_A_KIND
        if frequencies[0] == 4:
            return HandType.FOUR_OF_A_KIND
        if frequencies[0] == 3:
            if frequencies[1] == 2:
                return HandType.FULL_HOUSE
            return HandType.THREE_OF_A_KIND
        if frequencies[0] == 2:
            if frequencies[1] == 2:
                return HandType.TWO_PAIR
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    def _compare(self, other):
        for l, r in zip(self.cards, other.cards):
            if self._strength[l] != self._strength[r]:
                return self._strength[l] < self._strength[r]
        return False


def parse_data(data):
    return list(map(lambda x: Hand(x.split()), data))


def calc(hands):
    hands.sort()
    print(hands)
    return reduce(lambda acc, curr: acc + (curr[0] + 1) * curr[1].bid, enumerate(hands), 0)


def read_data():
    with open('/home/kote/Downloads/input_7.txt', 'r') as f:
        data = f.read().splitlines()
    return data


data = read_data()
print(data)
hands = parse_data(data)
print(hands)
data = calc(hands)
print(data)
