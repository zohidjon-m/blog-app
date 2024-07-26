import datetime
class Person:
    def __init__(self, name, angel, email):
        self.name = name
        self.angel = angel
        self.email = email

    def get_info(self):
        return f"name: {self.name}, age: {self.age}, email: {self.email}"

    def birth_day(self):
        if hasattr(self, "_age"):
            return self._age

        today = datetime.date.today()
        birthday = today.year - self.age

        return f"born in {birthday} "

person1 = Person('Anva',23,'fiji@gmail.com')


