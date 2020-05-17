class BasePizza:
    def __init__(self, sauce='tomatoes', cheese=True):
        self.name = self.__class__.__name__
        self.sauce = sauce
        self.cheese = cheese


class Margarita(BasePizza):
    def __init__(self, tomatoes=True, basil=True):
        super().__init__()
        self.tomatoes = tomatoes
        self.basil = basil


print(Margarita(tomatoes=True, basil=True).__dict__)
