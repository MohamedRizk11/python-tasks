"""

Build an email slicer : create a function that takes an email as input and retrieve the
username and domain of the email


"""
x=input("enter your email address :")
y=x.split("@")
print("your username is :",y[0])
print("your domain is :",y[1])


