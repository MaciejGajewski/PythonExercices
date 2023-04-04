from datetime import datetime
from constants import DEFAULT_DATE_FORMAT


def datefmt(date_string):
    return datetime.strptime(date_string, DEFAULT_DATE_FORMAT)


s = Student('Mary', '1981-7-23')
