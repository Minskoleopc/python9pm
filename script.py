
info = {
    "first_name":"chinmay",
    "last_name":"deshpande",
    "age":10,
    "rollNo":45
}

# info2 = info
# info2['age'] = 89

# print(info)
# print(info2)

# copy()
info3 = info.copy()
info3['age'] = 55
print(info)
print(info3)

# program 2
# clear()
info = {
    "first_name":"chinmay",
    "last_name":"deshpande",
    "age":10,
    "rollNo":45
}
# info.clear()
# print(info)

# pop(key)
# info.pop('age')
# print(info)

# #popitem()
# info.popitem()
# print(info)

# update()
# info.update({"city":"pune","language":"hindi"})
# print(info)

# program 3

info = {
    "first_name":"chinmay",
    "last_name":"deshpande",
    "age":10,
    "rollNo":45
}

# get()
#q11 = info['Age']
q1 = info.get('Age')
print(q1)
# print(q11)
print("hello")

# loop 

vehicle = {
    "color":"red",
    "type":"sedane",
    "regNo":123
}

print(vehicle['color'])
for item in vehicle:
    print(item,vehicle[item])

for x in vehicle.keys():
    print(x)

for y in vehicle.values():
    print(y)

for k,v  in vehicle.items():
    print(k , v)








