class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.i = len(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.i -= 1
        if self.i >= 0:
            return self.iterable[self.i]
        raise StopIteration()


reversed_iterable = reverse_iter([1, 2, 3, 4])
for el in reversed_iterable:
    print(el)
