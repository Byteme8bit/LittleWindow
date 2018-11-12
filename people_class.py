__author__ = "byteme8bit"
import random
import Generators
import time


class Person:
    def __repr__(self):
        return f"Name: {self.name}\n" \
               f"Birthday: {self.bday}\n" \
               f"Init @: {self.created_time}\n" \
               f"Fav Shape: {self.shape}\n" \
               f"Health: {self.health}\n" \
            # f"Dept: {self.dept}\n" \
        # f"Group: {self.group}"

    def __str__(self):
        return f"{self.name} is {self.health.lower()} and was born on {self.bday}."

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __init__(self, name, bday):
        self.name = name
        self.bday = str(bday)
        self.created_time = str(time.strftime('%d-%m-%Y %H:%M:%S'))
        # self.traits = []
        # self.likes = []
        self.shape = ''
        self.favourite_shape()
        self.health = ''  # Healthy, Unhealthy
        self.determine_health()
        self.id = Generators.generate_uid(self, time.time())
        # self.specialty = ''
        # self.determine_specialty()
        # self.dept = ''
        # self.determine_dept()
        # self.group = ''
        # self.determine_group()

    # def
    #
    # def personal_likes(self):
    #     artsy = []
    #
    #     self.likes.append(random.choice())

    def favourite_shape(self):
        shapes = ['Circle', 'Triangle', 'Diamond', 'Square', 'Rectangle', 'Octagon', 'Oval']
        self.shape = random.choice(shapes)

    def determine_health(self):
        roll = random.uniform(0, 1)
        if roll <= 0.6:
            self.health = 'Unhealthy'
        else:
            self.health = 'Healthy'

    # def determine_specialty(self):
    #     sharp_shapes = 'Triangle', 'Diamond', 'Square', 'Rectange'
    #     rounded_shapes = 'Circle', 'Oval', 'Octagon'
    #     sharp_specialties = 'Tool making', 'Jewel crafting', 'Mining'
    #     rounded_specialties = 'Gathering', 'Hunting', 'Cleaning'
    #
    #     if self.shape in rounded_shapes:
    #         return random.choice(rounded_specialties)
    #
    #     elif self.shape in sharp_shapes:
    #         return random.choice(sharp_specialties)
    #
    # def determine_dept(self):
