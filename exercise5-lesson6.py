class Stationery:

    def __init__(self, title="Канцелярская принадлежность"):
        self.title = title

    def draw(self):
        print(self.title)
        print("Запуск отрисовки отрисовку")


class Pen(Stationery):

    def draw(self):
        print("Начинаем рисовать ручкой")


class Pencil(Stationery):

    def draw(self):
        print("Начинаем рисовать карандашом")


class Handle(Stationery):

    def draw(self):
        print("Начинаем рисовать маркером")


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
