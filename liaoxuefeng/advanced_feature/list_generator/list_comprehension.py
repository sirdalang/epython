# list_comprehension.py

# to generate a list quickly

a = list(range(5,9)) # [5,6,7,8]

print (a)

a = [x for x in range(5,9)] # [5,6,7,8]

print (a)

a = [x*x for x in range(5,9)] # [25,36,49,64]

print (a)

a = [a + b for a in "ab" for b in "12"] # [a1,a2,b1,b2]

print (a)