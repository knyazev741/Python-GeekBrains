class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        print(self._length*self._width*25*5 // 1000, "Т")


item = Road(20, 5000)

item.mass()
