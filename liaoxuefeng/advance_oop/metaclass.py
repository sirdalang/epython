# type() and metaclass

# @ type is used to create class

def fn(self):
    print("hello!")

# here Hello is a class
Hello = type('Hello', (object,), dict(hello=fn))

Hello().hello() # hello!

# @ metaclass
# metaclass controls how to create class

# ... ignored