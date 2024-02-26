# list comprehension
# list comprehension ----- o/p list 

#[expression:loop:condition]


# table of 2
x = [1,2,3,4,5,6,7,8,9,10]
# x2 = [i * 2 for i in x]
# print(x2)



#  even no 
x2 = [i  for i in x if i % 2 == 0]
print(x2)

# odd no
x3 = [i  for i in x if i % 2 != 0]
print(x3)

# make every character to upper()
names = ["chinmay","sarika","poorva","tanmay"]
x4 = [i.upper() for i in names]
print(x4)

names = ["chinmay","sarika","poorva","tanmay"]
x4 = [i.upper() for i in names if i.endswith('y')]
print(x4)

names = ["chinmay","sarika","poorva","tanmay"]
x5 = [i[0] for i in names]
print(x5)

x6 = [
    {
        "firstName":"chinmay",
        "lastName":"deshpande",
        "age":19,
        "vehicle":True
    },
    {
        "firstName":"sarika",
        "lastName":"pansare",
        "age":4,
        "vehicle":True
    },
    {
        "firstName":"pranali",
        "lastName":"pansare",
        "age":19,
        "vehicle":False

    },

    {
        "firstName":"tavish",
        "lastName":"anade"
    }

]
x7 = [x['firstName'] for x in x6]
print(x7)


x8 = [11,22,33,44]
#[odd,even,odd,even]

x9 = [x for x in x8 if x % 2 == 0]
print(x9)

#       ternary operator
x10 = ["even" if x%2 == 0 else "odd" for x in x8]
print(x10)

# students 
students  = [
    {
        "firstName":"chinmay",
        "lastName":"deshpande",
        "age":19,
        "vehicle":True
    },
    {
        "firstName":"sarika",
        "lastName":"pansare",
        "age":4,
        "vehicle":True
    },
    {
        "firstName":"pranali",
        "lastName":"pansare",
        "age":19,
        "vehicle":False

    },

    {
        "firstName":"tavish",
        "lastName":"anade",
        "age":39,
        "vehicle":True
    }

]
q3 = [i['firstName'] for i in students if i['age'] >= 18 and i['vehicle'] == True]
print(q3)

q4 = [ x['firstName'] if x['age'] > 18 and x['vehicle'] else None for x in students]
print(q4)

q4 = [x for x in q4 if x != None]
print(q4)

#["chinmay":'candrive',"sarika":"cannot drive","pranali":"cannot","tavish":"candrive"]