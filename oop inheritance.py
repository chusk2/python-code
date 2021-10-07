class Animal:
	def __init__(self):
		self.status = "alive"
	def breathe(self):
		if self.status == 'alive':
			print("I'm breathing...")
		elif self.status == "dead":
			print("Not breathing anymore. X(")
	def kill(self):
		self.status = 'dead'
	def alive(self, name):
			
		if self.status == 'alive':
			print(f'{name} is happy and enjoying',
				f"its life")
		elif self.status == 'dead':
			print(f"I am terribly sorry. {name} is",
				f"in Heaven.")

class Dog(Animal):
	
	def __init__(self, dog_name):
		super().__init__()
		self.dog_name = dog_name
		self.mood = 'relaxed'

	def bark(self):
		print('Woof, woof!!')
	
	def pet(self):
		self.mood = 'excited'
		print(f"{self.dog_name} is {self.mood}"
			  " right now.")
	
	def show_mood(self):
		print(f"I'm {self.mood} right now!")
	
	
george = Dog(dog_name='George')

print('Is George alive?')
george.alive(name=george.dog_name)
george.pet()
george.bark()
george.breathe()
george.kill()
george.alive(name=george.dog_name)
george.breathe()


		
