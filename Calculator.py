#normal
num1=10
num2=20
add=num1+num2
print("Addition is - " + str(add))
sub=num1-num2
print("substraction is - " + str(sub))
mul=num1*num2
print("multiplication is - " + str(mul))
div=num1/num2
print("division is - " + str(div))

#using function
num3=input("enter your first number :")
num4=input("enter your second number :")
def add1():
    addition=int(num3)+int(num4)
    print("Addition is : ",addition)
def sub1():
    substraction=int(num3)-int(num4)
    print("substraction is :", substraction)
def mul1():
    multiplication=int(num3)*int(num4)
    print("multiplication is :", multiplication)
def div1():
    division=int(num3)/int(num4)
    print("division is :", division)

add1()
sub1()
mul1()
div1()
