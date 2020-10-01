
# coding: utf-8

# 78   Integer
# 21.98 float
# 'Q' character
# 'hello' string

# In[ ]:


type (78)


# In[ ]:


type(21.8)


# In[ ]:


type(21.88)


# In[ ]:


type('q')


# In[ ]:


type('ishan')


# variables

# In[ ]:


#integer
type(-10)


# In[ ]:


int(12.345)


# In[ ]:


int('123')


# In[ ]:


float(12.3467890909035400)


# In[ ]:


#boolean True False == != <= >=
type(True)


# In[ ]:


type(False)


# In[ ]:


5==4


# In[ ]:


5==5


# In[ ]:


#string
d = 'hello world'
c = 'hi'
print(d)
print(c)


# In[ ]:


str(1.2)


# In[ ]:


'hello ' + 'world'


# In[ ]:


#print
print('abc')


# In[ ]:


print('hello')
print('world')
print('good bye')


# In[ ]:


#end key word
print('hello', end=' ')
print('world', end=' ')
print('good bye')


# In[ ]:


#giving values to variables
c = 1
d = 2
e = 3
print(c)
print(d)
print(e)


# In[ ]:


p=q=100
print(p,q)


# In[ ]:


#scope of a variable


# In[ ]:


#write a program to swap two numbers
a = 5
b = 7
temp = a
a = b
b = temp
print(a,b)


# In[ ]:


#swap two numbers without using third variable
a = 8
b = 9
a,b=b,a
print(a,b)


# In[ ]:


#write a program to calculate area of rectangle
length = 10
width = 20
area = length * width
print(area)


# In[ ]:


#input function
a = input()
b = input()
print(a,b)


# In[ ]:


l = int(input())
w = int(input())
area = l*w
print(area)


# In[ ]:


x = input()
print('entered number is: ', x)
print('type of x is: ')
print(type(x))


# In[ ]:


x = int(input())
print(x)
print(type(x))


# In[ ]:


#write a program to calculate area of rectangle by taking input from user


# In[ ]:


#write a program to calculate the area of a circle
radius = int(input())
pi = 3.14
area = pi * radius
print(area)


# In[ ]:


format(area, '.3f')


# In[ ]:


#inbuilt function
#abs returns absolute value of x
abs(-2)


# In[ ]:


abs(2.2)


# In[ ]:


#max
max(1,2,3,4,5)


# In[ ]:


#min
min(1,2,3,4,5)


# In[ ]:


#pow
pow(2,3)


# In[ ]:


#round
round(10.3)


# In[ ]:


round(10.6)


# In[ ]:


round(10.5)


# In[ ]:


#ceil
import math
a = 10.23
math.ceil(a)


# In[ ]:


math.ceil(10.89)


# In[ ]:


math.floor(10.78)


# In[ ]:


math.floor(10.11)


# In[ ]:


math.sqrt(9)


# In[ ]:


# ord and chr
ord('a')


# In[ ]:


ord('A')


# In[ ]:


chr(97)


# In[ ]:


chr(65)


# In[ ]:


#write a program to add two number
#write a profram to subtract two numbers
#write a program to miltiply two numbers
#write a program to divide two numbers


# In[ ]:


7/2


# In[ ]:


7//2


# In[ ]:


#Modulo %
10 % 4


# In[ ]:


10 % 2


# In[ ]:


1234 % 10 


# # write program to reverse any four digit number

# In[ ]:


num =int(input())
r = num%10 # 1234 = 4
q = num//10 # 1234 = 123
r = (r * 10)+(q % 10) # 40 + 3 = 43
q = q//10 # 123 = 12
r = (r*10)+(q%10) # 430 + 2 = 432
q = q//10 # 1
r = (r*10)+(q%10) # 4320 + 1
print(r)


# In[ ]:


#not operator
True


# In[ ]:


not True


# In[ ]:


# and operator & |
True and True


# In[ ]:


True and False


# In[ ]:


# or operator 
True or True


# In[ ]:


True or False


# In[ ]:


False or True


# In[ ]:


False or False


# In[ ]:


a = 2
b = 2
a==b


# In[ ]:


#if statement


# In[ ]:


#write a program to check if two numbers have same value
num1 = int(input())
num2 = int(input())
if(num1==num2):
    print('equal number')


# In[ ]:


#write a program, if radius is greater than zero 
#then find out area and circumference of circle


# In[ ]:


#if-else
#write program to find greater number between two numbers
num1 = int(input())
num2 = int(input())
if num1>num2:
    print('num1 is greater')
else:
    print('num2 is greater')


# #greater number between three numbers
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# if (num1>num2 and num1>num3):
#     print('num1 is greater')
# elif (num2>num3):
#     print('num2 in greater')
# else:
#     print('num3 is greater')

# In[1]:


num1 = int(input())
num2 = int(input())
num3 = int(input())
if (num1>num2 and num1>num3):
    print('num1 is greater')
elif (num2>num3):
    print('num2 in greater')
else:
    print('num3 is greater')


# In[ ]:


a = int(input())
b = int(input())
c = a*b
print(c)


# In[ ]:


2**2**2


# In[ ]:


print("hello world")

