
# coding: utf-8

# In[3]:


D={}
D['name']='sachin'
D['age']=40
D


# In[6]:


D=dict(name='virat',age=35)
D


# In[8]:


dict([('name','rahul'),('age',40)])


# In[1]:


#adding and rePlacing values use subscriPt oPerator
D2 = {}
D2['john']='1234' # adding
D2


# In[2]:


D2['john']='5678' #rePlacing
D2


# In[23]:


D2['john']


# In[28]:


D3={}
D3['laptop']='mac'
D3['count']=10
D3


# In[31]:


A='i want %(count)d %(laptop)s laptops'%D3
A

# d and s for integer and string


# In[4]:


#comparing two dictionary
A={'I':'India','A':'America'}
B={'I':'Italy','A':'America'}

#A==B
#A!=B
C=A
C
C==A


# In[1]:


#METHOD OF DICT CLASS
#KEYS()

asicode={'A':65,'B':66,'C':67,'D':68}
#asicode.keys()  #return a sequence of keys
#asicode.values()   #return a sequence of values
#asicode.items()     #return a sequence of tuples
#asicode.clear()     #delete all entries
#asicode
#asicode.get('B')     #return the values of key
print(asicode.pop('C'))   # remove the key & return the value
asicode


# In[19]:


#traversing dictionaries

grades={'ram':'A','sham':'B','tom':'C', 'dom':'D'}
for key in grades:
    print(key,':',(grades[key]))




# In[13]:


grades={'ram':'A','sham':'B','tom':'C', 'dom':'D'}
for key in grades.keys():
    print(key,':',grades.get(key))


# In[16]:


#nested dictionaries

#{}
#['john']
players={'VIRAT':{'ODI':7212,'TEST':3245},
         'SACHIN':{'ODI':18426,'TEST':15921}}

players['VIRAT']['ODI']
#players['VIRAT']['TEST']

#players['SACHIN']['ODI']
#players['SACHIN']['TEST']


# In[19]:


#traversing nested dictionaries
players={'VIRAT':{'ODI':7212,'TEST':3245},
         'SACHIN':{'ODI':18426,'TEST':15921}}
for name,detail in players.items():
    print('',name)
    print('',detail)



# In[2]:





# In[25]:


players={'VIRAT':{'ODI':7212,'TEST':3245},
         'SACHIN':{'ODI':18426,'TEST':15921}}
for name,detail in players.items():
    print('player :', name)
    print('run score in odi :',detail['ODI'])
    print('run score in test :', detail['TEST'])


# In[27]:


players={'VIRAT':{'ODI':7212,'TEST':3245},
         'SACHIN':{'ODI':18426,'TEST':15921}}
for name, detail in players.items():
    print('',name)
    for key in detail:
        print(key,':',str(detail[key]))


# In[12]:


#write a function histogram that take string as
#parameter and generate a frequency of character in it
s='apple'

def histogram(s):
    D=dict()
    for c in s:
        if c not in D:
            D[c]=1
        else:
            D[c]=D[c]+1
    return D
H=histogram('apple')
print(H)


# In[2]:


x = input()
d = {}
def abc(s):
    for alpha in s:
        d[alpha]=x.count(alpha)
    print(d)
abc(x)

