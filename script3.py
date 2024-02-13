# # program 1 unique values 
# setA = {11,22,33,44,33}
# print(setA)

# # program 2 set stores the value by index ??
# #print(setA[0]) - No 

# # program 3
# setB = {"amol","satish","ram",22}
# print(setB)

# #program 4 # to verify a particular value in set
# print("amol" in setB)

# # program 5
# print(len(setB))

# # program 6
# setC = {"pune","chandrapur","mumbai","pune"}

# #        0         1       2        3
# city = ["pune","nagpur","mumbai","banglore"]
# print(type(city))
# for x in range(4):
#     #print(x)
#     print(city[x])

# for item in city:
#     print(item)

# for item in setC:
#     print(item)

# print(len(setC))


# program 1

# add()
setA = {11,22,33,44}
setA.add(333)
print(setA)

# program 2 # clear()
setB = {"ram","satish","sachin","ramesh"}
setB.clear()
print(setB)


# program 3 # pop() # remove(ele)
setB = {"ram","satish","sachin","ramesh"}
setB.remove("sachin")
print(setB)
setB.pop()
print(setB)

# program 4
setB = {"ram","satish","sachin","ramesh"}
setB.update(["chinmay","tamnay"])
setB.update(("sarika","pranali"))
print(setB)

# program 5
setB = {"ram","satish","sachin","ramesh"}
# setC = setB 
# setC.remove("ram")
# print(setC)
# print(setB) 

# setE = setB.copy()
# setE.remove("ram")
# print(setE)
# print(setB)


#program 6
setH = {11,22,33}
setJ = {44,55,66}
setK  = setH.union(setJ)
print(setK)

setL = {11,22,33}
setB = {44,55,33}
setQ  = setL.intersection(setB)
print(setQ)





















 