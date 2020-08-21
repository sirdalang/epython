# multiple inheritance
#
# similiar to cpp

# A            B
#   \        /
#        C

class A(object):
    def speak(self):
        print ("speak")

class B(object):
    def talk(self):
        print("talk")


class AB(A,B):
    pass

ab = AB()

ab.speak()
ab.talk()