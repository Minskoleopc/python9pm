# ducktyping
# class Duck:
#     def talk(self):
#         print("Quack Quack")

# class Human:
#     def talk(self):
#         print("Hi Hello")

# class Dog:
#     def bark():
#         print("Bow Bow")


# def call_talk(obj):
#     if hasattr(obj,'talk'):
#         obj.talk()
#     else:
#         obj.bark()

# a = Duck()
# b = Human()
# c = Dog()

# call_talk(a)
# call_talk(b)
# call_talk(c)

# operator overloading 
print("hello"+"world")  # __add__
print(11+3) # __add__

class BookX:
    def __init__(self,pg):
        self.pages = pg

class BookY:
    def __init__(self,pg):
        self.pages = pg

    def __add__(self,other):
        return self.pages + other.pages

ramayan = BookX(200)
mahabharat = BookY(100)
    
print(ramayan.pages + mahabharat.pages)
print(mahabharat+ramayan)


# program 3
class BookX:
    def __init__(self,pg):
        self.pages = pg
    def __gt__(self,other):
        return self.pages > other.pages

class BookY:
    def __init__(self,pg):
        self.pages = pg


ramayan = BookX(200)
mahabharat = BookY(100)
print(ramayan.pages > mahabharat.pages)
print(ramayan > mahabharat)

# overriding 
class WorldBank:
    def loan(self):
        print("I am loan from WB")

    def save(self):
        print("I am save from WB")

class SBI(WorldBank):
    
    def loan(self):
        print("I am loan from SBI")

    def save(self):
        print("I am save from SBI")
    
   
class PNB(WorldBank):
   def loan(self):
        print("I am loan from PNB")

   def save(self):
        print("I am save from PNB")

nagpur = SBI()
wardha = PNB()

nagpur.loan()
nagpur.save()



# overloading 









