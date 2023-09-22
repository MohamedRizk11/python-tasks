"""
Create a function that takes x,y and prints all the number that can be divide by y from x to 100

"""

x = int(input("enter first number :"))
y = int(input("enter secound number :"))
for c in range(x,100):
    if c%y==0:
        print (c)