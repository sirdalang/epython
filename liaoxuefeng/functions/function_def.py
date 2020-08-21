# function_def.py

max(1,2,3)

def my_abs(number):
    if number > 0:
        return number
    elif number == 0:
        return 0
    else:
        return -number

print (my_abs(-9))


# blank function

def nop():
    pass

# type checks
def my_abs_better(number):
    if not isinstance(number, (int,float)):
        raise TypeError("bad oprand type")
    return my_abs (number)

print (my_abs_better(-9))
# print (my_abs_better("this is amazing"))

# multiple return 
def rect_cal(width, height):
    return width * height, 2*width + 2*height

area,perimeter = rect_cal (3,4)
print ("rect(3,4): area=%d, perimeter=%d" % (area, perimeter))