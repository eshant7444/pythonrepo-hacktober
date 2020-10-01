
# coding: utf-8

# In[1]:


#write a simple program 
class Demo:
    pass
D1=Demo() #object of the class Demo
#print(D1)
D1


# In[4]:


#write a program to create a simple class and print a message and also print the address of the instance of the class
class Myfirstprog:
    print('welcome to object oriented programming')
C=Myfirstprog()
#print(C)
C


# In[16]:


#adding attributes to a class
class Rectangle:
    lenght=0 #attribute length
    width=0 #attribute width
R1 = Rectangle() #object of a class
print(Rectangle.lenght) #access attribute length
print(R1.width) #access attribute width


# In[6]:


#assigning value to an attribute
#write a program to calculate the area of a rectangle by assigning the value to the attributes of a rectangle.
class Rectangle:
    length = int(input())
    width = int(input())
R2 = Rectangle()
#R2.length = int(input())
#R2.width = int(input())
print(R2.length * R2.width)


# self represents the instance of the class. self keyword helps to access the attributes and methods of the class. it binds attributes with given arguments.

# In[3]:


#self-parameter and adding methods to a class
#adding methods to a class
#self parameter
#write a program to create a method Display_Message() in a class and pass a message
class Methoddemo:
    def Display_message(self):
        print('welcome to methods in a class')
ob1 = Methoddemo() #object of the class
ob1.Display_message() #calling method


# In[5]:


#defining self-parameter and other parameters in a class method
class Circle:
    def Circle_area(self,radius):
        return 3.14*radius**2
ob2 = Circle()
print(ob2.Circle_area(5))


# In[25]:


#write a program to calculate the area of a rectangle. pass length and width of the rectangle to method.
class Rectangle1:
    def Area_rectangle(self,length,width):
        return length*width
ob3 = Rectangle1()
print(ob3.Area_rectangle(5,4))


# In[11]:


#self parameter with instance variable
class Practice:
    x = 5
    def show(self,x):
        #print(x)
        x=30
        print(x)
        print(x)
ob = Practice()
ob.show(50)


# In[37]:


#write a program to demonstrate the use of self with an instance variable to solve the problem of variable hiding
class Practice:
    x = 5
    def display(self,x):
        x = 30
        print(x)
        print(self.x)
ob = Practice()
ob.display(50)


# In[12]:


#self parameter with method
#write a program with two methods. call method 1 using method 2
class Self_demo:
    def method_a(self):
        print('now in method a')
        print('i am method a')
    def method_b(self):
        print('in method b calling methohd a')
        self.method_a() #calling method_a
a = Self_demo()
a.method_b() #calling method_b


# In[13]:


#display class attributes and methods
#dir(name of class)
#dir(instance of class)
#write a program to display the attributes present in a given class
class Displaydemo:
    #name = 'abc'
    #age = '10'
    def read(self):
        name = input('enter name of student')
        print(name)
        age = input('enter age of student')
        print(age)
d2 = Displaydemo()
d2.read()


# In[44]:


dir(Displaydemo)


# In[15]:


class Displaydemo:
    name = 'xyz';
    age = '20';
    def read(self):
        name = input('enter name of student')
        print(name)
        age = input('enter age of student')
        print(age)
d2 = Displaydemo()
d2.read()


# In[49]:


Displaydemo.__dict__


# In[50]:


class Demo2:
    pass
D8=Demo2()
dir(D8)


# In[1]:


#ACCESSIBILITY
#To make an attribute and a method private we need to add two two underscore in front of attribute and method.
class Person:
    def __init__(self):
        self.name = 'ishan' #public attribute
        self.__bankaccno = 10101 #private attribute
    def Display(self):
        print('name is:', self.name)
        print('bank acc no.:', self.__bankaccno)
P = Person()
print(P.name)
P.Display()
print(P.__bankaccno)
print(P._Person__bankaccno)
#P.Display


# In[12]:


#attributes and __init__ method
#we can initialise the value of a member variable or attribute by making use of the __init__ method.
class Circle:
    pi = 0 #attribute pi
    radius = 0 #attribute radius
    def __init__(self):
        self.pi = 3.14
        self.radius = 5
    def calc_area(self):
        print(self.radius)
        return self.pi*self.radius**2
c1 = Circle()
print(c1.calc_area())


# In[12]:


