#q1
"""class TwoDvector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(f"{self.x}i + {self.y}j")

class ThreeDvector(TwoDvector):
    def __init__(self,x,y,z):
        super().__init__(x, y)
        self.z = z
    def show(self):
        print(f"{self.x}i + {self.y}j + {self.z}k")

o1 = TwoDvector(1,2)
o1.show()
o2 = ThreeDvector(1,2,3)
o2.show()
"""
#q2
"""class Animal:
    def __init__(self):
        print("Animal makes sound!!")
class Pets(Animal):
    def __init__(self):
        # super().__init__()
        print("Pets make soft sound!!")
class Dog(Pets):
    def __init__(self):
        # super().__init__()
        print("Bark Bark!!")

a1 = Animal()
d1 = Dog()
OR
class Animal:
    pass
class Pets(Animal):
    pass
class Dog(Pets):
    @staticmethod
    def bark():
       print("Bow Bow")

d= Dog()
d.bark()
"""

#q3
"""class Employee:
    salary = 5678
    increment = 20
    @property
    def salaryAfterincrement(self):
        return (self.salary  + self.salary *(self.increment/100))

    @salaryAfterincrement.setter
    def salaryAfterincrement(self,salary):
        self.increment = ({salary/self.salary}-1)*100

    
e= Employee()
# e.salary = 55767
# e.increment = 5
# print(e.sAI)
e.salaryAfterincrement = 280
print(e.increment)

"""
#q4
"""class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
    def __add__(self,c2):
        return Complex(self.r + c2.r ,self.i + c2.i)
    
    def __mul__(self,c2):
        real = self.r *c2.r  - self.i *c2.i
        imag = self.r *c2.i  + self.i *c2.r
        return Complex(real,imag)

    
    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(1,2)
c3 = Complex(2,1)
print(c1 + c3)
print(c1 * c3)

"""

#q5
"""class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
         result = Vector(self.x + other.x , self.y + other.y , self.z + other.z)
         return result
    
    def __mul__(self,other):
         result = (self.x * other.x + self.y * other.y + self.z * other.z)
         return result
    
    def __str__(self):
        return f"{self.x}i , {self.y}j, {self.z}k"

v1 = Vector(1,2,3)
v2 = Vector(3,2,3)
v3 = Vector(4,2,3)
print(v1 + v2)
print(v1 * v2)
"""
#q6
"""class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        print( f"{self.x}i + {self.y}j + {self.z}k")

v1 = Vector(1,2,3)
v1.__str__()
"""
#q7
class Vector:
    def __init__(self,l):
        self.l = l
    
    def __len__(self):
        return len(self.l)
    

v1 = Vector([1,2,3])
print(len(v1))
