"""

Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in
the x,y range



"""


c =int(input("enter first number x :"))
b =int(input("enter first number y :"))
for x in range (c,b):
    if x %2==0:
        print("even")
    else:
        print("odd")  