__author__ = "byteme8bit"
from modules import Generators
import time


class Person:
    def __repr__(self):
        return f"Name: {self.name}\n" \
               f"Birthday: {self.bday}\n" \
               f"Init @: {self.created_time}\n" \
               f"ID: {self.id}"

    def __str__(self):
        return f"{self.name} was born on {self.bday}."

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __init__(self, name, bday):
        self.name = name
        self.bday = str(bday)
        self.created_time = str(time.strftime('%d-%m-%Y %H:%M:%S'))
        self.id = int(Generators.generate_uid(self, time.time()))
