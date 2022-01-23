from .dough import Dough
from .topping import Topping
from collections import defaultdict


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = defaultdict(float)

    def add_topping(self, topping: Topping):
        if self.__toppings_capacity == len(self.__toppings):
            raise ValueError("Not enough space for another topping")
        else:
            self.__toppings[topping.topping] += topping.weight

    def calculate_total_weight(self):
        return sum(self.__toppings.items()) + self.__dough.weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, new_dough):
        self.__dough = new_dough

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, new_capacity):
        self.__toppings_capacity = new_capacity

    @property
    def toppings(self):
        return dict(self.__toppings)

    @toppings.setter
    def toppings(self, new_toppings):
        self.__toppings = defaultdict(float, new_toppings)