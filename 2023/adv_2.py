from functools import reduce


def read_data():
    with open('/home/kote/Downloads/input_2.txt', 'r') as f:
        data = f.read().splitlines()
    return data


def parse_cast(cast: str):
    cast = cast.strip()
    cubes = cast.split(',')
    cubes = list(map(lambda x: x.strip(), cubes))
    cubes = list(map(lambda x: x.split(' '), cubes))
    cubes = list(map(lambda x: (x[1], int(x[0])), cubes))
    cubes = dict(cubes)
    return cubes


# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
def parse_data(data: list[str]):
    parsed_data = []
    for line in data:
        parts = line.split(':')
        game_id = int(parts[0].split(' ')[1])
        casts = parts[1].split(';')
        casts = list(map(parse_cast, casts))
        game = {
            'id': game_id,
            'casts': casts
        }
        parsed_data.append(game)
    return parsed_data


constraint = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def match_constraint(game: list[dict]):
    for cast in game['casts']:
        for key in constraint:
            if key in cast and cast[key] > constraint[key]:
                return False
    return True


def get_set_power(game: dict):
    max_set = reduce(lambda acc, curr: {
        'red': max(acc.get('red', 0), curr.get('red', 0)),
        'green': max(acc.get('green', 0), curr.get('green', 0)),
        'blue': max(acc.get('blue', 0), curr.get('blue', 0))
    }, game['casts'])
    return max_set['red'] * max_set['green'] * max_set['blue']


data = read_data()
print(data)
data = parse_data(data)
print(data)

# data = list(filter(match_constraint, data))
# print(data)
# data = list(map(lambda x: x['id'], data))
# print(data)
# data = sum(data)
# print(data)

data = list(map(get_set_power, data))
print(data)
data = sum(data)
print(data)

adv_2.py
