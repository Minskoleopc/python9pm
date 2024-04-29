import re

# \w [a-z][A-Z][0-9]
# \b - blank space

# program 1
str = "an apple a day keeps doctor away"
e = re.findall(r'\ba[\w]*',str)
print(e)

# program 2
str2 = "The meeting will be conducted on 21st and 22nd and 1st"
#[21st,22nd,1st]
e2 = re.findall(r'\d[\w]*',str2)
e3 = re.findall(r'\d[\d]*',str2)
print(e2)
print(e3)

# program 3
str3 = "one two three four five aa bb six seven 8 9 10 ad44566m "
e4 = re.findall(r'\w{5}',str3)
e5 = re.findall(r'\w{4,}',str3)
e6 = re.findall(r'\w{3,5}',str3)
print(e4)
print(e5)
print(e6)

# program 4
e7 = re.findall(r'\d{1,}',str3)
e8 = re.findall(r'\b\d{1,}\b',str3)
print(e7)
print(e8)

#program 5 
str3 = "one two three four five six seven eight nine ten"
e9 = re.findall(r't[\w]*\Z',str3)
print(e9)
e10 = re.findall(r'\Ao[\w]*',str3)
print(e10)

# program 6

str4 = "ChinmayDeshpande:7709192441"
e5 = re.search(r'\d+',str4)
print(e5.group())

#a[\w]*   #a apple a day keeps doctor away  
#a\w+

a = 'apple a day keeps doctor away' 
print(re.findall(r'a\w+',a))
print(re.findall(r'a[\w]*',a))


