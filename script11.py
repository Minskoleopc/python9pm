def addA(x,y):
    print(x+y)
addA(12,3)

# program 2 Error
# def addA(x,y):
#     print(x+y)
# addA()

# default arguments 
# program 3
# def addA(x = 7 ,y = 3):
#     print(x+y)
# addA()
# addA(11,2)

# positional arguments 

# def addC(x,y):
#     print(x+y)

# e0 = addC(12,3)
# print(e0)
# print(e0)

# def addD(x,y):
#     return x + y
# e = addD(12,3)
# print(e)

# def subC(x,y):
#     return x - y
# subC(19,e)

# def sub(x,y):
#     print(x-y)
# sub(y = 33,x = 50)
    

# program 4
def addD(*args):
    print(args)
    total = 0
    for x in args:
        total = total + x
    return total
e3 = addD(1,2,33,4,55,6,7,88,9,55,66,77,8,99,44,55)
print(e3)

# program 5

def addinfo(**kwargs):
    print(kwargs)
    kwargs['city'] = "pune"
    return kwargs
e4 = addinfo(first_name = "shivani",last_name ="hedau",age= 30)
print(e4)


# program 6

def myfunction():
    a = 1
    b = 2
    a = a + 1
    print(a) # 2 
    print(b) # 2
myfunction()
#print(a)

# program 7

a = 1 # global
def myfunction2():
    b = 5 
    a = 6  # local
    a = a+ 1
    print(a) # 7
    print(b) # 5
myfunction2()
print(a) # 1

# program 8 
a = 10 # gloabal
def myfunction3():
    print(a) # global
    print(10)
myfunction3()
print(a) # global

# program 9
h = 10  # global varibale
def myfunction4():
    global h  
    h = 99 # global varibale
    print(h)
myfunction4()
print(h) # global variable

# program 10
# local varible 
# access function











