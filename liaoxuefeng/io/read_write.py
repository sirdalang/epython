# file read and write 
# very like libc

# normal open and read and close
def test():
    try:
        f = open('test', 'r')
        print(f.read(10))
        f.close()
    except IOError as e:
        print (e)

def test1():
    try:
        with open('test', 'r') as f:
            print (f.read(10))
    except IOError as e:
        print (e)

test()
test1()

# encoding support
# open (path, 'rb') : binary
# open (path, 'r', encoding='gbk)