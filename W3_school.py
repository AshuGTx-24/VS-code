if(5>2):
 print("five is greater than two")
 x=5
 y="hello world!"
 print(x, y)
 y=5
 y="ashu"
 print(y)
 a=6
 b="ashu"
 print(type(a))
 print(type(b))
 #variable names
 my_variable="snake casin"
 _myvariables="john"
 MyVariable="pascal casing"
 myVariableName="camal casing"
 #python allows us to assign multiple values to multiple variables in one line
 x1,y1,z1="apple","mango","orange"
 print(x1)
 print(y1)
 print(z1)
 print(x1,y1,z1)
 #same values to multiple variables
 x2=y2=z2="dragon fruit"
 print(x2)
 print(y2)
 print(z2)

 #unpacking
 fruits="apple","orange","mango"
 x3,y3,z3=fruits
 print(x3)
 print(y3)
 print(z3)
 #output variables
 x4="ashu"
 y4="gudu"
 z4=5
 print(x4+y4+str(z4))

 #global variables
 x5="awesome"
 def myfun():
   print("python is " + x5)
myfun()
#local variable
x6="awesome"
def myfun1():
  x6="fantastic"
  print("python is" + x6)
myfun1()
