__author__ = "byteme8bit"
import random
import csv
import time
import Generators
import people_class


# def initialize_five():
#     for i in range(5):
#         yield Generators.intialize_person()


with open('testDB3.csv', mode='w') as csv_file:
    headers = ['name', 'bday', 'date']
    writer = csv.writer(csv_file, delimiter=',')

    writer.writerow(headers)
    for i in range(100):
        person = people_class.Person(Generators.pick_a_name(), Generators.create_bday())
        writer.writerow(person)
        # time.sleep(random.uniform(0, 1))
