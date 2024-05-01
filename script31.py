# program 1
import re
str = "anil akhil anant an ak arun arati arundhanti abhjit ankur"
e = re.findall(r'\ba[nk][\w]*\b',str)
print(e)

# program 2
# dd-mm-yy

str = 'chinmay 7-11-1989 ,amol 19-08-1990 mayuri 21-2-1990 poorva 29-10-93 shivani 27 april 1994'
e = re.findall(r'\d{1,2}-\d{1,2}-\d{2,4}',str)
d = re.findall(r'\d{2}-\d{2}-\d{4}',str)
print(e)
print(d)

# program 3

str = "Hello world"
e = re.search(r'^he',str)
if e:
    print("string starts with He")
else:
    print("string does not starts with He")


str = "Hello world .. i am from India"
e = re.search(r'from India$',str)
if e:
    print("str ends with dia")
else:
    print("string does not end with dia")

# program 4 
str = "Hello WoRld"
e = re.search(r"world$",str,re.IGNORECASE)
if e :
    print("ends with world")
else:
    print('does not end with world')

# program 5
str2 = "Rahul got 95 marks , Vijay got 89 marks Chinmay got 60 marks"
f = re.findall(r'\d{1,2}',str2)
print(f)

g = re.findall(r'[A-Z][a-z]*',str2)
print(g)

# program 6
str3 = "The meeting will start at either 9am or 9pm else at evening 6pm"

# search - firstOccurence
# match - start of string 
# findall - all occurences











