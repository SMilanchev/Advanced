from Testing.Lab import solution
import unittest
from unittest import mock


class SolutionTest(unittest.TestCase):
    def test_get_my_daily_to_to(self):
        mock_value = {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
        with unittest.mock.patch('solution.get_task', return_value=mock_value):
            daily_tasks = solution.my_daily_to_do()
        self.assertEqual(daily_tasks, [{
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        }])


if __name__ == '__main__':
    unittest.main()
