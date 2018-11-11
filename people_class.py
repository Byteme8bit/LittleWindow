import random

__author__ = "byteme8bit"
import time


class Person:
    def __repr__(self):
        return f"Name: {self.name}\n" \
               f"Birthday: {self.bday}\n" \
               f"Init @: {self.created_time}\n" \
               f"Fav Shape: {self.shape}\n" \
               f"Health: {self.health}\n" \
               f"Dept: {self.dept}\n" \
               f"Group: {self.group}"

    def __init__(self, name, bday):
        self.name = name
        self.bday = str(bday)
        self.created_time = str(time.strftime('%d-%m-%Y %H:%M:%S'))
        self.shape = ''
        self.favourite_shape()
        self.health = ''  # Healthy, Unhealthy
        self.determine_health()
        self.specialty = ''
        self.dept = ''
        self.group = ''

    def favourite_shape(self):
        shapes = ['Circle', 'Triangle', 'Diamond', 'Square', 'Rectangle', 'Octagon', 'Oval']
        self.shape = random.choice(shapes)

    def determine_health(self):
        roll = random.uniform(0, 1)
        if roll <= 0.6:
            self.health = 'Unhealthy'
        else:
            self.health = 'Healthy'

    def determine_specialty(self):
        healthy_jobs = ''
        unhealthy_jobs = ''

        if self.health == 'Healthy':
            pass

        elif self.health == 'Unhealthy':
            pass

        else:
            pass

