#to check numbers
"""
num=-3
if num>0:
    print("number is positive")
elif num<0:
    print("number is negetive")
elif  num==0:
 print("neutral number")
else:
    print("enter a valid number")
    """

    #taking user input
"""""
num2=input("enter a number")

if int(num2)<0:
    print("negative")
elif int(num2)>0:
    print("positive")
else:
    print("number is zero")
    """

    #taking user input through CLA
""""

import sys

date1=float(sys.argv[1])

if date1==5.11:
    print("guddu's birthday")
elif date1==14.06:
    print("bhai's birthday")
elif date1==18.11:
    print("manu's birthday")
else:
    print("entear a valid date")
    """

#for AWS Instance
""""
import sys
instance_type=sys.argv[1]

if instance_type=="t2.micro":
    print("You are eligible for a free tier instance")
elif instance_type=="t2.medium":
    print("it will cost you $2")
elif instance_type=="t3.large":
    print("it will cos you $4")
else:
    print("enter a valid instance type")

"""

#username_password
""""
import sys
username=sys.argv[1]


if username=="ashu"  :
    print("you have logged in")
else:
    print("enter valid details")
"""

#find maximum b/w two numbers
import sys

a=float(sys.argv[1])
b=float(sys.argv[2])

if a>b: #use < to find minimum number
    print(a)
else:
    print(b)