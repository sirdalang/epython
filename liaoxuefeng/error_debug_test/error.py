# error process

import logging

# @ exception

def fn(x):
        
    print('try...')

    try:
        r = 10 / x # div 0 error
        print ("result=", r)
    except ZeroDivisionError as e:
        print ("except: ", e) 
    finally:
        print ("finally...")

    print ("end")


# output: 
#
# try...
# except:  division by zero
# finally...
# end
fn (0)

# output:
# 
# try...
# result= 10.0
# finally...
# end
fn (1)


# @ call stack

def calla(x):
    return 10/x
def callb(x):
    return calla(x)
def main(x):
    return callb(x)

# this call will generate call-stack infomation
# main(0)


# @ error logging
# import logging
# CallStack information will still be output, but 
# programe will not terminate.

def main_errlog(x):
    try:
        return callb(x)
    except Exception as e:
        logging.exception(e)

print(main_errlog(0))
print(main_errlog(1))


# @ custom exception
# like cpp or java

class MyException(Exception):
    pass

try:
    10 / 0
except Exception as e:
    print ("exception:", e)