#__init__ constructor
#initialiser
#special method that is used to initialise the instance
#of an object
#method runs as an object of a class
class box:
    width=0
    height=0
    depth=0
    volume=0
    def __init__(self):
        self.width=5
        self.height=5
        self.depth=5
        print(self.width*self.height*self.depth)
    
    def vol(self):
        print('width =', self.width)
        print('height =',self.height)
        print('depth =',self.depth)
        return self.width*self.height*self.depth
b1=box()
print('volume of cube is = ', b1.vol())


# In[6]:


#passing an object as parameter to a method
class test:
    a=0
    b=0
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def equal(self,abc):
        if(abc.a==self.a and abc.b==self.b):
            return True
        else:
            return False
obj1=test(10,20)
obj2=test(10,20)
obj3=test(12,90)
print('obj1 == obj2 ', obj1.equal(obj2))
print('obj1 == obj3 ', obj1.equal(obj3))
#it compare the invoking object with one that is passed
#as parameter to the method
#invoking object obj1 and the object being passed to equal method
#is obj2
#if both value same return true


# In[19]:


class rect:
    lenght=0
    breath=0
    def __init__(self,l,w):
        self.length=l
        self.breadth=w
    def area(self,obj):
        print('lenght = ', obj.length)
        print('breadth = ', obj.breadth)
        return obj.length*obj.breadth
obj1=rect(10,20)
print('the area of rectangle = ', obj1.area(obj1))


# In[4]:


#__del__ (destructor method)
class demo:
    def __init__(self):
        print('welcome')
    def __del__(self):
        print('destructor executed successfully')
ob1=demo()
ob2=ob1
ob3=ob1
print('id of ob1 = ',id(ob1))
print('id of ob2 = ',id(ob2))
print('id of ob3 = ',id(ob3))
del ob2  #remove refrence
del ob1
del ob3
print('id of ob1 = ',id(ob1))
print('id of ob1 = ',id(ob2))
print('id of ob1 = ',id(ob3))


# In[3]:


#destructor is not invoked unless all the aliases are deleted
#destructor is called exactly once

class demo:
    def __init__(self):
        print('welcome')
    def __del__(self):
        print('destructor executed successfully')
ob1=demo()
ob2=ob1
ob3=ob1
print('id of ob1 = ',id(ob1))
print('id of ob2 = ',id(ob2))
print('id of ob3 = ',id(ob3))
del ob2  #remove refrence
del ob1
#del ob3


# In[22]:


#class membership tests

#when we create an instence of a class, the type of that
#instance is the class itself
#isinstance(obj,class name) is used to check for membership

class a:
    pass
class b:
    pass
class c:
    pass
ob1=a()     #instance of class a
ob2=b()     #instance of class b  
ob3=c()     #instance of class C
isinstance(ob1,a)
#isinstance(ob2,b)
#isinstance(ob3,c)


# In[9]:


#method overloading in python

class overload:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
o1=overload()
o1.add(100,20)
#o1.add(100,20,10)
#python understands the last definitation of the method a+b+c
#while calling add() method it is forced to pass three argument
#in simple words it forget the previous definiation of method add()


# In[28]:


class demo:
    result=0
    def add(self,instanceof=None,*args):
        if instanceof == 'int':
            self.result=0
        if instanceof=='str':
            self.result=''
        for i in args:
            self.result=self.result+i
        return self.result
d1=demo()
print(d1.add('int', 10.5,20,30))
print(d1.add('str','i','love','python'))


# In[26]:


class overload:
    def greeting(self,name=None):
        if name is not None:
            print('welcome ' + name)
        else:
            print('welcomeee')

obj=overload()
obj.greeting()
obj.greeting('modi')
#in python, method overloading is a technique to define a method
#in such way that there are more than one way to call it.


# In[28]:


#operator overloading

#sum of two operand x + y
#when python observed the + operator, it convert the expression
#x+y to call a special method __add__

# x + y   __add__(self,other)
# x - y     __sub__(self,other)
# x * y     __mul__(self,other)
# x / y     __truediv__(self,other)
# x // y        __floordiv__(self,other)
# x % y         __mod__(self,other)
# -x        __neg__(self,other)


#write a (self,other)program to overload + operator

class over:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        print('the value of ob1 ',self.x)
        print('the value of ob2 ',other.x)
        print('the addition of two object is: ',end='')
        return (self.x+other.x)
