
# inheritance and polymorphic

# class definition

class Animal(object):
    _name = '' # -1-
    def introduce(self):
        print ("I'm ", self._name);
    def shout(self):
        pass

class Dog(Animal):
    def __init__(self):
        self._name = 'Dog'  # -2-  understand this
    def shout(self):
        print("Wang Wang")

class Cat(Animal):
    def __init__(self):
        self._name = 'Cat'
    def shout(self):
        print("Miao Miao")

# class instantiation

dog = Dog()
cat = Cat()

dog.introduce()
dog.shout()

cat.introduce()
cat.shout()

# this is valid, so it's only a naming convention
# while 'obj.__name' is protected by python interpreter
print(dog._name) 
