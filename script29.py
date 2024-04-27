# \w [az AZ 09]
# program 1
# only one occurance
import re
str = "man sun mop run"
result = re.search(r'm\w\w',str)
#print(result.group())
if result:
    print(result.group())


#program2
# gives all the occurances 
str2 = "man ran sun fun map rap shape mate fate"
list2 = re.findall(r'm\w\w',str2)
print(list2)

#program 3
str2 = "python is good language to learn"
q3 = re.match(r'p\w\w',str2)
#print(q3.group())
if q3:
    q3.group()


#program 4
#\W ---- non alpha - numeric
import re
str3 = "This ; is the : 'Core' python's book"
result = re.split(r'\W+',str3)
print(result)


#program 5
str4 = "i am learning javascriet and javascriet"
q4 = re.sub(r"javascriet","javascript",str4)
print(q4)

# search()
# findall()
# match()
# split()
# sub()
# group()

# \w [a-z A-Z 0-9]
# \W [not [a-z A-Z 0-9]]
# \d - [0-9]
# \D - not[0-9]
# \b - blank space
# \A - match only start of string 
# \Z - match only at end 

# program1 
import re
str = 'an apple a day keeps doctor away'
# listA = re.findall(r'a[\w]*',str) #['an', 'apple', 'a', 'ay', 'away']
listA = re.findall(r'\ba[\w]*',str)
print(listA)

# program 2
import re 
str = 'The meeting will be conducted on 1st and 21st of this month'
# 1st  21st

# program 3
listB = re.findall(r'\b\d[\w]*',str)
#listB = re.findall(r'\b\d[\d]*',str)
print(listB)

# program 4

import re
str = "one two three four five six seven 8 9 10"
# [three,seven]
listC = re.findall(r'\b\w{5}\b',str)
print(listC)

listC = re.search(r'\b\w{5}\b',str)
print(listC.group())

# listC = re.match(r'\b\w{5}\b',str)
# print(listC.group())

# program 5
str = "one two three four five six seven 8 9 10"
listD = re.findall(r'\b\w{4,}\b',str)
print(listD)

str = "one two three four five six seven aa 8 9 10"
listD = re.findall(r'\b\w{3,5}\b',str)
print(listD)


str = "one two three four five six seven aa 8 9 10"
listD = re.findall(r'\b\d{1,}\b',str)
print(listD)


str = "one two three four five six seven aa 8 9 10 two"
listD = re.findall(r't[\w]*\Z',str)
print(listD)


str = "three one two three four five six seven aa 8 9 10 two"
listD = re.findall(r'\At[\w]*',str)
print(listD)








