# rb = open('vk.jpg','rb')
# rb2 = open('vk2.jpg','wb')
# bytes = rb.read()
# rb2.write(bytes)
# rb.close()
# rb2.close()

# program 1
# with open('info4.txt','w') as f:
#     f.write("I am learning js")
#     f.write("I am learning python")

# # program 2
# with open('info4.txt','r') as f2:
#     str = f2.read()
#     print(str)

# program 2
# user defined data type 

import pickle
class Emp:
    def __init__(self,fn,ln,email,age):
        self.firstName = fn 
        self.lastName = ln 
        self.email = email 
        self.age = age

    def displayDetails(self):
        print(self.firstName)
        print(self.lastName)
        print(self.email)
        print(self.age)

f = open('student.dat','wb')  # file open
n = int(input('Enter the number of objects')) # 2
for x in range(n):
    fn = input("enter firstName")
    ln = input("enter lastName")
    email = input("enter email")
    age = input("enter age")
    e = Emp(fn,ln,email,age)
    pickle.dump(e,f)
f.close()
# python obj ------- data file write
# data read ----------> python object --------> displayDetails





















