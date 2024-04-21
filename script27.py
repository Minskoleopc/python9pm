# reclen = 20
# with open('cities.bin','wb') as f:
#     n = int(input('Enter the number of cities'))
#     for x in range(n):
#         city = input('enter the city') # pune
#         city = city + (reclen - len(city)) * " "
#         city = city.encode()
#         f.write(city)

# # program 2

# reclen = 20
# with open('cities.bin','rb') as f:
#     n = int(input('record number')) # 2
#     f.seek(reclen * (n-1))
#     str = f.read(reclen)
#     str = str.decode()
#     print(str)



import os
# reclen = 20
# size = os.path.getsize('cities.bin') # 100
# totalRecords = int(size/ reclen) # 5

# with open('cities.bin',"rb") as f:
#     city = input('enter the  city') # "nagpur"
#     #city = city + (reclen - len(city))*" "
#     city = city.encode()
#     position = 0
#     found = False
#     for x in range(totalRecords):
#         f.seek(position)
#         acity = f.read(reclen)
#         if city in acity:
#             print('city found')
#             found = True
#             break
#         position = position + reclen
#     if not found:
#         print("city not found")

# update


import os
reclen = 20
size = os.path.getsize('cities.bin')
totalRecords = int(size/ reclen)

with open('cities.bin','r+b') as f:
    rep = input('enter the city to replace')
    rep  = rep + (reclen - len(rep)) * " "
    rep = rep.encode()
    update = input('enter city to replace with')
    update  = update + (reclen - len(update)) * " "
    update = update.encode()

    position = 0 
    found  = False
    for x in range(totalRecords):
        f.seek(position)
        ac = f.read(reclen)
        if ac == rep:
            found = True
            f.seek(-20,1)
            f.write(update)
            break
        position = position + reclen
    if not found:
        print('city not found')























