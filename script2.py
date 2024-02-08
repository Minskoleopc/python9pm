# info2 = {
#     "firstName":"chinmay",
#     "lastName":"deshpande"
# }
# info2.clear()
# info2.copy()
# info2.pop('firstName')
# info2.popitem()
# info2.update({"city":"pune"})

# # for key in info2:
# #     print(key , info2[key])

# for key in info2.keys():
#     print(key)
# for val in info2.values():
#     print(val)
# for k,v in info2.items():
#     print(item)
#info2.get("firstName")

# program 1
e = dict.fromkeys(["amol","chinmay","ram"])
print(e)

info3 = {
    "admin":"chinmay",
    "customer":"sameer",
    "support":"raj"
}

info3.setdefault("manager",None)
print(info3)

# fromkeys()
f = dict.fromkeys(["key1","key2","key3"])
print(f)


# tuple vs list

listName = ["amol","chinmay","ram"]
print(listName)
print(type(listName))
listName.append("raj")
print(listName)
listName[0] = "sarika"


listNameB = ("amol","ram","satish")
print(listNameB)
print(type(listNameB))
#listNameB[0] = "sam"


# program 2

tupleB = (11,22)
tupleA = ("chinmay","raaj")
tupleC = (["ninad","vijeet"],["rohit","ameya"])
tupleD = 11,12
print(type(tupleD))


# program 3 
names = ("sonal","sham","ram")
print(names[0])
print(names[1])
print(names[2])

# using range 

for x in range(len(names)):
    #print(x)
    print(names[x])

# without using range
for item in names:
    print(item)

#program 4
    
tupleD = (11,22,33,44,55,66,33,55,33)
q = tupleD.count(33)
print(q)

w = tupleD.index(22)
print(w)




















