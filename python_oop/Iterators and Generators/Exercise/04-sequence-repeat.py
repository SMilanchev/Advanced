class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.index = 0
        self.length = len(self.sequence)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        val, self.index = self.index, self.index + 1
        if val == self.number:
            raise StopIteration()
        val = val % self.length
        return self.sequence[val]


def main():
    res = ' '.join(list(sequence_repeat('abc', 5)))
    print(f"{res} should be abcab")

if __name__ == '__main__':
    main()