# filter

def x_isodd(x):
    return x%2 == 1

listOrigin = list(range(0,5))

r = filter(x_isodd, listOrigin)

# r is an iterator

print (list(r))