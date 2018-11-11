__author__ = "byteme8bit"
import people_class
import Generators

# listed_names = [line.rstrip() for line in open('names')]
# print(listed_names)
# with open('names') as names:
#     for i in range(100):
#         next = names.readlines()
#         print(next)
#         name = next[:-2]
#         print(name)
#         listed_names.append(name)
#     # for name in listed_names:
#     #     name = name[:-2]
#
#     # data = names.readline()
#     print(listed_names)

person_one = people_class.Person(Generators.pick_a_name(), Generators.create_bday())
person_two = people_class.Person(Generators.pick_a_name(), Generators.create_bday())
person_three = people_class.Person(Generators.pick_a_name(), Generators.create_bday())
person_four = people_class.Person(Generators.pick_a_name(), Generators.create_bday())
person_five = people_class.Person(Generators.pick_a_name(), Generators.create_bday())
#
print(person_one)
#     print(var)
# print(person_two)
# print(person_three)
# print(person_four)
# print(person_five)