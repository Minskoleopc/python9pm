# # compile time 

# # def add():
# # print(8+8)

# # run time 

# # program 2

# # x = int(input("Enter the value 1 "))
# # y = int(input("Enter the value 2 "))
# # print(x/y)

# # listA = [11,22,33,44]
# # print(listA[4]) 


# # program3
# # def calculateBonusPlusSalary(salary):
# #     return 0.10 * salary
# # print(calculateBonusPlusSalary(1000))
# # print("hello")
# # try:
# #     x = int(input("Enter the value 1 "))
# #     y = int(input("Enter the value 2 "))
# #     print(x/y)
# # except Exception:
# #     print('Invalid input')
# # print("bye")

# # program 4
# # try:
# #     names = ["poorva","sarika","abhisha"]
# #     x = int(input("Enter the value 1 "))
# #     y = int(input("Enter the value 2 "))
# #     print(x/y)
# #     print(names[2])
# #     print(a)

# # except ArithmeticError:
# #     print('Invalid input')
# # except IndexError:
# #     print("increase value of your list")
# # except NameError:
# #     print("not defined")
# # except Exception:
# #     print("something went wront")
# # print("bye")


# #program 5

# # try:
# #     names = ["poorva","sarika","abhisha"]
# #     x = int(input("Enter the value 1 "))
# #     y = int(input("Enter the value 2 "))
# #     print(x/y)

# # except ArithmeticError:
# #     print('Invalid input')

# # finally:
# #     print("I will always execute")

# # program 6

# # try:
# #     x = int(input("Enter the value 1 "))
# #     y = int(input("Enter the value 2 "))
# #     print(x/y)

# # except ArithmeticError:
# #     print('Invalid input')

# # else:
# #     print("hello")

# # program 7
# # print('hello')
# try:
#     x = int(input("Enter the value 1 "))
#     y = int(input("Enter the value 2 "))
#     print(x/y)

# except ArithmeticError:
#     print('Invalid input')
# else:
#     print("hello")
# finally:
#     print("i willl always... ")
# print("bye")


# A single try block can be follwed by several except block 
# Multiple except blocks can be used to handle multiple excpetions 
# We cannot write except block with try block
# Else block and finally block are not compulsory
# When there is no exception raised else block is executed after try block 
# Finally block is always executed



# logical errors


# def avg(list):
#     total = 0 
#     for x in list:
#         total = total + x 
#     avg = total /len(list)
#     return total,avg


# try:
#     t,a = avg([3,5,6,7,8,'a'])
#     print(t)
#     print(a)
# except TypeError:
#     print("type error")
# except ZeroDivisionError:
#     print("zero division , cannot pass empty list")
# except Exception:
#     print('error')


# try:
#     x = int(input('Enter the number :'))
#     y = 1/x
# finally:
#     print("We are not catching the exceptions..")
# print("The inverse is ",y)

# handling the Assertion 

# try:
#     x = int(input("Enter the number between 5 and 10"))
#     assert x >= 5 and x <= 10
#     print("the number enter is ",x)
# except AssertionError:
#     print("The condition is not fulfilled")


class lowBalance(Exception):
    def __init__(self,msg):
        self.msg = msg

def check(dict):
    for k,v in dict.items():
        if(v < 20000):
            raise lowBalance("the value is below 20k , please add amount")

try:
   bank = {"raj":100000,"shivani":90000,"chinmay":100000,"tavish":50000}
   check(bank)
   print("all above 20 thousand")
except lowBalance as me:
        print(me)








