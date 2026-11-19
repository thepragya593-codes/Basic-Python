#q1
"""f = open("poem.txt")
text = f.read()
print(text)
find =text.find("twinkle")
print(find)
f.close()"""

#q2
"""import random

def game():
    print("You are playing the game!!")
    score =  random.randint(1,62)
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0


    print(f"Your score:{score}")
    if(score > hiscore):
        with open("hiscore.txt", "w") as f :
              f.write(str(score))

    return score

game()
"""

#q3
"""def genTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)
for i in range(2,21):
    genTable(i)
"""

#q4
"""with open("animal.txt") as f:
    r = f.read()

new = r.replace("donkey","###")

with open("animal.txt" , "w") as w:
    w.write(new)
    """

#q5
"""list = ["spam","money" ,"free","buy"]
with open("list.txt") as f:
    r = f.read()

for word in list:
    r = r.replace(word,"####")
    
with open("list.txt" , "w") as f:
    f.write(r)
"""


#q6
"""word = "python"
with open("log.txt") as f:
    content = f.read()
if word in content:
    print("It contains.")
else:
    print("It does not contains.")
"""

#q7
"""word = "python"
with open("log.txt") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if( word in line):
        print("Yes it present in line:",lineno)
        break
    lineno +=1
else:
    print("No pyhthon is not present.")
"""
 #q8
"""with open("this.txt") as f:
    content = f.read()
with open("this2.txt" , "w") as f:
    f.write(content)"""

#q9
"""with open("this.txt") as f:
    content1 = f.read()

with open("poem.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print("yes they are same")
else:
    print("No these are not same")
"""
#q10
"""with open("poem.txt" , "w") as f:
    f.write("")"""
#q11
with open("log.txt") as f:
    content = f.read()

with open("renamedFile.txt", "w") as f:
    f.write(content)

# now by using os module we can delete old file lo.txt