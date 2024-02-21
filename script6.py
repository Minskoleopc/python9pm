
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




