# oop - class and instance

# class definition

class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

# instantiation

Lily = Student('Lily', 94)
Jim = Student('Jim', 75)

print(Lily.name, Lily.score, Lily.get_grade())
print(Jim.name, Jim.score, Jim.get_grade())