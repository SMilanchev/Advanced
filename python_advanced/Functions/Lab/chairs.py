# from itertools import combinations
#
#
# print(*[f"{', '.join(el)}" for el in list(combinations(names, n))], sep='\n')
#


def calc_comb(names, n, combs=[]):
    if len(combs) == n:
        print(', '.join(combs))
        return

    for i in range(len(names)):
        name = names[i]
        combs.append(name)
        calc_comb(names[i+1:], n, combs)
        combs.pop()


names = input().split(', ')
n = int(input())
calc_comb(names, n)
