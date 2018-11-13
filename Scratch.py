import random

__author__ = "byteme8bit"
import time
import people_class
import Generators

person = people_class.Person(Generators.pick_a_name(), Generators.create_bday())

print(repr(person))


# curr_time = time.time()
# # print(len(str(one)))
# print(curr_time)
# print(int(str(curr_time)[:int(len(str(curr_time)) // 3)]))
