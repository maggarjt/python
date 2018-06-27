class Student:

	def __init__(self, name, grade):
		self.name = name
		self.grade = grade


kitty = Student('Kitty', 85)
daniel = Student('Daniel', 80)

print(kitty.grade)
print ('Daniel had an ' + str(daniel.grade) + ' because he studied')