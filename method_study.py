class Fighter:
		#define a class called Fighter
	def __init__(self, name):
		self.name = name
		self.health = 100
		self.damage = 10

#now define a method of class fighter called attack
	def attack(self, other_guy):
		other_guy.health = other_guy.health - self.damage
		# also could put "other_guy_health -= self.damage to decrement"

qazi = Fighter("Qazi")
you = Fighter("Jesse")

print(qazi.name + ' is attacked by ' + you.name)


# now access attack method
you.attack(qazi)

#object_name.Fighter_Class_Method(implicit parameter is the object entitled 'qazi' and has )
# object 'qazi' && object 'you' has method attack

print('Qazis health is ' + str(qazi.health))
you.attack(qazi)
print('Qazis health is ' + str(qazi.health))