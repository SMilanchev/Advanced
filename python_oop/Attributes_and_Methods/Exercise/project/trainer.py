from typing import ClassVar

from .customer import _get_next_id


class Trainer:
    name: str
    _counter: ClassVar[int] = 1

    def __init__(self, name: str):
        self.name = name

        self.id = self._counter
        self.__class__._counter += 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    get_next_id = _get_next_id