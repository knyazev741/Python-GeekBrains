class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        total_income = 0

        for i in self._income.values():
            total_income += i

        print(total_income)


item = Position("Никита", "Князев", "Директор", 50000, 10000)

item.get_full_name()
item.get_total_income()
