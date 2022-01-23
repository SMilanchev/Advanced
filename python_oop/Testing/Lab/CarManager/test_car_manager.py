from car_manager import Car


import unittest


class CarTest(unittest.TestCase):
    def setUp(self):
        self.car = Car("a", "b", 1, 4)

    def test_init(self):
        self.assertEqual(self.car.make, 'a')
        self.assertEqual(self.car.model, 'b')
        self.assertEqual(self.car.fuel_consumption, 1)
        self.assertEqual(self.car.fuel_capacity, 4)

    def test_make_empty_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.make = ''

    def test_model_empty_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.model = ''

    def test_fuel_consumption_zero_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.fuel_consumption = 0
        self.assertEqual(str(exc.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_consumption_negative_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = -1

    def test_fuel_capacity_zero_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.fuel_capacity = 0
        self.assertEqual(str(exc.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_capacity_negative_raises_exception(self):
        self.assertRaises(Exception, self.car.fuel_capacity, -1)

    def test_fuel_amount_negative_raises_exception(self):
        self.assertRaises(Exception, self.car.fuel_amount, 1)

    def test_refuel_negative_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.refuel(-42)

    def test_refuel_more_than_capacity(self):
        self.car.refuel(42)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_more_than_fuel(self):
        self.assertRaises(Exception, self.car.drive, 1000)

    def test_fuel_amount_after_drive(self):
        self.car.refuel(4)
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 3)

if __name__ == '__main__':
    unittest.main()
