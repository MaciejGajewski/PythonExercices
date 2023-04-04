import random


def func(type_='s'):
    if type_ == 's':
        return 'Mark'
    elif type_ == 'i':
        return random.randint(0, 1000)


def dec(func, type_):
    x = 8

    def wrapper():
        value = func(type_)
        if isinstance(value, int):
            return value * x
        elif isinstance(value, str):
            return "Hi " + value

    return wrapper


print(dec(func, 'i')())

