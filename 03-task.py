"""
Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y

"""
c =int(input("enter first number x :"))
b =int(input("enter first number y :"))
for x in range(c,b+1):
    for y in range(0,13):
        print(f"{x} X {y} ={x*y}")    

    print("----------------")    