# @property

# @property turn interface into attribute
# @interface.setter turn setter into attribute assignment (???)

class Student(object):
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must be between 0 to 100!")
        self._score = value
    
    @property
    def score_state(self):
        if (self.score > 90):
            return 'A'
        elif (self.score > 70):
            return 'B'
        else:
            return 'C'

    
lily = Student()

# lily.score = 'ha' 
# Err Msg: ValueError: score must be an integer!

# lily.score = 111 
# Err Msg: ValueError: score must be between 0 to 100!

lily.score = 80
print(lily.score_state) # B

lily.score = 95
print(lily.score_state) # A

# lily.score_state = 'B'
# Err Msg: AttributeError: can't set attribute