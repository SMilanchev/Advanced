from typing import List
from .customer import Customer
from .trainer import Trainer
from .equipment import Equipment
from .subscription import Subscription
from .exercise_plan import ExercisePlan


class Gym:
    customers: List[Customer]
    trainers: List[Trainer]
    equipment: List[Equipment]
    plans: List[ExercisePlan]
    subscriptions: List[Subscription]

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = [f"{s}" for s in self.subscriptions if s.id == subscription_id]
        customer = [f"{c}" for c in self.customers if c.id == subscription_id]
        trainer = [f"{t}" for t in self.trainers if t.id == subscription_id]
        equipment = [f"{e}" for e in self.equipment if e.id == subscription_id]
        plan = [f"{p}" for p in self.plans if p.id == subscription_id]

        return '\n'.join(subscription + customer + trainer + equipment + plan)

