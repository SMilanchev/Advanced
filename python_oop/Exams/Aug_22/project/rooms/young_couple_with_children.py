from .room import Room
from ..appliances.tv import TV
from ..appliances.fridge import Fridge
from ..appliances.laptop import Laptop
from ..people.child import Child


class YoungCoupleWithChildren(Room):
    room_cost = 30
    children = []

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children: Child):
        budget = salary_one + salary_two
        members_count = 2 + len(children)
        self.children = list(children)
        for _ in range(members_count):
            self.appliances.append(TV())
            self.appliances.append(Fridge())
            self.appliances.append(Laptop())
        super().__init__(family_name, budget, members_count)
        expenses = self.appliances + self.children
        self.calculate_expenses(*expenses)
