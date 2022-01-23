from .customer import Customer
from .dvd import DVD


class MovieWorld:
    _DVD_CAPACITY = 15
    _CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @classmethod
    def dvd_capacity(cls):
        return cls._DVD_CAPACITY

    @classmethod
    def customer_capacity(cls):
        return cls._CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd_ids = [dvd.id for dvd in self.dvds]
        current_customer = ""
        current_dvd = ""
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                current_dvd = self.dvds[self.dvds.index(dvd)]
                break
        for customer in self.customers:
            if customer.id == customer_id:
                current_customer = self.customers[self.customers.index(customer)]
                break
        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"
        elif current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"
        elif current_dvd.is_rented:
            return "DVD is already rented"
        else:
            current_dvd.is_rented = True
            current_customer.rented_dvds.append(current_dvd)
            return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer = ""
        current_dvd = ""
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                current_dvd = self.dvds[self.dvds.index(dvd)]
                break
        for customer in self.customers:
            if customer.id == customer_id:
                current_customer = self.customers[self.customers.index(customer)]
                break

        if current_dvd in current_customer.rented_dvds:
            current_dvd.is_rented = False
            current_customer.rented_dvds.remove(current_dvd)
            return f"{current_customer.name} has successfully returned {current_dvd.name}"
        else:
            return f"{current_customer.name} does not have that DVD"

    def __repr__(self):
        customers = list(map(str, self.customers))
        dvds = list(map(str, self.dvds))
        return '\n'.join(customers + dvds)

