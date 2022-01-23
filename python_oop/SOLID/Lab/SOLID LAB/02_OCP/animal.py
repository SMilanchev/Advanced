from abc import ABC, abstractmethod

from typing import List


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Dog(Animal):
    def make_sound(self):
        return 'bark'


class Tiger(Animal):
    def make_sound(self):
        return 'rawr!!!'


class Chicken(Animal):
    def make_sound(self):
        return 'chick-chirik'


def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat(), Tiger(), Chicken()]
animal_sound(animals)
