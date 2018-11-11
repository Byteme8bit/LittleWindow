__author__ = "byteme8bit"
import random
import people_class


def pick_a_name():
    listed_names = [line.rstrip() for line in open('names')]
    random_name = random.choice(listed_names)
    return str(random_name)


def create_bday():
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    bday_month = random.choice(months)
    if bday_month in ['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec']:
        bday_day = random.randint(1, 31)

    if bday_month in ['Apr', 'Jun', 'Sept', 'Nov']:
        bday_day = random.randint(1, 30)

    if bday_month == 'Feb':
        bday_day = random.randint(1, 28)

    year = '19' + str(random.randint(57, 99))

    return str(bday_day) + ' ' + bday_month + ' ' + year


def intialize_person():
    people_class.Person(pick_a_name(), create_bday())


def group_by_month(person):
    pass


def generate_numbers(num):
    for i in range(num):
        yield random.randint(1, 100)


def generate_number():
    return random.randint(1, 100)
