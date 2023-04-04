from main import datefmt


class Student:
    UNIVERSITY = "MIT"

    def __init__(self, name, date_string, *args):
        self.name = name
        self.birthdate = datefmt(date_string)
