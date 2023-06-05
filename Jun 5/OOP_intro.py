#Object Oriented Programming

class dog():
    def __init__(self):
        self.color = "black"
        self.size = "big"

    #def intro(self):
        #print("hi, my size is " + self.size)

    def __intro(self):
        print("hi, my size is " + self.size)

    def printintro(self):
        self.__intro()



lucky = dog()
happy = dog()
lucky.color = "brown"
lucky.size = "small"
print(lucky.color)
print(happy.color)
lucky.printintro()