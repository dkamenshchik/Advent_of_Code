import itertools
import math
from enum import Enum
from functools import reduce
import re
from operator import neg


def find_start(data):
    line_with_start = next(line for line in data if 'S' in line)
    return line_with_start.index('S'), data.index(line_with_start)


def get_neighbours_for_start(current, data):
    result = []
    x, y = current
    if data[y - 1][x] in ['F', '|', '7']:
        result.append((x, y - 1))
    if data[y + 1][x] in ['L', '|', 'J']:
        result.append((x, y + 1))
    if data[y][x + 1] in ['7', '-', 'J']:
        result.append((x + 1, y))
    if data[y][x - 1] in ['F', '-', 'L']:
        result.append((x - 1, y))
    return result if len(result) == 2 else [(-1, -1)]


def get_neighbours(current, data):
    x, y = current
    match data[y][x]:
        case 'F':
            return [(x, y + 1), (x + 1, y)]
        case '|':
            return [(x, y - 1), (x, y + 1)]
        case 'L':
            return [(x, y - 1), (x + 1, y)]
        case '-':
            return [(x - 1, y), (x + 1, y)]
        case 'J':
            return [(x - 1, y), (x, y - 1)]
        case '7':
            return [(x, y + 1), (x - 1, y)]

    return -1, -1


def get_color(prev_color, prev, curr, data):
    curr_s = data[curr[1]][curr[0]]
    match [data[prev[1]][prev[0]], data[curr[1]][curr[0]]]:
        # F
        case ['L', 'F'] | ['|', 'F'] | ['J', 'F']:
            return prev_color, curr_s
        case ['-', 'F'] | ['7', 'F']:
            return int(not prev_color), curr_s
        # |
        case [_, '|']:
            return prev_color, curr_s
        # L
        case ['-', 'L'] | ['|', 'L'] | ['7', 'L'] | ['F', 'L']:
            return prev_color, curr_s
        case ['J', 'L']:
            return int(not prev_color), curr_s
        # -
        case ['L', '-'] | ['-', '-'] | ['7', '-']:
            return prev_color, curr_s
        case ['F', '-'] | ['J', '-']:
            return int(not prev_color), curr_s
        # J
        case ['-', 'J'] | ['L', 'J']:
            return int(not prev_color), curr_s
        case ['F', 'J'] | ['7', 'J'] | ['|', 'J']:
            return prev_color, curr_s
        # 7
        case ['-', '7'] | ['L', '7'] | ['J', '7'] | ['|', '7']:
            return prev_color, curr_s
        case ['F', '7']:
            return int(not prev_color), curr_s
    return -1


def reveal_start(start, neighbours):
    x, y = start
    neighbours[0] = (neighbours[0][0] - x, neighbours[0][1] - y)
    neighbours[1] = (neighbours[1][0] - x, neighbours[1][1] - y)
    match neighbours:
        case [(0, -1), (0, 1)]:
            return '|'
        case [(-1, 0), (1, 0)]:
            return '-'
        case [(0, -1), (1, 0)]:
            return 'L'
        case [(0, 1), (-1, 0)]:
            return '7'
        case [(0, -1), (-1, 0)]:
            return 'J'
        case [(0, 1), (1, 0)]:
            return 'F'
    return 'S'


def trace_loop(data):
    vertices = {}
    start = find_start(data)
    start_neighbours = get_neighbours_for_start(start, data)
    prev = [start, start]
    start_s = reveal_start(start, start_neighbours)
    data[start[1]] = data[start[1]].replace('S', start_s)
    queue = [start]
    vertices[start] = (1, start_s)
    while queue:
        current = queue.pop(0)
        for neighbour in get_neighbours(current, data):
            if neighbour not in prev:
                if neighbour in vertices:
                    return vertices
                vertices[neighbour] = get_color(vertices[current][0], current, neighbour, data)
                queue.append(neighbour)
            else:
                prev.remove(neighbour)
        prev.append(current)
    return vertices


def read_data():
    with open('/home/kote/Downloads/input_10.txt', 'r') as f:
        data = f.read().splitlines()
    return data


def get_all_neighbours(current):
    x, y = current
    return [
        (x, y),
        (x, y - 1),
        (x, y + 1),
        (x + 1, y),
        (x - 1, y)
    ]


def fill(current, cells, loop):
    neighbours = set()
    loop_cells = set()
    close_neighbour = None
    neighbours.add(current)
    queue = [current]
    while queue:
        current = queue.pop(0)
        curr_neighbours = get_all_neighbours(current)
        for neighbour in curr_neighbours:
            if neighbour in cells or neighbour in loop:
                if neighbour not in loop:
                    if neighbour not in neighbours:
                        neighbours.add(neighbour)
                        queue.append(neighbour)
                else:
                    close_neighbour = current
                    loop_cells.add(neighbour)
        if loop_cells:
            break
    return neighbours, close_neighbour, loop_cells


def classify(neighbours, close_neighbour, loop_cells, loop, gray, orange):
    loop_cell = loop_cells.pop()
    position = (close_neighbour[0] - loop_cell[0], close_neighbour[1] - loop_cell[1])
    (color, loop_cell_type) = loop[loop_cell]
    match position:
        case (0, -1):
            match loop_cell_type:
                case '-' | '7':
                    (orange if color == 1 else gray).update(neighbours)
                case 'F':
                    (gray if color == 1 else orange).update(neighbours)
        case (0, 1):
            match loop_cell_type:
                case 'J':
                    (orange if color == 1 else gray).update(neighbours)
                case 'L' | '-':
                    (gray if color == 1 else orange).update(neighbours)
        case (-1, 0):
            match loop_cell_type:
                case 'L' | '|' | 'F':
                    (gray if color == 1 else orange).update(neighbours)
        case (1, 0):
            match loop_cell_type:
                case '7' | '|' | 'J':
                    (orange if color == 1 else gray).update(neighbours)


def calculate(data, loop):
    cells_to_classify = set()
    for (y, row) in enumerate(data):
        for (x, col) in enumerate(row):
            if (x, y) not in loop:
                cells_to_classify.add((x, y))
    cells_to_classify_total = list(cells_to_classify)
    #print(cells_to_classify)
    gray, orange = set(), set()
    while cells_to_classify:
        current = cells_to_classify.pop()
        neighbours, close_neighbour, loop_cells = fill(current, cells_to_classify_total, loop)
        classify(neighbours, close_neighbour, loop_cells, loop, gray, orange)
        cells_to_classify -= neighbours
    #print(gray)
    #print(orange)
    return len(gray) if (0, 0) in orange else len(orange)


data = read_data()
print(data)
loop = trace_loop(data)
print(loop)
data = calculate(data, loop)
print(data)
