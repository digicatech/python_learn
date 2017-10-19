#!/usr/bin/python3
import sys

#String variables
#====================================
name = "John"
surname = "Snow"
print(name)
print('Welcome ' + name +' '+surname)
print (name[0]) 
print (name[0:2]) # Substring
print (name[2:]) # Prints name starting from 3rd character
print(name * 3) # Prints name three times

#Numeric variables
#====================================
#integer variable
a = 17
print(a)
#floating point variable
miles   = 1000.0
print(miles)


#Multiple Assignment
k = i = 1
print(k)
print(i)

#list types
#====================================

mylist = ["John" , 5 , 10.2]
mylist2 = ["Michael","Sarah"]
print(mylist[0])
print(mylist[1:3])
print(mylist[1:])
print(mylist * 2)
print(mylist + mylist2)
mylist3 = mylist + mylist2
print(mylist3[4])

#tupples (read only lists)
#====================================
mytupple = ["John" , 5 , 10.2]
mytupple2 = ["Michael","Sarah"]
print(mytupple[0])
print(mytupple[1:3])
print(mytupple[1:])
print(mytupple * 2)
print(mytupple + mytupple2)
mytupple3 = mytupple + mytupple2
print(mytupple3[4])

#dictionary (like json)
#====================================
dict = {}
dict["name"] = "John Snow"
dict["age"] = 30
print(dict)
print(dict["name"])

#Data Type Conversion
#====================================
#Type check
myStr = "my test string"
print(type(myStr))  #import sys

if type(myStr) != str:
    print("variable is not string")
else:
    print("variable is string")

