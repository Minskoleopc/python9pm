# single inheritance
# class Student:
#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln

#     def displayName(self):
#         print(self.firstName + self.lastName)

# class Teacher(Student):
#     def __init__(self, fn, ln,salary):
#         super().__init__(fn, ln)
#         self.salary = salary

#     def displaySalary(self):
#         print(self.salary)

# amol = Teacher("amol","rao",1000)
# print(amol.firstName)
# print(amol.lastName)
# print(amol.salary)
# amol.displayName()
# amol.displaySalary()


# Multi-level

class Student:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self, fn, ln,salary):
        super().__init__(fn, ln)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

class Professor(Teacher):
    def __init__(self, fn, ln, salary,spe):
        super().__init__(fn, ln, salary)
        self.specialization = spe
    
    def displaySpecialization(self):
        print(self.specialization)

amolp = Professor("amol","rao",1000,"oracle")
print(amolp.firstName)
print(amolp.lastName)
print(amolp.salary)
print(amolp.specialization)

amolp.displayName()
amolp.displaySalary()
amolp.displaySpecialization()


# program 3

# Herarchical inheritance

class Mother:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
    
    def displayMName(self):
        print(self.firstName + self.lastName)


class Son(Mother):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn, ln)
        self.sname  = ssn

    def displaySName(self):
        print(self.sname + self.lastName)

class Daughter(Mother):

    def __init__(self, fn, ln,ddn):
        super().__init__(fn, ln)
        self.dname  = ddn

    def displayDName(self):
        print(self.dname + self.lastName)

chinmay = Son('kanchan','deshpande','chinmay')
print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.sname)
chinmay.displaySName()
chinmay.displayMName()

gauri = Daughter('kanchan','deshpande','gauri')
print(gauri.firstName)
print(gauri.lastName)
print(gauri.dname)
gauri.displayDName()
gauri.displayMName()

# program 4


class Mother:
    def __init__(self,fn,ln):
        print("mother constructor called")
        self.firstName = fn 
        self.lastName = ln
    
    def displayName(self):
        print(self.firstName + self.lastName)

class Father:
    def __init__(self,fn,ln):
        print("father constructor called")
        self.firstName = fn 
        self.lastName = ln
    
    def displayName(self):
        print(self.firstName + self.lastName)

class Son(Father,Mother):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn, ln)
        self.sname = ssn

    def displaySname(self):
        print(self.firstName + self.lastName)

chinmay = Son("shirish","deshpande","chinmay")
chinmay.displayName()
















# multi-level inheritance 

# herarchical inheritance 

# multiple inheritance