from io import StringIO


# in-mem file
# StringIO and BytesIO

# StringIO

def test():
    f = StringIO()
    f.write ("hello, world")
    print(f.getvalue())

def test2():
    f = StringIO("hello\nworld\n")
    print(f.readline())
    print(f.readline())

def test3():
    f = BytesIO()


test()
test2()