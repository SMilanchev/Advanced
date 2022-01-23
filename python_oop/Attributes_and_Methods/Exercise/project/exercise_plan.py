from typing import ClassVar

from .customer import _get_next_id


class ExercisePlan:
    trainer_id: int
    equipment_id: int
    duration: int
    _counter: ClassVar[int] = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_hd = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration

        self.id = self._counter
        self.__class__._counter += 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        minutes = hours * 60
        return cls(trainer_id, equipment_id, minutes)

    get_next_id = _get_next_id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"



