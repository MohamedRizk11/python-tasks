"""
Make a temperature/measurement converter. Write a script that can convert
Fahrenheit to Celcius and back, or inches to centimeters and back, etc in 3 different
ways


"""
# way 1 
d = int(input("""1 : Fahrenheit to Celcius
2 : Celcius to Fahrenheit
3 : inches to centimeters
4 : centimeters to inches
enter number to calculate :"""))


if d==1:
    f=int(input("enter degre in Fahrenheit :"))
    for c in range (1):
        c=(f-32)*5/9
        print(c)
elif d==2:
    c=int(input("enter degre in Celcius :"))
    for f in range (1):
        f=c*9/5+32
        print(f)
elif d==3:
    i=int(input("enter degre in inche :"))
    for c in range (1):
        c=i*2.54
        print(c)
elif d==4:
    c=int(input("enter degre in centimeter :"))
    for i in range (1):
        i=c/2.54
        print(i)     
else:
    print("please choose number")          


# way 2
degre={'first':30,'sec':60}
res={k:v*2.54 for (k,v) in degre.items()}
print("result in cm ",res)


# way 3

class calc:
    def ftoc(f):
        return (f-32)*5/9
    def ctof(c):
        return c*9/5+32
    
d=calc.ftoc(62)
f=calc.ctof(30)
print(d)
print(f)
