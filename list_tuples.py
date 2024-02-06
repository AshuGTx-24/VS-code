#list=use to store multiple value/element to a single variable

students_name=["ashu","jim","harry","brook"]
print(type(students_name))
print(students_name)

#tuples=are also list but are immutable in nature

students=("jack","jimmy","elly","green")
print(type(students))
print(students)

#to check the lenght of any list/tuple
fruits=("orange","apple","amngo") #tuple
print(len(fruits))
print(fruits)

animals=["cow","monkey","tiger","elephant"]
print(len(animals))
print(animals)

#indexing

s3_bucket_name=["web_bucket","app_bucket","server_bucket","development_bucket"]
#print(s3_bucket_name[3])
#print(s3_bucket_name[0:2]) #slicing of list where upper range doesn't count

s3_bucket_name.append("programme_bucket")
print(s3_bucket_name)
s3_bucket_name.remove("app_bucket")
print(s3_bucket_name)

#sorting
number=[1,5,9,11,67,34,2,10]
number.sort()
print(number)

#conactenation
variable=["s3_bucket","ec2_instance","load balancing"]
print(variable[0] + "-----" + variable[2])