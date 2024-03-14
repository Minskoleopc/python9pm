# # inheritance

# class Student:
#     def __init__(self,firstName,lastName,adharNo):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.adharNo = adharNo

#     def displaName(self):
#         print(self.firstName + self.lastName)

# class Teacher(Student):
#     salary = 10000

#     def displaySalary(self):
#         print(self.salary) 

# amol = Teacher("amol","rao",123)
# print(amol.firstName)
# print(amol.lastName)
# print(amol.adharNo)
# print(amol.salary)
# amol.displaName()
# amol.displaySalary()


# program 2
# Single inheritance


class Student:

    def __init__(self,fn,ln,adharNo) :
        self.firstName = fn 
        self.lastName = ln 
        self.adharNo = adharNo

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self, fn, ln, adharNo ,salary):
        super().__init__(fn, ln, adharNo)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

amol = Teacher("amol","rao",123,40000)
print(amol.firstName)
print(amol.lastName)
print(amol.adharNo)
print(amol.salary)

amol.displayName()
amol.displaySalary()

# program 3
class GrandFather():
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
    
    def displayGName(self):
        print(self.firstName+ self.lastName)

class Father(GrandFather):
    def __init__(self, fn, ln ,ffn):
        super().__init__(fn, ln)
        self.fname = ffn 

    def displayFName(self):
        print(self.fname + self.lastName)


class Son(Father):
    def __init__(self, fn, ln, ffn ,ssn):
        super().__init__(fn, ln, ffn)
        self.sname = ssn
    
    def displaySName(self):
        print(self.sname + self.lastName)

amol = Son("dadaji","rao","dilip","amol")
print(amol.firstName)
print(amol.lastName)
print(amol.fname)
print(amol.sname)

amol.displayFName()
amol.displaySName()
amol.displayGName()




        
    





















