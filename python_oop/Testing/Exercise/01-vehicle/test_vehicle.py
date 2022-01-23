from vehicle import Car
from vehicle import Truck
import unittest


class VehicleTest(unittest.TestCase):
    def setUp(self):
        self.car = Car(1, 1)
        self.truck = Truck(1, 1)

    def test_vehicles_are_initialized_properly(self):
        self.assertEqual(self.car.fuel_consumption, 1)
        self.assertEqual(self.car.fuel_quantity, 1)
        self.assertEqual(self.truck.fuel_consumption, 1)
        self.assertEqual(self.truck.fuel_quantity, 1)

    def test_refuel_increases_fuel_quantity(self):
        self.car.refuel(5)
        self.assertEqual(self.car.fuel_quantity, 6)
        self.truck.refuel(5)
        self.assertEqual(self.truck.fuel_quantity, 5.75)

    def test_drive_vehicles_with_enough_fuel(self):
        self.car.refuel(5)
        self.car.drive(1)
        self.assertEqual(self.car.fuel_quantity, 4.1)
        self.truck.refuel(5)
        self.truck.drive(1)
        self.assertEqual(self.truck.fuel_quantity, 3.15)

    def test_drive_vehicles_with_not_enough_fuel(self):
        self.car.drive(1)
        self.assertEqual(self.car.fuel_quantity, 1)
        self.truck.drive(1)
        self.assertEqual(self.truck.fuel_quantity, 1)

if __name__ == '__main__':
    unittest.main()

# def test_vehicles_can_be_instantiated(self):
#     Car(3, 4)
#     Truck(3, 4)
