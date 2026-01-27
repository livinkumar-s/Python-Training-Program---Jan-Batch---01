# Creating Class

class Bottle:
    # attributes
    def __init__(self):
        self.height=40
        self.radius=2
    
    # Methods
    def open(self):
        print("The bottle is getting opened")
    
    def close(self):
        print("The Bottle is getting closed...!")
    
    def printVolume(self):
        print((22/7)*self.radius*self.radius*self.height)

#attr-->2, Methods--> 3

class Rect(Bottle):
    def __init__(self,lenght,birth):
        self.length=lenght
        self.birth=birth 
    
    def perimeter(self):
        print((self.birth+self.length)*2)
    def area(self):
        print(self.birth*self.length)

# bot1=Bottle()
# bot2=Bottle()
# bot3=Bottle()
# bot4=Bottle()

# rectangle1=Rect(30,20)
# rectangle2=Rect(40,10)

# print(rectangle1.birth)
# rectangle1.area()

# a=1
# b="One"
# c=[1,2,3,4]


# print(type(rectangle1)) #<class __main__.'Bottle'>

# r1=Rect(2,2)

# r1.open()

# class authManager:
#     #attr
#     pass 
#     #method

# a1=authManager()

# a1.login()
# a1.register()
