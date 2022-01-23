# def squares(n):
#     for i in range(1, n + 1):
#         yield pow(i, 2)
#
#
# print(next(squares(3)))
# print(next(squares(3)))
# print(next(squares(4)))

squares = lambda n: (pow(n, 2) for n in range(1, n+1))