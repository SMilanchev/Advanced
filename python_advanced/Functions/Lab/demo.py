def combination(names, n, combs=[]):
    if len(combs) == n:
        print(combs)
        return
    for i in range(len(names)):
        name = names[i]
        combs.append(name)
        combination(names[i+1:], n, combs)
        combs.pop()


names = ['peter', 'george', 'ivan']
n = 2
combination(names, n)