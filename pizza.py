class BasePizza:
    cheese = 100
    sauce = 100


class Margarita(BasePizza):
    basil = 5
    tomatoes = 100

    def __str__(self):
        ingredients = (elem for elem in dir(Margarita) if elem[0] != '_')
        print('Margarira \N{tomato}', end=' ')
        for elem in ingredients:
            print(elem, end=' ')
        print('\N{black heart}')


class Pepperoni(BasePizza):
    pepperoni = 100

    def __str__(self):
        ingredients = (elem for elem in dir(Pepperoni) if elem[0] != '_')
        print('Pepperoni \N{beer mug}', end=' ')
        for elem in ingredients:
            print(elem,  end=' ')
        print('\N{black heart}')


class Hawaiian(BasePizza):
    chicken = 100
    pineapple = 50

    def __str__(self):
        ingredients = (elem for elem in dir(Hawaiian) if elem[0] != '_')
        print('Hawaiian \N{desert island}', end=' ')
        for elem in ingredients:
            print(elem, end=' ')
        print('\N{black heart}')
