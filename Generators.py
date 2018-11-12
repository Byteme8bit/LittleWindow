__author__ = "byteme8bit"
import random
import people_class
import time


def pick_a_name():
    first_names = [line.rstrip() for line in open('first_names')]
    last_names = [line.rstrip() for line in open('last_names')]
    random_name = random.choice(first_names)
    random_name += ' ' + random.choice(last_names)
    return random_name


def pick_full_name():
    listed_names = [line.rstrip() for line in open('names_full')]
    random_name = random.choice(listed_names)
    return random_name


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


def generate_uid(user, time):
    alpha_to_num_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
                           'e': 5, 'f': 6, 'g': 7, 'h': 8,
                           'i': 9, 'j': 10, 'k': 11, 'l': 12,
                           'm': 13, 'n': 14, 'o': 15, 'p': 16,
                           'q': 17, 'r': 18, 's': 19, 't': 20,
                           'u': 21, 'v': 22, 'w': 23, 'x': 24,
                           'y': 25, 'z': 26}

    shape_to_num_values = {'Circle': 27, 'Triangle': 28, 'Diamond': 29,
                           'Square': 30, 'Rectangle': 31, 'Octagon': 32,
                           'Oval': 33}

    split_full_name = user.name.lower().split()
    firstname = list(split_full_name[0])
    lastname = list(split_full_name[1])

    part_one_total = 0
    for char_f in firstname:
        part_one_total += alpha_to_num_values[char_f]
        part_one_total *= 2

    part_two_total = 0
    for char_l in lastname:
        part_two_total += alpha_to_num_values[char_l]
        part_two_total *= 3

    part_three_total = int(str(part_one_total) + str(part_two_total))
    part_four_total = part_three_total // shape_to_num_values[user.shape]
    return time - part_four_total
