# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:20:14 2019

@author: magga
"""

class BestCourse:
    web = "www.google.com"
    
    def __init__(self, name):
        self.name = name
        
python_course = BestCourse("Learn Python")
learn_command_line = BestCourse("Learn command line")

#print attribute of instantiated object variable
print(python_course.name)
#attribute of class itself, accessed the same way
print(BestCourse.web)

print(learn_command_line.name)
#will be the same for any object when .web is used
print(BestCourse.web)