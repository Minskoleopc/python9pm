
# function 

# int as parameter and int as return 
def add(x,y):
    return x + y
e = add(12,3)
print(type(e))

# float as parameter and float as return 
def add(x,y):
    return x + y
f = add(23.5,66.7)
print(type(f))

# string as parameter and string as return type 
def greet(word):
    return "hello "+ word
g = greet("chinmay")
print(type(g))

# list as parameter and list as return type 
cities = ["pune","mumbai","nagpur"]
def addCity(lst):
    cities.append("wardha")
    return lst
h = addCity(cities)
print(type(h))
# dict as paramerter and dict as return type

info = {
    "firstName":"chinmay",
    "lastName":"deshpande"
}

def addLang(dictA):
    dictA['language'] = "hindi"
    return dictA
j = addLang(info)
print(j)
print(type(j))

# tuple as parameter and tuple as return type 

a1 = 12,13
a1 = (12,13)

def addElementToTuple(tupA):
    tupA = list(tupA) # (12,13), [12,13]
    print(tupA)
    tupA.append(45)
    print(tupA)
    tupA = tuple(tupA)
    return tupA
l = addElementToTuple(a1)
print(type(l))

# set as a parameter and set as return type
setA = {11,22,33}
def addEtoS(x):
    setA.add(x)
    return setA
l = addEtoS(23)
print(type(l))

# lambda

def add(x,y):
    return x + y

e = add(12,4)
print(e)

addB = lambda x,y:x+y
e2 = addB(21,4)
print(e2)
e = lambda x : x*x 
e3 = e(3)
print(e3)

names = ["amit","amol","akay","shivani"]
def changeName(lst):
    #lst = names 
    lst[0] = "ajay"
    return lst

e4 = changeName(names)
print(e4)
print(names)

# city = ["pune","nagpur","kolkata"]
# city2 = city 
# city2[0] = "wardha"
# print(city)
# print(city2)

lstA = [1,2,3,4,5]
n = []
for i in lstA:
    n.append(i*5)
print(n)

# list comprehension -- o/p - list
#[expression:loop:condition]
e4 = [i * 5 for i in lstA]
print(e4)
lstB = [1,2,3,4,5,6,7,8,9,10]
e5 = [i* i for i in lstB]
print(e5)

lstC = [44,55,66,77,33,44,55,66,77,11,22,33,7,8,9]
listD= []
for x in lstC:
    if x % 2 == 0:
        listD.append(x)
print(listD)

#[expression:loop:condition]
e6 =  [x for x in lstC if x % 2 == 0]
print(e6)
        
