import re


def read_data():
    with open('/home/kote/Downloads/input.txt', 'r') as f:
        data = f.read()
    return data


def process(x: str):
    reg_filter_mul = r'mul\((\d{1,3}),(\d{1,3})\)'
    reg_filter_do = r"do\(\)"
    reg_filter_dont = r"don't\(\)"

    matches_mul = list(re.finditer(reg_filter_mul, x, re.IGNORECASE))
    matches_do = list(re.finditer(reg_filter_do, x, re.IGNORECASE))
    matches_dont = list(re.finditer(reg_filter_dont, x, re.IGNORECASE))

    result_do = [m.start() for m in matches_do]
    result_dont = [m.start() for m in matches_dont]
    intervals = []
    while result_dont:
        handled = False
        current = result_dont.pop(0)
        while result_do:
            if intervals:
                if current < intervals[-1][1]:
                    handled = True
                    break
            next = result_do.pop(0)
            if next > current:
                intervals.append((current, next))
                handled = True
                break
        if not handled:
            if intervals and current < intervals[-1][1]:
                continue
            intervals.append((current, len(x)))
    print(intervals)

    result_mul = [(int(m.group(1)), int(m.group(2)), m.start()) for m in matches_mul]

    print(result_mul)

    result_mul = [m[0] * m[1] for m in result_mul if not any([i[0] < m[2] < i[1] for i in intervals])]

    return result_mul


data = read_data()
print(data)
data = process(data)
print(data)
data = sum(data)
print(data)
