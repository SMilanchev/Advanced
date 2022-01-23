from .animal import Bird
from ..food import Food, Meat


class Owl(Bird):
    _FOOD_PREFERENCES = (Meat,)
    _WEIGHT_GAIN_PER_FOOD = 0.25

    def make_sound(self):
        return 'Hoot Hoot'


class Hen(Bird):
    _FOOD_PREFERENCES = None
    _WEIGHT_GAIN_PER_FOOD = 0.35

    def make_sound(self):
        return 'Cluck'