ob1=over(20)
ob2=over(30)
ob3=ob1+ob2 #ob1.__add__(ob2)
print(ob3)
#ob1 + ob2 it will call the int class __add__
#ob1.__add__(ob2)


# In[3]:


#operator overloading comparing two object

class demo:
    def __init__(self,x):
        self.x=x
        
    def __lt__(self,other):
        print('value of ob1 ',self.x)
        print('value of ob2 ',other.x)
        print('ob1 < ob2 : ',end='')
        return self.x < other.x

    def __gt__(self,other):
        print('ob1 > ob2 :', end=' ')
        return self.x > other.x

    def __le__(self,other):
        print('ob1 <= ob2 :', end='')
        return self.x <= other.x
ob1=demo(20)
ob2=demo(30)
print(ob1 < ob2)
print(ob1 > ob2) #  ob1.__gt__(ob2)
print(ob1 <= ob2)


#object equality

#ob1=50
#ob2=60
#ob3=ob1
#id(ob1)
#id(ob2)
#ob1 is ob2
#ob3 is ob1
#ob4=50
#ob1==ob4


# In[10]:


#inheritance

#single inheritance x->y
#multilevel inheritance  x-> y ->z
#multiple inheritance   x->y <-z


class a:  #parent class
    print('hello i m in base class')
class b(a):    #child class    #object class
    print('i m drived class')
ob2 = b()



class parent:
    def setcordinate(self,x,y):
        self.x=x
        self.y=y
        
class child(parent):
    def draw(self):
        print('locate point x1 = ',self.x,' on x axis')
        print('locate point y1 = ',self.y,' on y axis')

c=child()
c.setcordinate(10,20)
c.draw()


# In[13]:


#multilevel inheritance

#base class ->  middle base class  ->  derived class

#program of multilevel inheritance

class a:
    name=''
    age=0

class b(a):
    height=''

class c(b):
    weight=''

    def read(self):
        print('enter the following values')
        self.name=input('enter name:')
        self.age=input('enter age')
        self.height=input('enter height')
        self.weight=input('enter weight')

    def display(self):
        print('enter values are as follows')
        print('name', self.name)
        print('age', self.age)
        print('height', self.height)
        print('weight', self.weight)

c1=c()
c1.read()
c1.display()


# In[15]:


#multiple inheritance

#a-> c <-b  a nd b are base class

class a:
    a1=0

class b:
    b1=0

class c(a,b):
    c1=0

    def read(self):
        print('enter the following values')
        self.a1=input('enter value of a1')
        self.b1=input('enter value of b1')
        self.c1=input('enter value of c1')
        

    def display(self):
        print('enter values are as follows')
        print('a', self.a1)
        print('b', self.b1)
        print('c', self.c1)
        


ob1=c()         #instance of child class
ob1.read()
ob1.display()


# In[8]:


#super()

class demo:
    a=0
    b=0
    c=0

    def __init__(self,a1,b1,c1):
        self.a=a1
        self.b=b1
        self.c=c1
    def dis(self):
        print(self.a,self.b,self.c)

class newdemo(demo):
    d=0
    def __init__(self,a1,b1,c1,d1):
        self.d=d1
        super().__init__(a1,b1,c1)

    def dis(self):
        print(self.a,self.b,self.c,self.d)

b1=demo(100,200,300)
print('content of base class')
b1.dis()
d1=newdemo(10,20,30,40)
print('content of derived class')
d1.dis()


# In[11]:


#method overriding

class a:
    i=0
    def dis(self):
        print('i m in super class')

class b(a):
    i=0
    def dis(self):
        print('i m in sub class')

d1=b()
d1.dis()

#only output i m in sub class


# In[13]:


#so we use super to access the overridden method
#super().methodname

class a:            #base class
    i=0
    def dis(self):
        print('i m in super class')

class b(a):         #super class
    i=0
    def dis(self):
        print('i m in sub class')
        super().dis()       #call display of base class
        
d1=b()
d1.dis()


# In[1]:


class abc:
    def m1(self,a,b):
        return a+b
ob1 = abc()
ob2 = abc()
print(ob1.m1(10,20))
print(ob2.m1(20,30))


# In[1]:


class demo:
    def __init__(abc):
        print("hello")
class newdemo:
    def __init__(self):
        print("hi")
class olddemo(newdemo,demo):
    def __init__(self):
        print("bye")
        super().__init__()
        super().__init__()
d3 = olddemo()


# In[3]:




