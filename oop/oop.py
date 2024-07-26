class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country
    @property
    def full_address(self):
        return f"{self.street}, {self.city}, {self.country}"
    
    def from_full_address(cls, full_address):
        parts = full_address.split(',')
        obj = cls(parts[0],parts[1],parts[2])
        return obj


address1 = Address('Gwangju', 'Seoul', 'South Korea')
address2 = Address('Maktab', 'Namangan', "O'zbekiston")

class Date:
    def __init__(self, year, month,day):
        self.year=year
        self.set_month(month)
        self.day=day
    
    @staticmethod
    def format(date, country = None):
        if country == "USA":
            return f"{date.month}/{date.day}/{date.year}"
        return f"{date.day}/{date.month}/{date.year}"

    def set_month(self, new_month):
        if new_month>12 or new_month<=0:
            raise ValueError("invalid month")
        self.month = new_month

date = Date(2024,7,4)
date2 = Date(2024,13,9)
