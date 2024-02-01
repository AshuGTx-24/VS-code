"""import Calculator as basic_calc

basic_calc
"""

#percentage calculator
"""numb1=540
numb2=20
percentage=numb1/100*numb2
print(percentage)
"""

#taking user input
"""numb3=input("enter your total number :")
numb4=input("enter the percent you want :")
def percentage1():
    percent=int(numb3)/100*int(numb4)
    print("percentage is :" , percent)

percentage1()
"""
#way2
"""
def percentage2(numb5,numb6):
    percent1=int(numb5)/100*int(numb6)
    return percent1
print(percentage2(input("enter your total number :"), input("enter percent :")))
"""

#calculator using commnad line argumrnts
"""""

import sys
def addition(num1,num2):
    add=num1+num2
    return add
def substraction(num1,num2):
    sub=num1-num2
    return sub
def multiplication(num1,num2):
    mul=num1*num2
    return mul
def division(num1,num2):
    div=num1/num2
    return div
num1=float(sys.argv[1])
operation=sys.argv[2]
num2=float(sys.argv[3])
if operation=="add":
    output=addition(num1,num2)
    print(output)

if operation=="sub":
    output1=substraction(num1,num2)
    print (output1)

if operation=="mul":
    output2=multiplication(num1,num2)
    print(output2)

if operation=="div":
    output3=division(num1,num2)
    print(output3)
    """

#enviroment variables
#import os
#print(os.getenv("password"))

#operators
a=5
b=6
sum=a+b
sub=a-b
prod=a*b
div=a/b
print(sum)
print(sub)
print(prod)
print(div)
comp1=a>b
comp2=a<b
comp3=a<=b
comp4=a>=b
comp5=a==b
comp6=a!=b
print(comp1)
print(comp2)
print(comp3)
print(comp4)
print(comp5)
print(comp6)

total = 10

total += 5
total -= 3
total *= 2
total /= 4

print("Final total:", total)
   
   
