from typing import ClassVar


@classmethod
def _get_next_id(cls):
    return cls._counter


def generic_init(self, *args):
    attributes = self.__annotations__

    for attr, value in zip(attributes, args):
        if attr == '_counter':
            continue
        setattr(self, attr, value)

    self.id = self.__class__._counter
    self.__class__._counter += 1


class Customer:
    name: str
    address: str
    email: str
    _counter: ClassVar[int] = 1

    __init__ = generic_init

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    get_next_id = _get_next_id


c = Customer("n", "pk", "gosho_98")
print(c.get_next_id())

Customer = dataclass({
    'name': 'str',
    'address': 'str',
    'email': 'str'
}, "Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}")

