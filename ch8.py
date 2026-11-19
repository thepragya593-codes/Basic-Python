#q1
"""def greatest(a,b,c):
    if(a>b and a>c):
        print("A is Greater.")
    elif(b>a and b>c):
        print("B is greater.")
    else:
        print("C is greater.")

x = int(input("Enter 1st no.:"))
y = int(input("Enter 2nd no.:"))
z = int(input("Enter 3rd no.:"))
greatest(x,y,z)
"""
#q2
"""def degree(c):
   f = ((c*9/5)+32)
   print(f)

a = int(input("Enter the tempertature in Celcius:"))
degree(a)"""
     
#q4
# x = int(input("Enter the last term:"))
# sum = 0
# for i in range(1,x+1):
#     sum = sum +i
# print(sum)
"""def sum(n):
    total = 0
    for i in range(1,n+1):
        total = total + i
    print(total)

x = int(input("Enter the last term:"))
sum(x)"""

"""def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

x = int(input("Enter the last term:"))
total = sum(x)
print(total)"""

#q5
"""def pattern(n):
    for i in range(n):
        for j in range(i,n):
            print("*" ,end = " ")
        print()

x = int(input("Enter no. of rows:"))
pattern(x)"""

#q7
def clean(l,word):
   l1 = []

   for item in l:
        if item != word:
            l1.append(item.strip())
    
   return l1

list =[" Apple " , "   Mango", "  orange  "]
print(clean(list,"Mango"))

    



#q8
"""def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")


x = int(input("Enter the number:"))
table(x)"""


