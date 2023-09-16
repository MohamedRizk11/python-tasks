"""
names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha"] 

Get the names that contains 2 or more a letter using [normal list - list comprehension - functional
programming]

"""
names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha"] 

# normal list
result1=[]
s="a"
for x in names:
     if x.count(s)>1:
        result1.append(x)

print (result1)

# list comprehension
result2=[x for x in names if x.count(s)>1]
print(result2)

#functional programming

def countletter(names):
    for x in names:
        if names.count(s)>1:
            return(x)


result3=list(filter(countletter,names))
print(result3)






