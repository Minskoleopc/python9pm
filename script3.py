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
# setH = {11,22,33}
# setJ = {44,55,66}
# setK  = setH.union(setJ)
# print(setK)

# setL = {11,22,33}
# setB = {44,55,33}
# setQ  = setL.intersection(setB)
# print(setQ)


# program 1
setA = {11,22,33}
setB = {33,44,55}
setC = setA.union(setB)
print(setC)

# program 2

setC = {11,22,33,44}
setD = {33,44,55}
# setE = setC.intersection(setD)
# print(setE)
setC.intersection_update(setD)
print(setC)


setL = {11,22,33,44}
setJ = {66,77,88,99,22,44}
setL.intersection_update(setJ)
print(setL)


# program 3

setF = {11,22,33,44}
setB = {66,11,33,99}

#setG = setF.symmetric_difference(setB)
setF.symmetric_difference_update(setB)
print(setF)


setQ = {11,22,33}
setM = {44,55,22}

# setN = setQ.symmetric_difference(setM)
# print(setN)
setM.symmetric_difference_update(setQ)
print(setM)


# program 4
setQ1 = {11,22,44}
setQ2 = {66,22,88}
# setW = setQ1.difference(setQ2)
# print(setW)
# print(setQ1)

setQ1.difference_update(setQ2)
print(setQ1)


# program 5
setQ1 = {11,22,33}
setQ2 = {11,22,33,44}
e = setQ2.issuperset(setQ1)
f = setQ1.issuperset(setQ2)
print(e)
print(f)
x = setQ1.issubset(setQ2)
print(x)

# program6
setA = {11,22,33,88}
setB = {77,88,99}
h = setA.isdisjoint(setB)
print(h)

setG = {11,22,33,44}
w = setG.discard(55)
print(w)
print(setG)







































 