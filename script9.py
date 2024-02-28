
numbers = [1,2,3,4,5]

# map 

e = lambda x:x + 5
# ue = list(map(e,numbers))
# print(ue)
e2 = list(map(lambda x:x+ 5, numbers))
print(e2)

# program 2
birthYear = [1989,1990,1991,1992]
#[35,34,33,32]
e3 = list(map(lambda x : 2024 - x,birthYear))
print(e3)
# e4 = [2024 - x for x in birthYear]
# print(e4)

# filter 
transactions = [55,-66,33,-44,55,-66,77]
deposit = [x for x in transactions if x > 0]
withdrawl = [x for x in transactions if x < 0]
print(deposit)
print(withdrawl)
e5 = list(filter(lambda x : x > 0 , transactions))
print(e5)
e6 = list(filter(lambda x : x < 0 , transactions))
print(e6)

marks  = [99,77,66,55,90,88,22,33,44]
e7 = list(filter(lambda x : x > 70,marks))
print(e7)

# reduce

from functools import reduce
lista = [11,22,33]
e = reduce(lambda acc,el:acc+el,lista,5)
print(e)






