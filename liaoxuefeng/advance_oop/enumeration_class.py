# ad-oop - enumeration class

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', "Jul",
    'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

month1 = Month.Jan
month2 = Month.Mar

if month1 == month2:
    print (month1, ' is equal to ', month2)
else:
    print (month1, ' not equal to ', month2)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# Sun -> Weekday.Sun , 0
# ...
for name,member in Weekday.__members__.items():
    print (name, "->", member, ',', member.value)