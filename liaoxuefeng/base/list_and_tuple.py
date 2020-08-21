# list and tuple

print ("Part 1 - list")

def list_fun(listA):
    print (listA)
    print ("list len: %s" % len(listA))

    index = 0
    for item in listA:
        print ("list[%d]=%s" % (index,item))
        index = index+1

a = [1,2,3,4]

list_fun(a)

a.insert (2,100)

list_fun(a)

a[2] = 3

list_fun(a)


# Tuple

print ("Part 2 - tuple")

# tuple is a readonly version of list.
# We should use it as often as possible.

tupleA = (1,2,3)

print (tupleA)