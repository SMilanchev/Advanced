# import random
#
#
# class EndlessIterator:
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         i = random.randint(0, 100)
#         if i == 42:
#             raise StopIteration()
#         return i
#
#
# iterator = EndlessIterator()
# for num in iterator:
#     print(num)
#
# def generator():
#     print('before 1')
#     yield 1
#     print('before 2')
#     yield 2
#     print('before 3')
#     yield 3
#
# iterator = generator()
# print(next(iterator))
# print('---')
# print(next(iterator))
# print('---')
# print(next(iterator))
# print('---')
#
# def generator(string: str):
#     for c in string:
#         if c in 'aeiouy':
#             yield c
#
#
# my_string = generator('Literatori')
# for char in my_string:
#     print(char)

reverse_text = lambda s: (el for el in reversed(s))
for char in reverse_text('step'):
    print(char)