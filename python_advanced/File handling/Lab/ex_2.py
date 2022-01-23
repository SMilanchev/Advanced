with open('numbers.txt') as file:
    print(sum([int(line.rstrip()) for line in file.readlines()]))