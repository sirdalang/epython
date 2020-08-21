
# ifelse

def comp(a, b):
    print ("a=%s,b=%s" % (a,b))
    if a < b:
        print ("a < b")
    elif a == b:
        print ("a = b")
    else:
        print ("a > b")

comp(1,2)
comp("a","b")
comp("a","A")
comp(1.3,1.31)