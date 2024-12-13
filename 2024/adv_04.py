from collections import Counter
from itertools import pairwise

from numpy import sign


def read_data():
    with open('/home/kote/Downloads/input.txt', 'r') as f:
        data = f.read().splitlines()
    return data


def process(grid: [str]):
    for (x, line) in enumerate(grid):
        for (y, ch) in enumerate(line):
            if ch == 'X':
                yield sum(check(grid, x, y))


def check(grid: [str], x: int, y: int):
    for line in snow_iter(grid, x, y):
        if line == "XMAS":
            yield 1
    yield 0


def snow_iter(grid: [str], x: int, y: int):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    distance = len("XMAS")
    for (dx, dy) in directions:
        line = ""
        for i in range(distance):
            nx = x + i * dx
            ny = y + i * dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[nx]):
                break
            line += grid[nx][ny]
        yield line


def process2(grid: [str]):
    for (x, line) in enumerate(grid):
        for (y, ch) in enumerate(line):
            if ch == 'A':
                yield check2(grid, x, y)


def check2(grid: [str], x: int, y: int):
    directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    for (dx, dy) in directions:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[nx]):
            return 0
    l = grid[x - 1][y - 1] + grid[x + 1][y + 1]
    r = grid[x - 1][y + 1] + grid[x + 1][y - 1]
    combos = ["SM", "MS"]
    if l in combos and r in combos:
        return 1
    return 0


data = read_data()
print(data)
data = process2(data)
print(data)
data = sum(data)
print(data)
