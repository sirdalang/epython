
# circulation

# for x in cols

def cal_sum(array):
    sum = 0
    for it in array:
        sum += it
    return sum


array_1 = [1,2,3,4,5,6,7,8,9]
print ("sum of array_1 = %d" % (cal_sum(array_1)))

# range(100) = [0,1,2,...,99]
print ("sum of range(100) = %d" % (cal_sum(range(100))))

# while 

def fibonacci(i):
    if i < 1:
        return 0
    prev = 0
    it = 1
    count = 1
    while (count < i):
        temp = prev + it
        prev = it
        it = temp
        count += 1
    return it


test = range(10)
for i in test:
    print ("fibonacci(%d)=%d" % (i, fibonacci(i)))


# examples about 'break' and 'continue'
# blank...