from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    __CAR_FUEL_INCREASE = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        total_fuel_needed = (self.fuel_consumption + self.__CAR_FUEL_INCREASE) * distance
        if total_fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= total_fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    __TRUCK_FUEL_INCREASE = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        total_fuel_needed = (self.fuel_consumption + self.__TRUCK_FUEL_INCREASE) * distance
        if total_fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= total_fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
