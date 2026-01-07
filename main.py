class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("ramya",21)
p2=person("amra",22)
print(p1.name,p2.age)

#BUILT-IN-MODULES
import math,random
print("Built-in Modules")
print(math.sqrt(5))
print(math.pow(2,5))
print(math.sin(3))
print(random.randint(1,100))

#creating a own module
def myfunc(x):
    if x>=18:
        print("You are eligible to Vote")
    else:
        print("You are not eligible to Vote")

