# def genrange(start, end):
#     while start <= end:
#         yield start
#         start += 1
#
#
# print(list(genrange(1, 10)))

genrange = lambda x, y: (i for i in range(x, y+1))
print(list(genrange(1, 10)))