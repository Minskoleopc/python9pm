# Duck typing 

# class - 1
# class Duck:
#     def talk(self):
#         print("quack quack")

# # class -2
# class Human:
#     def talk(self):
#         print("Hi hello")

# def call_talk(obj):
#     obj.talk()


# duckA = Duck()
# amol = Human()
# call_talk(duckA)
# call_talk(amol)

# program 2
class Duck:
    def talk(self):
        print("quack quack")

# class -2
# class Human:
#     def talk(self):
#         print("Hi hello")

# #class -3
# class Dog:
#     def bark(self):
#         print("bow bow")


# def call_talk(obj):
#     if hasattr(obj,'talk'):
#           obj.talk()
#     else:
#         obj.bark()


# duckA = Duck()
# amol = Human()
# moti = Dog()
# call_talk(moti)

# Operator overloading 
        
print(1+1)
print("hello"+ "world")

class BookX:
   def __init__(self,pages):
      self.pages = pages

class BookY:
 def __init__(self,pages):
    self.pages = pages

 def __add__(self,other):
      return self.pages + other.pages
    
ramayan = BookX(100)
mahabharat = BookY(200)

print(ramayan.pages + mahabharat.pages)
print(mahabharat + ramayan)


# Method overriding