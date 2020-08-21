
# Attribute of class and insntances

# The default attribute of a instance is same to its class.
# In CPP, class is only type, it can't be accessed unless 
# is has been instantialized.

class Animal(object):
    name = "Animal" # this is the attribute of class

animal = Animal()

print (animal.name) # "Animal"
print (Animal.name) # "Animal"

animal.name = "Dog" # change the attribute of instance

print (animal.name) # "Dog"
print (Animal.name) # "Animal"