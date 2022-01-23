from typing import ClassVar

from .customer import _get_next_id


class Subscription:
    date: str
    customer_id: int
    trainer_id: int
    exercise_id: int
    _counter: ClassVar[int] = 1

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id

        self.id = self._counter
        self.__class__._counter += 1

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

    get_next_id = _get_next_id

