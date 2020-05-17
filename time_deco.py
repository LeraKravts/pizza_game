import random
from functools import wraps


def time_deco(action: str):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if action == '+':
                print(f'Пицца будет у вас через {random.randint(10, 30)} минут')
            else:
                print(f'Заберите пиццу через {random.randint(10, 30)} минут')
            result = func(*args, **kwargs)
            return result
        return wrapper
    return inner
