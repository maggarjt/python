# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:00:37 2019

@author: magga
creating classes and using initialization methods and print
to view those attributes
looking at the diff between classes and objescts of the class
"""

class Fighters:
    def __init__(self, name):
        self.name = name
        
qazi = Fighters("Qazi")
joe = Fighters("Joe")


print(qazi.name)
print(joe.name)


class Car:
    def __init__(self, color, year, make, model):
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        
        
hooptie = Car('red', 1990, 'ford', 'thunderbird')


print(hooptie.color)
print(hooptie.year)
print(hooptie.make)
