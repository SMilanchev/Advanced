from .main_dish import MainDish


class Salmon(MainDish):
    SALMON_GRAMS = 22

    def __init__(self, name: str, price: float):
        super().__init__(name, price, self.__class__.SALMON_GRAMS)

