#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

print("J" in name) #True
print("k" in name) #False
print("k" not in name) #True

print("My name is %s %s. And I am %i years old."%(name , surname , 28))  #string format

print(u"unicode string...")
print("çarşı her şeye karşı".encode(encoding='utf_8'))
print("my test string".capitalize()) #capitalize first char

#String interpolation
#====================================
print(f"Hello , {name}")


#Numeric variables
#====================================
#integer variable
a = 17
print(a)
#floating point variable
miles   = 1000.0
print(miles)

print(int("15"))
print(float("12.5"))


#Multiple Assignment
k = i = 1
print(k)
print(i)
del k  #delete variable

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

#tuples (read only lists)
#====================================
mytuple = ["John" , 5 , 10.2]
mytuple2 = ["Michael","Sarah"]
print(mytuple[0])
print(mytuple[1:3])
print(mytuple[1:])
print(mytuple * 2)
print(mytuple + mytuple2)
mytuple3 = mytuple + mytuple2
print(mytuple3[4])
print('John' in mytuple)
print('John' in mytuple2)
print('John' in mytuple3)
for val in mytuple3:
    print(val)
print(len(mytuple3))
print(tuple(mylist3)) #converts list to tuple
del mytuple3
try:
    print(mytuple3) #error
except Exception as e:
    #print("hata" +  str()
    print(e)
finally:
    print("and finally ...")

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

