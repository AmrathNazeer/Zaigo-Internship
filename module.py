#Creating Custom Modules
import main
""" Importing the main module in this module """
a=input("Enter your name :")
b=int(input("Enter your age :"))
main.myfunc(b)

#enuerate ()
print("Enumerate()")
fruits=["apple","banana","mango","sapota","pineapple","grapes"]
for i,fruit in enumerate(fruits):
    print(i,fruit)

#Zip ()
print("Zip()")
names= ['A','B','C','D']
height= [150,145,162,170]
print(list(zip(names,height)))

#sorted()
print("Sorted()")
marks=[95,45,78,83,62]
print(sorted(marks))
print(sorted(marks,reverse=True))
names=('sameera','rajesh','azees','karthika','zaithoona')
print(sorted(names))
print(sorted(names,reverse=True))


#Debug using Print()
print("Debug using Print()")
a = 10
b = 5
print("a =", a)
print("b =", b)
print(a / b)

#Using pdb(Python Debugger)
print("pdb")
import pdb
a = 10
pdb.set_trace()
b = 5
print(a + b)
