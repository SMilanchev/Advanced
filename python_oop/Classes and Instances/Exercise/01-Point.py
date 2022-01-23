from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        square_root = sqrt(pow((self.x - x), 2) + pow((self.y - 2), 2))
        return square_root


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))