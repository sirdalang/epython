# generator.py

# [] --> ()

alist = [x*x for x in  range(1,5)] # [1,4,9,16]

print (alist)

# here create a generator

agenerator = (x*x for x in  range(1,5))

for i in agenerator:    # same as alist
    print(i)

# using keyword 'yield' to create generator

def agenerator_2():
    yield 3
    yield 7
    yield 4

for i in agenerator_2():
    print(i)