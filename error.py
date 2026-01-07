# class NegativeError(Exception):
#     pass
# class ZeroError(Exception):
#     pass
# try:
#     num=int(input('enter a positive integer:'))
#     if (num<0):
#         raise NegativeError
#     elif (num==0):
#         raise ZeroError
#     else:
#         print("The entered positive integer is=",num)
# except NegativeError:
#     print('You have entered negative value')
# except ZeroError:
#     print('you have entered zero value')

try:
    n=int(input('enter a number:'))
    res=n/100
except ValueError:
    print("The entered number is not a number" )
except ZeroDivisionError:
    print("zero is not divided by any number")
else:
    print("the result is ",res)

try:
    with open("notes.txt","r") as f:
        con=f.read()
        print(con)
except FileNotFoundError:
    print("file not found ")

class NegativeError(Exception):
    pass
try:
    marks=int(input("enter a number:"))
    if marks<0:
        raise NegativeError
    else:
        print("the marks is ",marks)
except NegativeError:
    print("The entered Marks is less than 0")

