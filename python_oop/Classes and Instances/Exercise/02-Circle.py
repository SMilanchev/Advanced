class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        area = pow(self.radius, 2) * Circle.pi
        return round(area, 2)

    def get_circumference(self):
        circumference = Circle.pi * (2 * self.radius)
        return round(circumference, 2)


circle = Circle(12)
print(circle.get_area())
print(circle.get_circumference())