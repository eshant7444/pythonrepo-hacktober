
# coding: utf-8

# Unit 1 part 2

# In[2]:


#write a program that prompts a user to enter two different numbers. 
#perform basic arithemetic operations based on the choices.
num1 = int(input())
num2 = int(input())
print('1. addition')
print('2. subtraction')
print('3. multiplication')
print('4. division')
choice = int(input("please enter choice: "))
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    print(num1/num2)
else:
    print("invalid number")


# In[2]:


# while loop


# In[26]:


#write a program to print number from 1 to 5 using while loop
count = 1
while count<=5:
    print(count) 
    count += 1 
#print(count)


# In[4]:


#write a program to add 10 consecutive numbers starting from 1 using while loop.


# In[25]:


count = 0
sum = 0
while count <=10:
    sum = sum + count 
    count = count + 1 
    #print(sum)
print(sum)


# In[6]:


#write a program to find sum of the digits of a given number


# In[7]:


num = int(input('enter the number')) 
#x = num
sum = 0
r = 0
while num>0: 
    r = num%10 
    num = num//10  
    sum = sum + r 
print(sum)


# In[9]:


#write a program to display reverse of the number using while loop
num = int(input()) 
r = 0
while num>0: 
    p = num % 10 
    num = num//10 
    r = r*10 +p 
print(r)


# In[12]:


#write a program to print the sum of the numbers from 1 to 20 
#inlcuding 1 and 20
#that are divisible by 5 using the while loop.


# In[5]:


count = 1
sum = 0
while count <=20: 
    if count % 5 ==0: 
        sum = sum + count 
    count = count + 1 
print(sum)


# In[14]:


#write program to print factorial of a number


# In[4]:


num = int(input()) 
fact = 1 
a = 1
while fact <= num: 
    a = a * fact 
    fact = fact + 1 
print(a)


# In[16]:


#write program to check whether the number is an Armstrong number or not.


# In[6]:


num = int(input()) 
sum = 0 
x = num
while num>0: 
    d = num % 10 
    num = num // 10 
    sum = sum + (d*d*d*d) 
if (x == sum):
    print('number is armstrong')
else:
    print('number is not armstrong')


# In[10]:


'''
Range Function
range(begin, end, step) 
it goes from n to n-1
'''


# In[14]:


list (range(1,5))


# In[4]:


# create a list from 1 to 20 with a difference of 2.
list (range(1, 20, 2))


# In[1]:


list(range(5,0,-1))


# In[4]:


list(range(1,10))


# In[9]:


# For Loop
# for var in sequence:
#  Statement


# In[16]:


#a = 1
#b = 10
for i in range(1,10,1): 
    print(i)
print('end of program')


# In[2]:


a = int(input())
b = int(input())
c = int(input())
list(range(a,b,c))


# In[15]:


#display capitol letters from A to Z (65 to 91)
for i in range (65,91,1):
    print(chr(i), end=' ')


# In[2]:


#use for loop to print numbers from 1 to 10 in reverse order
for i in range(10,0,-1):
    print(i,end=' ')


# In[21]:


#write a program to print square of first five numbers
for i in range(1,6):
    sq = i*i
    print(sq)


# In[26]:


#write program to print even numbers from 0 to 10 
#and find their sum.
sum = 0
for i in range(0,11,1):
    if i%2==0:
        print (i)
        sum = sum + i
print(sum)


# In[1]:


#write a program that prompts a user to enter four numbers 
#and find the greatest number among the four numbers entered.


# In[8]:


p = 0
for i in range(4):
    n = int(input())
    if n > p:
        p = n
print(p)


# In[18]:


num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
sum = num1+num2+num3+num4
for i in range(sum):
    if i==num1 or i==num2 or i==num3 or i==num4:
        l = i
print('greatest number is: ', l)


# In[1]:


#Write a program to print Fabonacci series up to 8.

first = int(input()) #0
second = int(input()) #1
limit = int(input())
print(first,second, end =' ')
for i in range(limit): #,,,,7
    sum = first + second # 1,2,3,5
    first = second # 1,1,2,3
    second = sum   # 1,2,3,5
    print(sum,end=' ')


# In[12]:


# pattern questions

num = 1
#x = num
for i in range (1,6,1):
    num = num + 1
    for j in range(1,num,1):
        print(" * ",end=' ')
        #x = num + 1
    print()


# In[16]:


num = 7
x = num
for i in range (1,6,1):
    num = num - 1
    for j in range (1,num,1):
        print(" * ",end = ' ')
        x = num - 1
    print()


# In[1]:


#num = 1
#x = num
for i in range(1,6,1):
    #num = num + 1
    for j in range (1,i+1,1): #(1,3,1)
        print (j,end=' ')
        #x = num + 1
    print()


# In[5]:


num = 1
x = num
for i in range (1,5,1):
    num = num + 1
    for j in range (1,num,1):
        print(j, end = " ")
        x = num + 1
    print()
    
num = 5 
x = num
for i in range(1,5,1):
    num = num - 1
    for j in range(1,num,1):
        print(j,end=" ")
        x = num - 1
    print()


# In[6]:


# break statement. WAP to print numbers from 1 to 10 in a range of 1 to 100
for i in range (1,100,1):
    if (i==11):
        break
    else:
        print(i,end=" ")


# In[1]:


#continue. 
for i in range (1,11,1):
    if i == 5:
        continue
    print (i,end = " ")


# In[5]:


# while (conditions):
    statements
    counter


# In[17]:


for i in range(5,0,-1): 
    for j in range(i,0,-1): 
        print(j, end = " ")
    print()


# In[8]:


for i in range(65,70,1): #65,66,67,68,69
    for j in range(65,i+1,1): #(65,66,1),(65,67,1)..65,66
        print(chr(j), end = ' ')
    print()


# In[11]:


for i in range(1,5,1):
    for j in range (1,i+1,1):
        print(j,end=" ")
    print()
for x in range (5,1,-1):
    for y in range (1,x-1,1):
        print(y,end=" ")
    print()

