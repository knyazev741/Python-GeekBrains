class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell > other.cell:
            return self.cell - other.cell
        else:
            return "Невозможно выполнить вычитание объеектов, результат был был меньше 0"

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return self.cell // other.cell

    @staticmethod
    def make_order(obj, cell):
        count = 0

        if obj.cell % cell == 0:
            rows = obj.cell // cell
            result = ""

            for row in range(rows):

                for i in range(cell):
                    result += "*"

                count += 1
                if count == rows:
                    result += "."
                else:
                    result += "/n"

            return result

        else:
            rows = obj.cell // cell
            result = ""

            for row in range(rows):

                for i in range(cell):
                    result += "*"

                result += "/n"

            dop_row = obj.cell - rows*cell

            for item in range(dop_row):
                result += "*"

            result += "."

            return result


c1 = Cell(25)
c2 = Cell(12)

print(c1 - c2)
print(c2 - c1)
print(c1 * c2)
print(c1 / c2)
print(c1 + c2)
print(Cell.make_order(c1, 12))
print(Cell.make_order(c2, 3))
