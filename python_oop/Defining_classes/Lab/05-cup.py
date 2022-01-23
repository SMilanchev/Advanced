class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, mililiters):
        new_quantity = self.quantity + mililiters
        if new_quantity <= self.size:
            self.quantity = new_quantity

        return self.quantity

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
cup.fill(30)
cup.fill(10)
print(cup.status())