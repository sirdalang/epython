# map and reduce

from functools import reduce

# map

def xsquare(x):
    return x*x

listOrigin = list(range(0,5)) # 0,1,2,3,4

r = map (xsquare, listOrigin)

# here r is an iterator

print (list(r)) # 0,1,4,9,16


# reduce
# python 3.x need to import reduce from functools

def xadd(x,y):
    return x+y

r = reduce (xadd, listOrigin)

print (r)
