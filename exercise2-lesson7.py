class Coat:
    def __init__(self, v):
        self.v = v

    def sum_(self):
        return self.v/6.5 + 0.5


class Suit:
    def __init__(self, h):
        self.h = h

    def sum_(self):
        return 2*self.h + 0.3


class Clothes:
    def __init__(self, name=None):
        self.name = name

    @staticmethod
    def result(v, h):
        return Coat(v).sum_() + Suit(h).sum_()


item = Clothes()
print(item.result(10, 5))
