class dictionary_iter:
    def __init__(self, dd: dict):
        self.dd = dd
        self.__data = iter(self.dd.items())

    def __iter__(self):
        self.__data = iter(self.dd.items())
        return self

    def __next__(self):
        val = next(self.__data)
        return val

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
