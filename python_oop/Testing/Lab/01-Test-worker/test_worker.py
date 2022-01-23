from worker import Worker
from parameterized import parameterized
import unittest


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Simeon', 100, 42)

    def test_worker_is_initialized_properly(self):
        self.assertEqual(self.worker.name, 'Simeon')
        self.assertEqual(self.worker.salary, 100)
        self.assertEqual(self.worker.energy, 42)

    def test_energy_is_increased_when_rest(self):
        old_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy - old_energy, 1)

    @parameterized.expand([
        (-10, ),
        (-20, ),
        (0, ),
        (-42, ),
    ])
    def test_raises_exception_when_working_with_zero_or_negative_energy(self, energy):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_money_increased_after_work(self):
        worker_old_money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money - worker_old_money, self.worker.salary)

    def test_worker_energy_decreases_after_work(self):
        old_energy = self.worker.energy
        self.worker.work()
        self.assertEqual(self.worker.energy - old_energy, -1)

    def test_get_info(self):
        info = self.worker.get_info()
        self.assertEqual(info, 'Simeon has saved 0 money.')


if __name__ == '__main__':
    unittest.main()
