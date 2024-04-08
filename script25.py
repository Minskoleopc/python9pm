# three modes 
# read , write , append

# creation a object
# f  = open('myfile.txt','w')
# # taking user input
# str = input('Enter the name')
# # writing to the file
# f.write(str)
# # closing the filec
# f.close()

# program 2
#
f = None
try:
    fileName = input('enter the filename')
    f = open(fileName,'r')
    str = f.read()
    print(str)
except FileNotFoundError:
    print("File not found")
finally:
    if f is not None:
        f.close()
print("bye")