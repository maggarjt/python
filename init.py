# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:48:50 2019

@author: magga
"""

class Student:
    #define initialization method
    #things that are common between students
    #name, 
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
        
#create a new student from class Student and let initialization method work
        
larry = Student('Kitty', 85, 20)
daniel = Student('Daniel', 80, 50)
    
#cvariables no contain the methods of the class and can be called easily

print(larry.name)
print(daniel.name)

print(larry.grade)
print(daniel.grade)

print(larry.age)
print(daniel.age)