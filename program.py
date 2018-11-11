__author__ = "byteme8bit"
import random
import csv
import time
import Generators
import people_class


# def initialize_five():
#     for i in range(5):
#         yield Generators.intialize_person()


with open('test7.csv', mode='w') as csv_file:
    headers = ['name', 'bday', 'date', 'shape', 'health']
    writer = csv.writer(csv_file, delimiter=',', quotechar='"')
    # list_of_people = list(initialize_five())
    person_one = people_class.Person(Generators.pick_a_name(), Generators.create_bday())
    person_two = people_class.Person(Generators.pick_a_name(), Generators.create_bday())
    person_three = people_class.Person(Generators.pick_a_name(), Generators.create_bday())
    person_four = people_class.Person(Generators.pick_a_name(), Generators.create_bday())
    person_five = people_class.Person(Generators.pick_a_name(), Generators.create_bday())
    print(person_one)
    # writer.writerow(headers)
    # writer.writerows(person_one)
    # writer.writerow(person_two.name, person_two.bday, person_two.created_time, person_two.shape, person_two.health)
    # writer.writerow(person_three.name, person_three.bday, person_three.created_time, person_three.shape,
    #                 person_three.health)
    # writer.writerow(person_four.name, person_four.bday, person_four.created_time, person_four.shape, person_four.health)
    # writer.writerow(person_five.name, person_five.bday, person_five.created_time, person_five.shape, person_five.health)
    # writer.writerow([Generators.pick_a_name(), Generators.create_bday(), time.time(), 'Hexagon'])
    # time.sleep(random.uniform(0, 1))
    # writer.writerow([Generators.pick_a_name(), Generators.create_bday(), time.time(), 'Diamond'])
    # time.sleep(random.uniform(0, 1))
    # writer.writerow([Generators.pick_a_name(), Generators.create_bday(), time.time(), 'Circle'])
    # time.sleep(random.uniform(0, 1))
    # writer.writerow([Generators.pick_a_name(), Generators.create_bday(),  time.time(), 'Square'])
    # time.sleep(random.uniform(0, 1))
    # writer.writerow([Generators.pick_a_name(), Generators.create_bday(), time.time(), 'Triangle'])
    #



    #
    # for i in range(0, 4):
    #     writer.writerow(list_of_people[i].name, list_of_people[i].bday)