
# def addA(x,y):
#     return x + y 
# e = addA(23,5)

# program 1
# def addition(fn,x,y):
#     # fn  = lambda x,y:x+y
#     # x = 12
#     # y = 4
#     e = fn(x,y) # 16
#     return e # 16

# add = lambda x,y:x+y

# result = addition(add,12,4)
# print(result) # 16

# program 2
# function as a parameter to another function
sub = lambda x,y:x-y
def subtraction(fn,a,b):
    # fn =  lambda x,y:x-y
    # a = 12
    # b = 4
    e = fn(a,b) # 8
    return e # 8

result2 = subtraction(sub,12,4)
print(result2)

# x = 10 
# print(x)
# print(sub) # function 
# sub(23,3) #  function call

# program 3
# function as a return type 
def multiplication():
    return lambda x,y:x*y

result3 = multiplication()
#result3 = lambda x,y:x*y
e2 = result3(34,5)
print(e2)