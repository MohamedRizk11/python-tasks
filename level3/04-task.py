"""

Currency converter : create a python script that takes a money with currency sign and
convert it to some other currencies , the code should be like the game we did before

"""

class currency:
    
    def __init__(self):
        while True:
            print(  """
            welcome in our company 
            1- to convert dollar to pound
            2- to convert pound to dollar
            """)
            user_choice=int(input("please enter number :"))

            if user_choice==1:
                self.dollartopound()
            elif user_choice==2:
                self.poundtodollar()
            
            d=int(input("""if you want to exit press 1
to do another convert press 2 """))
            if d==1:
                print("goodbye...")
                break



    def dollartopound(self):
        x=int(input("enter the amount of money :"))     
        print(x*31,"pound")
      
            
            

    def poundtodollar(self):
        x=int(input("enter the amount of money :"))     
        print(x/31,"dollar")
        d=int(input("""if you want to exit press 1
                 to do another convert press enter """))
        if d==1:
            print("goodbye...")


                       
h=currency()   




       
      
         
       