#q1
class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,lang):
        self.name = name
        self.salary = salary
        self.lang = lang

h = Programmer("Harry" ,120000,"py")
# a = Programmer("Aman", 1200000,"java")
print(h.name, h.salary,h.lang)


#q2
"""class Calculator:
    def square(self,a):
        print("The sqaure is:",a*a)
    def cube(self,a):
        print("The cube is:",a*a*a)
    def sqrt_root(self,a):
        print("The square root is:",a*1/2)

x = int(input("Enter a number:"))
b = Calculator()
b.cube(x)
b.square(x)
b.sqrt_root(x)
"""

#q3
"""class Test:
    a = 100

x = Test()
# print(x.a)
x.a = 0
print(x.a)
"""
#q4
"""class Calculator:
    def square(self,a):
        print("The sqaure is:",a*a)
    def cube(self,a):
        print("The cube is:",a*a*a)
    def sqrt_root(self,a):
        print("The square root is:",a*1/2)
    @staticmethod     
    def greet(): 
        print("Hello user")

x = int(input("Enter a number:"))
b = Calculator()
b.greet()
b.square(x)
b.cube(x)
"""
# q5
"""from random import randint
class Train:
    def bookTicket(self,trainNo,fro,to):
        print(f"Ticket is booked in Train No.:{trainNo} from{fro} to {to}")

    def getStatus(self,trainNo):
        print(f"Train No.{trainNo} is running on time")
    def fareInfo(self,trainNo,fro,to):
        print(f"Ticket fare in train No. {trainNo} from{fro} to {to} is (randint(100,700))")

t = Train()

t.bookTicket(3445767,"Rampur","Panaji")
t.getStatus(3445767)
t.fareInfo(3445767,"Rampur","panaji")        
"""



#q6
"""class Calculator:
    def square(pragya,a):
        print("The sqaure is:",a*a)

x = int(input("Enter a number:"))
b = Calculator()
b.square(x)

yes it is working when we use pragya in place of self also...
"""