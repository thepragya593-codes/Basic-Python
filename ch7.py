# quick Quiz 1
"""list = ["apple", 'banana', "grapes", "orange"]

lenght = len(list)
i = 0
while (i<lenght):
    print(list[i])
    i = i+1"""

#q1
"""n = int(input("Enter a number:"))
for i in range(1,11):
    print(n*i)"""

#q2
"""l = ["Harry", "Soham", "Sachin", "Rahul"] 
for name in l:
    if(name.startswith("S")):
        print("Hlo",name)
"""

#q3
"""n = int(input("Enter a number:"))
i = 1
while(i<=10):
    print(n*i)
    i = i+1"""

#q4
"""n = int(input("Enter a number:"))
i = 2
while(i<n):
    if(n% i == 0):
       print("It is not prime number!") 
       break
    i = i+ 1
else:
    print("It is prime number")"""

#q5
"""n = int(input("Enter last term:"))
i = 1
sum = 0
while(i<=n):
    sum = sum +i
    i = i +1
print(sum)"""

#q6
"""n = int(input("Enter a number:"))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)"""

#q7
 #    * 
   # *** 
   #***** for n = 3 
"""n=4
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ") 
for j in range(1,2*i-1):
    print("*", end=" ")
print()    """ 

#q9
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i == 1 or i == n or j ==1 or j==n):
            print("*",end = " ")
        else:
            print(" ", end =" ")   
    print()
