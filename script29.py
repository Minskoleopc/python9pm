
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

