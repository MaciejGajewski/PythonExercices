import datetime


class Human(object):
    name = None
    gender = None
    birthdate = None

    def __getattr__(self, name):
        print(f"__getattr__ {name}")
        if name == 'age':
            return datetime.datetime.now() - self.birthdate
        else:
            return None

    def __getattribute__(self, name):
        print(f"__getattribute__ {name}")
        return object.__getattribute__(self, name)


h = Human()
h.birthdate = datetime.datetime(1984, 8, 20)
h.age = 28
print(h.age)
