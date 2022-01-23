perm = [0] * 3
print(perm)


def permutation(sequence, idx=0):
    if idx == len(sequence):
        print(perm)
        return
    for n in sequence:
        perm[idx] = n
        permutation(sequence[idx:], idx+1)


permutation([1, 2, 3], 0)