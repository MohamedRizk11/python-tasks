"""
Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can
be divided on x,y

"""


c =int(input("enter first number x :"))
b =int(input("enter first number y :"))
for x in range(1,100):
    if x%c==0 and x%b==0:
        print (x)
      