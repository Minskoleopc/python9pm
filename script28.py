# deleting a record from the file 


import os
reclen = 20
size = os.path.getsize('cities.bin')
totalRecords = int(size/reclen)

f1 = open('cities.bin','rb')
f2 = open('cities2.bin','wb')

cityToBeDeleted  = input('Enter the city to be deleted')
cityToBeDeleted = cityToBeDeleted + (reclen - len(cityToBeDeleted)) * " "
cityToBeDeleted = cityToBeDeleted.encode()

for x in range(totalRecords):
    str = f1.read(reclen)
    if(cityToBeDeleted != str):
        f2.write(str)
f1.close()
f2.close()
os.remove('cities.bin')
os.rename('cities2.bin','cities.bin')

# regular expression
# string
str = "chinmay:7709192441" # ["chinmay","7709192441"]
info  = "chinmay-deshpande-07/11/1989"
print(str.split(":")[1])
print(info.split("-")[2])




