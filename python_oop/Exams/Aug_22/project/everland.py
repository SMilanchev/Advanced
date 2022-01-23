from .rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms: list = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses
            total_consumption += room.room_cost
        total_consumption *= 30
        return f"Monthly consumption: {total_consumption}$."

    def pay(self):
        strings = []
        rooms_to_remove = []
        for room in self.rooms:
            monthly_expenses = (room.expenses + room.room_cost) * 30
            if room.budget >= monthly_expenses:
                room.budget -= monthly_expenses
                strings.append(f"{room.family_name} paid {monthly_expenses}$ and have {room.budget}$ left.")
            else:
                strings.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                rooms_to_remove.append(room)

        for r in rooms_to_remove:
            self.rooms.pop(self.rooms.index(r))

        return '\n'.join(strings)

    def status(self):
        s = ""
        all_people_in_the_hotel = sum([room.members_count for room in self.rooms])
        s += f'Total population: {all_people_in_the_hotel}\n'
        for room in self.rooms:
            room.calculate_expenses()
            room_name = room.family_name
            members = room.members_count
            current_budget = room.budget
            expenses = room.expenses
            s += f'{room_name} with {members} members. Budget: {current_budget}$, Expenses: {expenses}$\n'
            for n, child in (room.children, 1):
                cost_for_one_month = child.cost * 30
                s += f'--- Child {n} monthly cost: {cost_for_one_month}$\n'
            cost_of_all_appliances_for_one_month = sum([r.cost for r in room.appliances]) * 30
            s += f'--- Appliances monthly cost: {cost_of_all_appliances_for_one_month}$\n'

        return s
