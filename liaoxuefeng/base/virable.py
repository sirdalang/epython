
# Python use # to start comment


# 1.Examples about interger.

print ("PART 1 - Interger")

a = 1
b = 2
c = b - a

if c == a:
    print ("c(%d) equal to a(%d)"%(c,a))
else:
    print ("not equal!")


# 2.Examples about float number.

print ("PART 2.1 - float number")

a = 1.1
b = 2.2 
c = b / 2
if a == c:
    print ("c(%f) equal to a(%f)" % (c,a))
else:
    print ("not equal!")

# Let's see if the precision is enough

print ("PART 2.2 - float number precision")

def precision_test(x):
    a = x
    b = 1
    c = b + a
    if (c - b) == a:
        print ("precision enough for (%s == %s)" % (c - b, a))
    else:
        print ("precision not enough for (%s == %s)" % (c - b, a))

# Here we can see that float calculation is not accurate.

a = 1
b = 1e-1
precision_test (a)
precision_test (b)

# 3.Examples about BOOL value

print ("Part 3 - bool value")

a = True
b = True and False
c = True or False
d = not False

print ("%s %s %s %s" % (a,b,c,d))

# 4. None

print ("Part 4 - none value")

a = None
b = None
if a == b:
    print ("a(%s) equal to b(%s)" % (a,b))
else:
    print ("a(%s) not equal to b(%s)" % (a,b))

# 5. About '//'

print ("Part 5 - \'//\'")

a = 10
b = 3
c = 10 / 3
d = 10 // 3
print ("10/3=%s, 10//3=%s" % (c,d))


# 6. About copy

a = 10
b = a
b = 15
print ("a=",a,"b=",b)