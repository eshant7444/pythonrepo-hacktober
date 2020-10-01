
# coding: utf-8

# In[2]:


#WAP to display a message "welcome to functions", by creating a function.
def Display():
    print("welcome to functions")
Display()


# In[6]:


#write a program to print message, by taking name from user.
def print_msg():
    str = input("enter your name ")
    print("Dear ",str,"Welcome to functions")
print_msg()


# In[ ]:


#Reason why we need functions.
sum = 0
for i in range (1,26):
    sum = sum + i
print(sum, end = " ""\n")
sum = 0
for i in range (50,71):
    sum = sum + i
print(sum, end= " ")


# In[13]:


#same question using functions:
def rangesum(x,y):
        s = 0 
        for i in range(x,y+1):
            s = s + i
        print(s)
rangesum(100,125)
rangesum(150,170)


# In[ ]:


rangesum(50,63)


# In[ ]:


# Parameters and arguments in a function
'''
parameters = formal parameters
arguments = actual parameters
'''


# In[4]:


def printmax(n1,n2):
    if(n1>n2):
        print("n1 is greater")
    else:
        print("n2 is greater")
printmax(10,20)


# In[ ]:


printmax(20,12)


# In[ ]:


# positional arguments
def display(name,age):
    print("name is: ",name,"age is: ", age)
display('ishan',29)


# In[ ]:


def display(name,age):
    print("name: ", name, "age: ", age)
display('ishan')


# In[ ]:


#keyword arguments
def display(name,age):
    print("name: ", name, "age: ", age)
display(age = 20, name = 'saurav')


# In[ ]:


def display(name, age):
    print("name: ", name, "age: ", age)
display(age=29,'ishan')


# In[ ]:


display('ishan',age=29)


# In[ ]:


#parameters with default values
def greet(name,msg='welcome to functions'):
    print('hello', name, msg)
greet('ishan')


# In[ ]:


greet('ishan','welcome to LPU')


# In[ ]:


#WAP to find area of a circle using function
def areacircle(r,pi=3.14):
    area = pi*r*r
    print(area)
areacircle(5)


# In[ ]:


#local and global variables

p = 20   #global var
def demo():
    q = 10   #local var
    print(q)
    print(p)
demo()
print(p)
#print(q)


# In[ ]:


#try to access local var outside function
def demo():
    q = 15
    print(q)
demo()
print(q)


# In[ ]:


# return statement

#write a program to return a minimum of two numbers.
def minimum(a,b):
    if a<b:
        return a
    elif b < a:
        return b
    else:
        return "both the numbers are equal"
minimum(100,85)


# In[9]:


#WAP to find distance between two points. 
# ((x2-x1)**2 + (y2-y1)**2)**0.5

def distance(x1,x2,y1,y2):
    dx = (x2-x1)**2
    dy = (y2-y1)**2
    d = (dx + dy)**0.5
    return d
distance(12,4,18,10)


# In[ ]:


def distance(x1,x2,y1,y2):
    dx = (x2-x1)**2
    dy = (y2-y1)**2
    d = (dx + dy)**0.5
    return d
a = int(input())
b = int(input())
c = int(input())
d = int(input())
distance(a,b,c,d)


# In[2]:


#WAP that returns the following output
'''
if d > 0: equation has two real roots
if d = 0: equation has one real root
if d < 0: equation has two complex roots
'''
# formula:  ax**2 + bx + c, d = b**2 - 4ac

def quad_d(a,b,c):
    d = b**2 - 4 * a * c
    if d > 0 :
        return 'equation has two real roots'
    elif d < 0:
        return 'equation has two complex root'
    else:
        return 'euation has one real root'
quad_d(1,2,5)


# In[7]:


# returning multiple values
def plus(num1,num2):
    return num1+num2,num1-num2
plus(10,5)


# In[4]:


# assign returned multiple values to variable(s)
def demo(num1):
    return num1**2,num1**3
square, cube = demo(4)
print(square,cube)


# In[1]:


# recursive function
#calculate the factorial of a number using recursion

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)
fact(5)


# In[5]:


x = int(input())
y = x//2
def prime(x,y):
    c = 0
    for i in range(2,y+1,1):
        if (x%i==0):
            c += 1
    if c == 0:
        print('prime')
    else:
        print('not prime')
prime(x,y)


# In[3]:


a = 5
b = 5
a is b


# In[3]:


b is a


# In[4]:


id(a)


# In[5]:


id(b)


# In[30]:


p = input()
q = input()
print(p,q)


# In[31]:


id(p)


# In[32]:


id(q)

