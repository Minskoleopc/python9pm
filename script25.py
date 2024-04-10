# # three modes 
# # read , write , append

# # creation a object
# # f  = open('myfile.txt','w')
# # # taking user input
# # str = input('Enter the name')
# # # writing to the file
# # f.write(str)
# # # closing the filec
# # f.close()

# # program 2
# #
# f = None
# try:
#     fileName = input('enter the filename')
#     f = open(fileName,'r')
#     str = f.read()
#     print(str)
# except FileNotFoundError:
#     print("File not found")
# finally:
#     if f is not None:
#         f.close()
# print("bye")

# program 1 
# read , write and append

# opening the file 
# f = open("myfile2.txt",'w')
# # taking input from the user
# name = input('Enter the name')
# # writing to file
# f.write(name)
# # closing
# f.close()

# program 2
# fileName = input('please enter the fileName')
# f = open(fileName,'r')
# str = f.read()
# print(str)
# f.close()

# program3
# f = None
# try:
#     fileName = input('please enter the fileName')
#     f = open(fileName,'r')
#     str = f.read()
#     print(str)
# except FileNotFoundError:
#     print("file not found")
# finally:
#     if f is not None:
#         f.close()

# program4
# f = open('myfile3.txt',"w")
# while str != "@":
#     str = input('Enter the name'+'\n')
#     if str != '@':
#         f.write(str + '\n')
# f.close()

# program 5
# r w
# f = open('myfile2.txt','a+')
# while str != "@":
#     str = input("Enter the names")
#     if str != '@':
#         f.write(str + "\n")
# f.seek(0,0)
# str2 = f.read()
# print(str2)
# f.close()

# program 2

import os , sys
# fname = input('Enter the filename: ')
# if os.path.isfile(fname):
#     f = open(fname,'r')
# else:
#     sys.exit()
# print('The file contents are: ')
# str = f.read()
# print(str)
# f.close()


#count word character and lines

fname = input('Enter the filename: ')
if os.path.isfile(fname):
    f = open(fname,'r')
else:
    print("file does not exist")
    sys.exit()

cc = 0
cw = 0
cl = 0

for line in f:
    cl = cl + 1
    list = line.split() #["chinmay","learning" ,"js"] 
    cw = cw + len(list)
    cc = cc + len(line)
print(cl)
print(cw)
print(cc)

f.close()


f.close()































































