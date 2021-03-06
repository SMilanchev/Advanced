from dataclasses import dataclass


@dataclass()
class Room:
    number: int
    capacity: int
    guests: int = 0
    is_taken: bool = False

    # def __init__(self, number: int, capacity: int):
    #     self.number = number
    #     self.capacity = capacity
    #     self.guests = 0
    #     self.is_taken = False

    def take_room(self, people):
        if self.is_taken or people > self.capacity:
            return f"Room number {self.number} cannot be taken"
        else:
            self.is_taken = True
            self.guests += people

    def free_room(self):
        if self.is_taken:
            self.guests = 0
            self.is_taken = False
            return
        return f"Room number {self.number} is not taken"