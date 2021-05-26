#from file import class
from animal import Animal

#instance/ object

dog = Animal(name='Lizzy', age = 3)
cat = Animal(name = 'Zorka', age=10)
bird= Animal(name= 'Fufu', age=19)

print(dog.speak())
print(cat.speak())
print(bird.speak())

print(dog.kiki())
print(cat.kiki())
print(bird.kiki())


