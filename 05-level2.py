"""
names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha"] 

Print a list contains the len of each word in the list using [normal list - list comprehension -
functional programming]

"""
names = ["mahmoud","farida","ali","hassan","mohamed","khaled","taha"] 

# normal list

for x in  names :
  print ( len(x))

# list comprehension

result1=[len(x) for x in names ]
print(result1)

# functional programming
def countlen(names):
    for x in names:
        print(len([x]))

countlen(names)        