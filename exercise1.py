# # Print numbers from 1 to N
# n=int(input("Enter the number :"))
# for i in range(1,n+1):
#     print(i)
# Print all even numbers in a list
l=[21,53,53,8,8,9,10,22,34,21,53,81]
b=[]
for i in range(len(l)):
    if l[i]%2==0:
        b.append(l[i])
print(b)

# Find the sum of elements in a list
s=0
for i in range(len(l)):
    s=s+l[i]

print(s)

# # Find the largest number in a list
big=l[0]
for i in l:
    if i>big:
        big=i
print(big)

# # Count how many times a number appears in a list
for i in range(len(l)):
    count=1
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            count=count+1
    print(l[i],'appears',count,'times')

#find the smallest number in a list
li=[22,34,56,78,14,10]
small=li[0]
for i in li:
    if i<small:
        small=i
print(small)

#reverse the number from a list
#Input: [1, 2, 3, 4]
#Output: [4, 3, 2, 1]
s=[1,2,3,4]
c=[]
for i in range(len(s)-1,-1,-1):
     c.append(s[i])
print(c)

#using function to check username and password
def check(x,y):
    a = "admin"
    b = 1234
    if x==a and y==b:
        print("your Login Successful")
    else:
        print("Invalid Login Credentials")

username=input("Enter your username: ")
try:
    password=int(input("Enter your password: "))
    check(username, password)
except ValueError:
    print("Invalid Data Type, using only digits")


#remove duplicates from the list
t=[1,2,2,3,4,4,5,6,7,8,9]
t1=[]
for i in t:
    if i  not in  t1:
        t1.append(i)
print(t1)

#print the greatest number using function
def great(a,b):
    if a>b:
        print("A is greatest")
    elif b>a:
        print("B is greatest")
    else:
        print("Both are Equal")

x=int(input("Enter a number :"))
y=int(input("Enter another number :"))
great(x,y)


#count the no of vowels in a given string using  function
def vowel(a):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    c=[]
    count=0
    for i in range(len(a)):
        if  a[i] in vowels:
            c.append(i)
            count=count+1
    print("the number of vowels in your string is:",count)

str=input("Enter a string :")
vowel(str)