"""
Names = [mahmoud,farida,ali,hassan,mohamed,,,khaled,,","taha"]
 1. Transform all names to uppercase using [normal list - list comprehension - functional programming]
"""
names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]

# normal list
result1=[]
for x in names:
    result1.append(x.upper())
print(result1)    

# list comprehension
result2=[x.upper() for x in names]
print(result2)


# functional programming
def uppercase(n):
    return n.upper()
result3=list(map(uppercase,names))

print(result3)