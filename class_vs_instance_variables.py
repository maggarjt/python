class 	BestCourse:
	website = "http://cleverprogrammer.com"

	def __init__(self, name):
		self.name = name

course = BestCourse("Learn Python")
learn_command_line_course = BestCourse("Learn command Line")

print(course.name)  				#object_name.method
print(BestCourse.website)			#class_name.method									
print(learn_command_line_course.name) #object_name.method
print(learn_command_line_course.website) #object instantiated has access to CLass-wide variable

