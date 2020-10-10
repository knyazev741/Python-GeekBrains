class Car:

    def __init__(self, speed=0, color=None, name=None, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула на {direction}")

    def show_speed(self):
        print(f"Скорость автомобиля {self.speed} км/ч")


class TownCar(Car):

    def show_speed(self):
        super().show_speed()

        if self.speed > 60:
            print("Автомобиль превышает скорость!")


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()

        if self.speed > 40:
            print("Автомобиль превышает скорость!")


town = TownCar(speed=90, name="Volvo", color="Green")
work = WorkCar(speed=50, name="BMW", color="Black")
work2 = WorkCar(speed=40, name="LADA2110", color="Yellow")

print(town.speed, town.color, town.is_police, town.name)
town.go()
town.show_speed()
town.turn("право")
town.stop()

print(work.speed, work.color, work.is_police, work.name)
work.go()
work.show_speed()
work.turn("лево")
work.stop()

print(work2.speed, work2.color, work2.is_police, work2.name)
work2.go()
work2.show_speed()
work2.turn("лево")
work2.stop()
