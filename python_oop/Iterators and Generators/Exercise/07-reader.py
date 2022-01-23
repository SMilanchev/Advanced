def read_next(*args):
    for el in args:
        for e in el:
            yield e

for item in read_next('string', (2,), {'m': 1, 'd': 3, 'p': 4}):
    print(item, end='')
