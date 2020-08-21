# class customize


# @ __str__

class A(object):
    def __str__(self):
        return "Custom A"

print (A())

# @ __iter__

class B(object):
    def __init__(self, limit):
        self.__count = 0
        self.__limit = limit
    def __iter__(self):
        return self
    def __next__(self):
        self.__count += 1
        if (self.__count > self.__limit):
            raise StopIteration()
        else:
            return self.__count

# print 1,2,3,4,5
count = B(5)
for i in count:
    print(i)

# @ __getitem__

class C(object):
    def __getitem__(self, n):
        if (isinstance(n, int)):
            return n
        elif (isinstance(n, slice)):
            L = []
            for i in range(n.start, n.stop):
                L.append(i)
            return L

c = C()

print(c[2]) # 2
print(c[5:10]) # [5,6,7,8,9]

# @ __getattr__

class D(object):
    def __getattribute__(self, attr):
        if attr == 'haha':
            print ("trying to get @haha, but not exist!")

d = D()
d.haha # trying to get @haha, but not exist!

# @ __call__

class E(object):
    def __call__(self):
        print ("call E")

E()() # call E