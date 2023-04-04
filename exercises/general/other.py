# 1

a = [1, 2, 3]
b = a
del a

# b = ?

# 2
MULTIPLIER = 3
a = lambda x, y: (x * MULTIPLIER) / y

a(2, 3)

# 3


class Human:
    name = "bla"
    _name = "blabla"
    __name = "dupa"


h = Human()

h.name
h._name
h.__name

# 4

# "".join is a lot faster then s += string
# https://waymoot.org/home/python_string/

# 5


class Human:
    def __setattr__(self, key, value):
        if key == "gender" and value in ('male', 'female'):
            self.gender = value
        else:
            raise AttributeError("Must be male or female")


h = Human()
h.name = "Mary"
h.gender = "female"


# 6
a = ['orange', 'apple', 'banana']
b = a
a = ['tomato', 'cucumber', 'carrot']

b

