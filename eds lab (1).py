Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> mass = float(input("Enter mass in kilogram" : ))
SyntaxError: invalid syntax
>>> velocity = (int(input("Enter velocity in m\s"))
... momentum = mass * velocity
...             
SyntaxError: '(' was never closed
>>> print("The momentum is : ",momentum)
...             
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print("The momentum is : ",momentum)
NameError: name 'momentum' is not defined
>>> mass = float(input("Enter mass in kilogram"))
...             
Enter mass in kilogram12
>>> velocity = int(input("Enter velocity in m\s"))
...             
Enter velocity in m\s12
>>> print("The momentum is : ",momentum)
...             
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print("The momentum is : ",momentum)
NameError: name 'momentum' is not defined
>>> momentum = mass * velocity
...             
>>> mass = float(input("Enter mass in kilogram"))
...             
Enter mass in kilogram12
>>> velocity = int(input("Enter velocity in m\s"))
...             
Enter velocity in m\s12
>>> momentum = mass * velocity
...             
>>> print("The momentum is : ",momentum)
...             
The momentum is :  144.0
>>> 
>>> 
>>> import math
>>> n = int(input("Enter a number : "))
Enter a number : 8
>>> if 0 <= n < 10:
...     print("square of n : ", n*n)
... elif 10 <= n <100:
...     print("square root of n : ", math.sqrt(n))
... elif 100 <= n < 1000:
...     print("cube root of n : ", n**(1/3))
... else:
...     print("Please enter a number between 1 to 1000")
... 
...     
square of n :  64
>>> square of n :  64
SyntaxError: invalid syntax
