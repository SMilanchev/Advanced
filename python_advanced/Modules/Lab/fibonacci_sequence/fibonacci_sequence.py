seq = [0, 1]


def create_sequence(n):
    global seq
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        seq = [0, 1]
        for i in range(2, n):
            seq.append(seq[-1] + seq[-2])
    return seq


def locate(n):
    if n in seq:
        return seq.index(n)
    else:
        return None


