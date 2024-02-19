
import re
# program 1 search
str = 'cat man sun mpo run mat mm9 sun'
e = re.search(r'm\w\w',str)
f = re.search(r'\wun',str)
#/w - A-Z , a-z , 0-9




#e # None---- python ---- false value
if e:
    print(e.group())
else:
    print("match not found !")

if f:
    print(f.group())
else:
    print("match not found")


# program 2 # findall
strB  = "man sun mop run mat fat cat sat"
q = re.search(r'\w\wp',strB)
if q:
    print(q.group())
else:
    print("not found")

q2 = re.findall(r'm\w\w',strB)
q3 = re.findall(r'\wat',strB)
print(q2)
print(q3)

# program 3
# match
strC = "mon tue wed thu fri sat"
q4 = re.match(r"m\w\w",strC)
if q4:
    print(q4.group())
else:
    print("match not found")



# program 4
strD = "This; is the 'core' python's book"
#\w - [A-Z a-z 0-9]
#\W - non alphanumreic
q5 = re.split(r"\W+",strD)
print(q5)
#'\W' - non - alpha-number
info = 'chinmay:7709192441'
print(re.split(r'\W+',info))

#program 5
strE = "I am learning javascript"
q6 = re.sub(r'javascript','python',strE)
print(q6)

# search(),findall(),match(),split(),sub()

# program 6
# [A-Z , a-z , 0-9] // alphanumric  // " ", %%%
# [/W] --- " " and special symbol
# [/w]* zero or more repetitions
# \d  -- represents only digits
# \b -- only blank space
str6 = "an apple a day keeps doctor away"
e2 = re.findall(r'\ba[\w]*',str6)   # ["an", "apple" , a , ay,away]
print(e2)

# program 7
str7 = "The meeting will be conducted on 1st and 21st of each month"
e3 = re.findall(r'\d[\w]*',str7)
print(e3)
#\d - digit

# 9:30 pm
# 9:30 pm

# program 8
str8 = "one two three four five six seven 8 9 10"
e4 = re.findall(r'\b\w\w\w\w\w',str8)
print(e4)
str8 = "one two three four five six seven 8 9 10"
e4 = re.findall(r'\b\w{5}',str8)
print(e4)
str8 = "one two three four five six seven 8 9 10"
e4 = re.search(r'\b\w{5}',str8)
print(e4.group())
# program 9
str9 = "one two three four five six seven nineteen 8 9 10"
e5 = re.findall(r'\b\w{4,}',str9)
print(e5)

#program 10
str9 = "one two three four five six seven nineteen 8 9 10"
e5 = re.findall(r'\b\w{3,5}\b',str9)
print(e5)

# program11
str6 = "one two three four five six seven nineteen 8 9 10"
e6 = re.findall(r'\b\d{1,}\b',str6)
e7 = re.findall(r'\b\d+\b',str6)
print(e6)
print(e7)

#program12
# a regular expression to find last word starting with 's'
# a regular expression to find last word starting with 'o'
str6 = "o one two three four five six seven seventeen two"
# '\Z' 0 end of string
# '\A' start of string

e8 = re.findall(r'\bs[\w]*\Z',str6)
e9 = re.findall(r'\A\bo[\w]*',str6)
print(e8)
print(e9)























