# iterator

# list and tuple

alist = [1,3]

for i in alist:
    print ("alist.it=%d" % i)

atuple = (1,4)

for i in atuple:
    print ("atuple.it=%d" % (i))

# dict and set

adict = dict({1:"a", 2:"b", 3:"c"})
aset = set(['a','b','c'])

for key in adict:
    print ("adict key[%s]=%s" % (key, adict[key]))

for value in adict.values():
    print ("adict.value=%s" % (value))

for key,value in adict.items():
    print ("adict[%s]=%s" % (key,value))