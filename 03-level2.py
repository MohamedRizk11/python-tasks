"""
names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha"]
Get the names that starts with t in a list using [normal list - list comprehension - functional
programming]

"""
names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha"] 
startword=""
# normal list
result1=[]

for x in names:
    if x[0]==startword:
        result1.append(x)
print (result1)  

# list comprehension

result2=[x for x in names if x[0].lower()== startword.lower()]
print(result2)

# functional programming
def filterword(n):
    if  n[0]==startword:
        return n
    
result3=list(filter(filterword,names))
print(result3)


    