def integers():
    i = 1
    while True:
        yield i

        i += 1


def halves():
    for n in integers():
        yield n / 2


def take(count, seq):
    return [x for _, x in zip(range(count), seq)]


def solution():
    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))