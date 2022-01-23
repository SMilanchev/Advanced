class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.index = count

    def __iter__(self):
        self.index = self.count
        return self

    def __next__(self):
        val, self.index = self.index, self.index - 1
        if val == -1:
            raise StopIteration()

        return val


def main():
    res = list(countdown_iterator(3))
    print(f"{res} should be 3 2 1 0")

if __name__ == '__main__':
    main()