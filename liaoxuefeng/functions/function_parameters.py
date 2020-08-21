# function_parameters.py

# default parameters

def openfile(filename, mode="rw"):
    print ("open <%s> with mode <%s>" % (filename, mode))

openfile ("log.dat")

# virable parameters
# virable parameters --> tuple

def sumall(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

print (sumall(1,2,3,4,5,6,7,8,9))

# key parameters
# --> dict

def printnames(name, grade, **other):
    print("name:",name,"grade:",grade,"other:",other)

printnames("Jim", 3, city="Guizhou", gender="Male")
printnames("Tom", 4)

# named key parameters
# --> dict with keys

def printnames_v2(name, grade, *, city, gender):
    pass