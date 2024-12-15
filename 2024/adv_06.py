import itertools
from collections import Counter
from itertools import pairwise

from numpy import sign


def read_data():
    with open('/home/kote/Downloads/input.txt', 'r') as f:
        data = f.read().splitlines()
    return data


def process(grid: [str]):
    x, y, dir = get_start(grid)
    return len(set(visited(grid, x, y, dir)))


def process2(grid: [str]):
    x, y, dir = get_start(grid)
    to_replace = (set(visited(grid, x, y, dir)))
    possible_loops = 0
    for (xr, yr) in to_replace:
        grid_copy = grid.copy()
        grid_copy[xr] = grid_copy[xr][:yr] + '#' + grid_copy[xr][yr + 1:]
        possible_loops += has_loop(grid_copy, x, y, dir)
    return possible_loops


def has_loop(grid, x, y, dir):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    right_turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    visited = {(x, y, dir)}
    while in_bounds(grid, x, y):
        dx, dy = directions[dir]
        x += dx
        y += dy
        if in_bounds(grid, x, y) and grid[x][y] == '#':
            dir = right_turns[dir]
            x -= dx
            y -= dy
        if (x, y, dir) in visited:
            return True
        visited.add((x, y, dir))
    return False


def get_start(grid):
    for (x, line) in enumerate(grid):
        for (y, ch) in enumerate(line):
            if ch in ['^', 'v', '<', '>']:
                return x, y, ch


def visited(grid, x, y, dir):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    right_turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    while in_bounds(grid, x, y):
        yield x, y
        dx, dy = directions[dir]
        x += dx
        y += dy
        if in_bounds(grid, x, y) and grid[x][y] == '#':
            dir = right_turns[dir]
            x -= dx
            y -= dy


def in_bounds(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])


data = read_data()
print(data)
data = process2(data)
print(data)
