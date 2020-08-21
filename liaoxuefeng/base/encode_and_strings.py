# 20191228

# encode and strings

from encode_and_strings_2 import test

print ("Part 1 - source file encoding")

# First let's jump to 'encode and strings_2.py' to see 
#  file encoding's effects.

# --> encode and strings_2.py
test ()

print ("Part 2 - utf-8 as default")

def string_info(x):
    print ("string: <%s>" % x)
    print (" len=%s" % len(x))
    print (" encode as utf-8 size=%s" % len(x.encode('utf-8')))
    print (" encode as gb2312 size=%s" % len(x.encode('gb2312')))

a = '奋发图强'
string_info(a)
a = 'ABCDEF'
string_info(a)