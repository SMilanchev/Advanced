class vowels:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index <= len(self.string) - 1:
            c = self.string[self.index]
            self.index += 1
            if self.is_vowel(c):
                return c
        raise StopIteration


    @staticmethod
    def is_vowel(c):
        vowels = 'aeiuyo'
        return c.lower() in vowels


iterator =vowels('Abcedifuty0o')
for char in iterator:
    print(char)