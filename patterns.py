#q1
# * * * * *
# * * * * *
# * * * * *
"""
n = 5
for i in range(n):
    for j in range(n):
        print("*" , end=" ")
    print()
"""
#q2
"""*
   * *
   * * *
"""
#q2 Increasing triangle
"""
n = 5
for i in range(n):
    for j in range(i +1):
        print("*", end=" ")
    print()
"""

#q3 Decreasing Triangle
"""
n = 5
for i in range(n):
    for j in range(i,n):
        print("*" , end = " ")
    print()
"""

#q4 - Right Side Triangle
"""
n = 5
for i in range(n):
    for j in range(i,n):
        print(" " , end = " ")
    for j in range(i+1):
        print("*",end=" ")
    print()
"""

#q5 - Left Side Triangle
"""
n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end= " ")
    for j in range(i,n):
        print("*",end=" ")
    print()
"""
#q5 - Hill Pattern
"""
n = 5
for i in range(n):
    for j in range(i,n):
        print(" " , end = " ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")     
    print()
"""
#q6 - Reverse Hill Pattern
"""
n= 5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    print()
"""
#q7 - Diamond Pattern
n = 5
for i in range(n-1):
    for j in range(i,n):
        print(" " , end = " ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")

    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")     
    for j in range(i,n):
        print("*",end=" ")
    print()