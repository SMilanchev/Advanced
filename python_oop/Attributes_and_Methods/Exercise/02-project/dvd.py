import datetime


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        status = 'rented' if self.is_rented else 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        month, year = cls.get_year_and_month(date)
        return cls(name, id, year, month, age_restriction)

    @staticmethod
    def get_year_and_month(date_string):
        d, m, y = list(map(int, date_string.split('.')))
        months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                  7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November',
                  12: 'December'
                  }
        month_name = months[m]
        year_number = y
        return month_name, year_number

