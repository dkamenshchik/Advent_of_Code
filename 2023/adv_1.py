def read_data():
    with open('/home/kote/Downloads/input.txt', 'r') as f:
        data = f.read().splitlines()
    return data


name_to_digit_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def get_indexes(x: str, key: str):
    indexes = []
    index = 0
    while index < len(x):
        index = x.find(key, index)
        if index == -1:
            break
        indexes.append(index)
        index += len(key)
    return indexes


def replace(x: str):
    digits = []
    for key in name_to_digit_map:
        indexes_of_key = get_indexes(x, key)
        for index in indexes_of_key:
            digits.append((index, name_to_digit_map[key]))
    for value in name_to_digit_map.values():
        indexes_of_key = get_indexes(x, str(value))
        for index in indexes_of_key:
            digits.append((index, value))
    digits.sort(key=lambda x: x[0])
    return int(digits[0][1] + digits[-1][1])


data = read_data()
print(data)
data = list(map(replace, data))
print(data)
data = sum(data)
print(data)
