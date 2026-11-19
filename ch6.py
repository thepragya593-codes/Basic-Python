#q1
"""a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))
d = int(input("Enter 4th number:"))

if (a>b and a>c and a>d ):
    print("A is greater.")
elif(b>a and b>c and b>d):
    print("B is greater.")
elif(c>a and c>b and c>d):
    print("C is greater.")
elif(d>a and d>c and d>b):
    print("D is greater.")"""

#q2
"""m1 = int(input("Enter marks of subject 1:"))
m2 = int(input("Enter marks of subject 2:"))
m3 = int(input("Enter marks of subject 3:"))

total = (((m1+m2+m3)/300)*100)

if(total>40):
    if(m1 <33 or m2 <33 or m3 <33):
        print("You failed because you scored less than 33 in subject.")
    else:
        print("You passed in all subjects!")
else:
    print("Try next year!!!")"""

#q3
"""msg = input("Enter a msg:")
if(msg == "Make a lot of money " or msg =="buy now" or msg =="subscribe this"or msg =="click this"):
    print("It is spam!!")
else:
    print("You are safe..")    """
# we can use in also to solve this question.

#q4
"""username = input("Enter your username:")

if(len(username)<10):
    print("Your username is short..Add more words")
else:
    print("Fine..") """ 

#q5
"""m1 = int(input("Enter marks of subject 1:"))
m2 = int(input("Enter marks of subject 2:"))
m3 = int(input("Enter marks of subject 3:"))

total = (((m1+m2+m3)/300)*100)
print(f"{total:.2f}")

if(total == 100 and total >=90):
    print("Excellent..")
elif(total<90 and total >=80):
    print("A Grade")    
elif(total<80 and total >=70):
    print("B Grade")    
elif(total<70 and total >=60):
    print("C Grade")    
elif(total<60 and total >=50):
    print("D Grade") 
else:
    print("F")   """

#q7
"""post = input("Enter a post:")

if(post.find("Hary")):
    print("This post talks about Harry!!")
else:
    print("No..")"""

