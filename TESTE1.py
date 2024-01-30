text="hi how are you!!"
length=len(text)
print("length of text is : ", length)
#replace text
text1="ashutosh is unemployed"
new_text=text1.replace("unemployed","focusing")
print("new text is:", new_text)
text2=new_text.replace("employed", "focusing")
#strippedtext
text3="   hi  how are you  "
stripped_text=text3.strip()
print("new text is:", stripped_text)
#keywords=learn almost 26 keywords
#variables= dynamic programming
full_name="ashutosh mohanty" #full_name is the variable
print(full_name)
#2 types variables= 1 is global and 2 is local
#global= placed outside the function
num1=2
num2=5
addtion=(num1+num2)
print("addition is:", addtion)
substraction=(num2-num1)
print("sub is :", substraction)
#calculator programme

num3=input("enter your number:")
num4=input("enter your number:")
result1=(int(num3)+int(num4))
result2=(int(num3)-int(num4))
result3=(int(num3)%int(num4))
result4=(int(num3)*int(num4))
print("add is:",result1)
print("sub is:",result2)
print("div is :", result3)
print("multi is :",result4)