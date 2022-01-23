from .animal_base import AnimalBase
from .employee_base import EmployeeBase
from .lion import Lion
from.tiger import Tiger
from .cheetah import Cheetah
from .keeper import Keeper
from .vet import Vet
from .caretaker import Caretaker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal: AnimalBase, price):
        if self.__budget >= price and self.__animal_capacity > 0:
            self.__budget -= price
            self.__animal_capacity -= 1
            self.animals.append(animal)
            animal_type = type(animal).__name__
            return f"{animal.name} the {animal_type} added to the zoo"
        elif self.__animal_capacity > 0:
            return 'Not enough budget'
        else:
            return 'Not enough space for animal'

    def hire_worker(self, worker: EmployeeBase):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            employee_type = type(worker).__name__
            return f"{worker.name} the {employee_type} hired successfully"
        return 'Not enough space for worker'

    def fire_worker(self, worker_name: EmployeeBase):
        prev_num_of_workers = len(self.workers)
        self.workers = [
            worker
            for worker in self.workers
            if worker.name != worker_name
        ]
        next_num_of_workers = len(self.workers)
        if prev_num_of_workers > next_num_of_workers:  # Care
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum([w.salary for w in self.workers])
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        total_due = sum([a.get_needs() for a in self.animals])
        if self.__budget >= total_due:
            self.__budget -= total_due
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def workers_status(self):
        total_workers_count = len(self.workers)
        keepers = [k.__repr__() for k in self.workers if isinstance(k, Keeper)]
        caretakers = [c.__repr__() for c in self.workers if isinstance(c, Caretaker)]
        vets = [v.__repr__() for v in self.workers if isinstance(v, Vet)]

        NEW_LINE = '\n'

        return f'''You have {total_workers_count} workers
----- {len(keepers)} Keepers:
{NEW_LINE.join(keepers)}
----- {len(caretakers)} Caretakers:
{NEW_LINE.join(caretakers)}
----- {len(vets)} Vets:
{NEW_LINE.join(vets)}'''

    def animals_status(self):
        total_animals_count = len(self.animals)
        lions = [l.__repr__() for l in self.animals if isinstance(l, Lion)]
        tigers = [t.__repr__() for t in self.animals if isinstance(t, Tiger)]
        cheetahs = [c.__repr__() for c in self.animals if isinstance(c, Cheetah)]

        NEW_LINE = '\n'

        return f'''You have {total_animals_count} animals
----- {len(lions)} Lions:
{NEW_LINE.join(lions)}
----- {len(tigers)} Tigers:
{NEW_LINE.join(tigers)}
----- {len(cheetahs)} Cheetahs:
{NEW_LINE.join(cheetahs)}'''

