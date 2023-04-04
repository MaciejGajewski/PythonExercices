class AB(object):
    brothers = []

    def __init__(self, name):
        self.name = name


a = AB('Richard')
b = AB('Eilly')
a.brothers.append('John')

print(a.name, a.brothers, b.name, b.brothers)