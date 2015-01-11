class Animal:
	def __init__(self,name,color,age,size):
		self.name = name
		self.color = color

		self.age = age

		self.size = size

	def printAll(self):
		print(self.name)
		print(self.color)
		print(self.age)
		print(self.size)
	
	def sleep(self):
		print("the animal named " + self.name + " is sleeping")

	def eat(self):
		print("the animal named " + self.name + " is eating")

sloth = Animal(name = "sid",color = "blue",age = 21,size = "1.6 times the cosine of awesomeness")

babe = Animal(name = "babe",color = "beautiful",age = "amazing",size = "air baloon")

sloth.printAll()
print("###########")
babe.printAll()
print("###########")
sloth.sleep()
sloth.eat()
print("###########")
babe.sleep()
babe.eat()



		
