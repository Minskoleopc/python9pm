# program 1
# x , y   ---- formal arguments 
# 12, 13  ---- actual arguments 
def addA(x,y):
    return x + y
e1 = addA(12,3)
print(e1)


# program 2 "positional argument"
def subA(x,y):
    return x - y
e2 = subA(y = 35,x = 45)
print(e2)

# program 3 "default arguments"
def mulA(x = 10, y = 5):
    return x * y
e3 = mulA()
e4 = mulA(3,5)
print(e3)
print(e4)

# program 4 - variable length arguments
def addAll(*args):
    print(args)
    total = 0 
    for i in args:
        total  =  total + i
    return total
    

e5 = addAll(1,2,3,4,5,6,73,4,5,6,6,55,6,7,3,4,5,6,7)


# program 5 
def greet(*args):
    for i in args:
        print("welcome "+ i)
greet("pune","nagpur","wardha","akola")

# program 6
# g = 10
# h = 12.4
# j = True
# l = [11,22,33]
# f = 12,4
# r = {
#     "firstName":"chinmay"
# }
# g = {1,2,3,4}
# h = "chinmay"

def printInfo(**kwargs):
    print(kwargs)
    for i in kwargs:
        print(i,kwargs[i])

printInfo(first_name = "chinmay",lastName = "deshpande",age = 34 , city = "pune")





