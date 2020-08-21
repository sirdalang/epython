# oop - get object infomation

class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

# type()
# type() returns class

print(type("string"))
print(type('string'))
print(type(1.13))
print(type(1))
print(type(False))

animal = Animal()
dog = Dog()
husky = Husky()
print(type(animal))
print(type(dog))
print(type(husky))

# isinstance()
# useful with class inheritation
print(isinstance(animal, Animal)) # True
print(isinstance(dog, Dog)) # True
print(isinstance(husky, Dog)) # True

