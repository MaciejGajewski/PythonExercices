class Something:
    X = 2

    def __init__(self, x: int = None):
        if x:
            self._some_x = x

    @property
    def x(self):
        return self._some_x * self.X

    @x.setter
    def x(self, x):
        self._some_x = x - 1


obj = Something(2)

print(Something.x)
print(obj.x)

obj.x = 2

print(Something.x)
print(obj.x)
