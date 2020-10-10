from time import sleep


class TrafficLight:
    __color = None

    def running(self):
        self.__color = "Red"
        print(self.__color)
        sleep(7)
        self.__color = "Yellow"
        print(self.__color)
        sleep(2)
        self.__color = "Green"
        print(self.__color)
        sleep(10)


item = TrafficLight()

item.running()
