from abc import ABC, abstractmethod


class Car:
    pass


class BMW(Car):
    pass


class Mercedes(Car):
    pass


# class CarFactory:
#     def make_bmw(self):
#         return BMW()
#
#     def make_mercedes(self):
#         return Mercedes()
#
#     @staticmethod
#     def simple_car_factory(brand):
#         cars = {
#             'mercedes': Mercedes,
#             'bmw': BMW,
#         }
#         return cars[brand]()
class CarFactory(ABC):
    @abstractmethod
    def produce_car(self):
        pass


class BMWFactory(CarFactory):
    def produce_car(self):
        return BMW()


class MercedesFactory(CarFactory):
    def produce_car(self):
        return Mercedes()