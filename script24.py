
# A single try block can be follwed by several except block 
# Multiple except blocks can be used to handle multiple excpetions 
# We cannot write except block with try block
# We cannot write try block with except block
# Else block and finally block are not compulsory
# When there is no exception raised else block is executed after try block 
# Finally block is always executed

# program 1
# try:
#     names = ["sarika","poorva","shraddha"]
#     a = int(input('Enter a numberA'))
#     b = int(input('Enter the number B'))
#     print(a/b)
#     print(names[4])
# except ArithmeticError:
#     print("please enter correct input")
# except IndexError:
#     print('please add more values to list')

# program2 
# print("hello")
# try:
#     print(34/0)
# finally:
#     print("i will always execute")
# print("bye")

# program 3
# def calAvg(list):
#     [11,22,33][4]
#     total = 0
#     for item in list:
#         total = total + item 
#     avg = total/len(list)
#     return total,avg
# try:
#     a,b = calAvg([1,2,3,'a'])
#     print(a)
#     print(b)
# except TypeError:
#     print('enter the correct input')
# except ZeroDivisionError:
#     print('Arithmetic exception , enter correct value')
# except Exception:
#     print("please enter correct input")

# print("hello")
# try:
#     x = 18
#     assert x > 1 and x <= 9
#     print(x)
# except AssertionError:
#     print("condition not matched")
# print("bye")

class lowBalance(Exception):
    def __init__(self,msg):
        self.msg = msg

def check(dict):
    for k,v in dict.items():
        if(v < 20000):
            raise lowBalance("Balance is low")
try:
    names = {"snehal":100000 , "hrushali":400000,"ninad":388888,"chinmay":335}
    check(names)
    print(names)
except lowBalance as msg:
    print(msg)


    





