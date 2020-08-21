# oop - access control

# 'name' is public
# '__name' is private

# class definition

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def name(self):
        return self.__name  # access private virable
    def score(self):
        return self.__score

    def __get_score(self):
        if (self.__score >= 90):
            return 'A'
        elif (self.__score >= 60):
            return 'B'
        else:
            return 'C'
    
    def get_score(self):
        return self.__get_score()  # access private interface

# instantiation

Lily = Student('Lily', 95)
Jim = Student('Jim', 87)


# print(Lily.__name, Lily.get_score())
# print(Jim.__name, Jim.get_score())
#
# err msg: 'Student' object has no attribute '__name'

print(Lily.name(), Lily.get_score())
print(Jim.name(), Jim.get_score())