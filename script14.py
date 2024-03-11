# class Person:
#     country  = "India"
#     def __init__(self,fn,ln,rollNo,age):
#         self.firstName = fn 
#         self.lastName = ln 
#         self.rollNo = rollNo
#         self.age = age

#     # instance method
#     def displayName(self):
#         print(self.firstName + self.lastName)

#     def updateAge(self,ag):
#         self.age = ag
# shivani =  Person("shivani","hedau",23,30)
# print(shivani.firstName)
# print(shivani.lastName)
# print(shivani.rollNo)
# print(shivani.age)
# print(shivani.country)
# shivani.country = "Bharat"     

# amit =  Person("amit","bhure",22,32)
# print(amit.country)
# amit.updateAge(13)


# program 2
# class Person:
#     country = "India"
#     def __init__(self,fn,ln,age):
#         self.firstName = fn 
#         self.lastName = ln 
#         self.age = age

#     @classmethod
#     def updateCountry(cls,country):
#         cls.country = country

#     def updateAge(self,age):
#         self.age = age

# amol = Person("amol","rao",23)
# amol2 = Person("amol2","rao2",23)
# amol3 = Person("amol3","rao3",23)

# print(amol.country)
# print(amol2.country)
# print(amol3.country)

# Person.updateCountry("Bharat")

# print(amol.country)
# print(amol2.country)
# print(amol3.country)

# program 3
# count of object

class Vehicle:
    count = 0
    country = 'india'
    def __init__(self,color, type):
        self.color = color 
        self.type = type 
        Vehicle.count = Vehicle.count + 1

    # instance method 
    def updateColor(self,cl):
        self.color = cl
    # class method
    @classmethod
    def updateCountry(cls,cnty):
        cls.country = cnty
    @staticmethod
    def countObj():
        print(Vehicle.count)

audi = Vehicle("blue","sedane")
bmw = Vehicle("red","SUV")
maruti = Vehicle("blue","jeep")

print(audi.country)
print(bmw.country)
print(maruti.country)        

Vehicle.updateCountry("bharat")

print(audi.country)
print(bmw.country)
print(maruti.country)   
Vehicle.countObj()
        







