"""
names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
Get the names that contains 'a' in a list using [normal list - list comprehension - functional
programming]

"""
names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]

# normal list

result1=[]
litter="l"
for x in names:
    if litter in x:
        result1.append(x)
print(result1)        

# list comprehension

litter2="h"
result2=[ x for x in names if litter2 in x ]
print(result2)

# functional programming
def filterword(x):
    if litter in x:
        return x
    
result12=list(filter(filterword,names))
print(result12)