# slots 

# __slots__ is used to restrict bindings to class and insntaces.
# Both attribute and interface can be dynamicly bound to class or 
# instance.

class Animal(object):
    pass

animal = Animal()

# dynamicly bind attribute to instance
animal.name = "Dog" 
print(animal.name)

def set_name(self, name):
    self.name = name

# dynamicly bind interface to instance
from types import MethodType
animal.set_name = MethodType(set_name, animal)

animal.set_name("Cat")
print(animal.name)

# Bind interface to instance affects instance only
# Bind interface to class affects all instance
# Only after it's bound, it takes effect
def get_name(self):
    return self.name

Animal.get_name = get_name

print(animal.get_name())

# __slots__

# Below HAnimal only allows attribute "name" and "age"
# "__slots__" onlt affects THIS class, not its children.
class HAnimal(object):
    __slots__ = ('name', 'age')

