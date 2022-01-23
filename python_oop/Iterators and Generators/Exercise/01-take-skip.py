from datetime import datetime
import sys
from typing import Iterable


class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.repeat = count
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        val, self.index = self.index, self.index + self.step
        gen_so_far = (val/self.step)
        if gen_so_far == self.repeat:
            raise StopIteration()
        return val


itera = take_skip(2, 6)
print(next(itera))
iterb = take_skip(2, 6)
print(next(iterb))