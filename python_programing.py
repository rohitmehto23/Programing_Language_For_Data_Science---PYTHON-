#!/usr/bin/env python
# coding: utf-8

# In[3]:


L=[1,2,3,4,5]
print(L)


# In[42]:


L1=['a','b',2,3,4,'c']
print(L1)


# In[3]:


print(len(L))


# In[4]:


print(type(L))


# In[5]:


print(type(L1))


# In[7]:


print(L[3])


# In[8]:


print(L[-1])


# In[9]:


print(L[1:4])


# In[11]:


print(L[0:2])


# In[12]:


print(L[2:4])


# In[13]:


print(L[0:4])


# In[15]:


print(L[2:5])


# In[19]:


print(L[-3:])


# In[4]:


L.append(6)#append is to add an item to the list at last


# In[5]:


print(L)


# In[7]:


L1.append(9)


# In[8]:


print(L1)


# In[9]:


#insert 


# In[10]:


L.insert(1,'A')


# In[11]:


print(L)


# In[4]:


course=['python','stats','mysql']


# In[5]:


print(course)


# In[6]:


company=['TCS','HCL','ORACLE']


# In[7]:


print(company)


# In[8]:


course.extend(company)#extend:to join two list


# In[9]:


print(course)


# In[10]:


course.remove('mysql')


# In[11]:


print(course)


# In[12]:


company.pop()
print(company)


# In[22]:


L8=[1,1,1,2,3,4,5]


# In[23]:


print(L8)


# In[24]:


L8.remove(1)


# In[25]:


print(L8)


# In[26]:


L9=[11,1,5,2,3,5,6,7,5,12]


# In[28]:


print(L9)


# In[32]:


L9.remove(5,)#if there are more than 1 item with specific value remove method removes 1st appearence


# In[30]:


print(L9)


# In[1]:


L1=[1,2,3]
L2=L1.copy()#method 1
print(L2)


# In[2]:


L3=[4,5,6]
L4=list(L3)#method 2
print(L4)


# In[3]:


L5=L1+L2+L3
print(L5)


# In[4]:


L1.extend(L2)
print(L1)


# In[13]:


# tuple
T1=(1,2,3,4)
print(T1)


# In[8]:


print(T1[1])


# In[9]:


print(T1[-3])


# In[12]:


subjects=("nlp","dl","ml","ai","python","sql")


# In[13]:


print(subjects)


# In[14]:


print(subjects[2:5])


# In[16]:


print(subjects[:3])


# In[18]:


print(subjects[3:])


# In[20]:


Y=list(T1)


# In[22]:


print(Y)


# In[23]:


Y[1]=5


# In[24]:


print(Y)


# In[27]:


T1=tuple(Y)


# In[28]:


print(Y)


# In[29]:


s=list(T1)


# In[30]:


print(s)


# In[31]:


s.append(8)


# In[32]:


print(s)


# In[33]:


T1=tuple(s)


# In[34]:


print(T1)


# In[1]:


t5=(2,)


# In[2]:


print(t5)


# In[4]:


T2=('a','b',1,3,6,7)


# In[5]:


print(T2)


# In[6]:


R=list(T2)


# In[7]:


print(R)


# In[8]:


R.remove('a')


# In[9]:


print(R)


# In[10]:


T2=tuple(R)


# In[11]:


print(T2)


# In[14]:


T2=T2+T1


# In[15]:


print(T2)


# In[16]:


T3=(8,9,1)


# In[17]:


T4=T2+T3


# In[23]:


print(T4)


# In[19]:


# multiply tuples
malls=('DLF','GIP','LOGIXS')


# In[20]:


shop=malls*2


# In[21]:


print(shop)


# In[27]:


T5=(23,4,5,5,6,63,2,23)


# In[29]:


print(max(T5))


# In[30]:


print(min(T5))


# In[31]:


print(sum(T5))


# In[35]:


S={1,2,3,4}
print(2 in S)


# In[36]:


#add item in set
S.add(5)


# In[37]:


print(S)


# In[38]:


#add one set to another set
S1={'a','b'}
S2={3,6,7}


# In[39]:


S2.update(S1)


# In[40]:


print(S2)


# In[46]:


# add list to set
S3={1,7}
L1=[9,8]
S3.update(L1)


# In[48]:


print(S3)


# In[50]:


#n remove items from set
S3.remove(9)


# In[51]:


print(S3)


# In[52]:


S3.discard(1)


# In[53]:


print(S3)


# In[1]:


S4={'a','b','c'}
S5={1,2,3,4}
S6=S4.union(S5)


# In[2]:


print(S6)


# In[3]:


# strings
X='hello'
print(X)


# In[5]:


Y="Hello"
print(Y)


# In[8]:


P=""" rohit
     mehto
     is a super boy """
print(P)


# In[3]:


X='Hello, world!'
print(X[2:5])


# In[4]:


print(X[:5])


# In[9]:


print(X[-5:-2])


# In[10]:


# modify string
print(X.upper())


# In[11]:


print(X.lower())


# In[12]:


print(X.replace("H","Y"))


# In[13]:


print(X.split(","))


# In[16]:


P="AAFT"
Q=" SODS"
R=P+Q
#R=P+" "+Q
print(R)


# In[18]:


# string format-we csn combile strings and number by using format method
age=22
txt="My name is john, and I am {} years old"
print(txt.format(age))


# In[20]:


print(X.capitalize())


# In[21]:


print(X.title())


# In[4]:


# dictionary
car_dict={'brand':'ford','model':'mustang','year':1998}


# In[2]:


print(car_dict)


# In[14]:


# print the brand value of the dictionary?
print(car_dict['brand'])


# In[15]:


car_dict={'brand':'ford','model':'mustang','year':1998,'year':2022}


# In[16]:


print(car_dict)


# In[19]:


print(len(car_dict))


# In[21]:


print(type(car_dict))


# In[22]:


#axis dictionary items
print(car_dict['model'])


# In[23]:


# other method
X=car_dict['model']
print(X)


# In[24]:


# another method(get method)
X=car_dict.get('model')
print(X)


# In[25]:


# keys method
print(car_dict.keys())


# In[26]:


# and
X=car_dict.keys()
print(X)


# In[29]:


# to add new item to the dictionary 
car_dict['color']='zed_black'
print(car_dict)


# In[31]:


veg_dict={'veg1':'potato','veg2':'tomato','veg3':'capsicum'}
print(veg_dict)


# In[32]:


X=veg_dict.keys()
print(X) # before change


# In[33]:


veg_dict['veg4']='cabage'
print(X) # after change


# In[15]:


print(car_dict.values())


# In[14]:


print(car_dict.items())


# In[7]:


# change values 
car_dict['year']=2023


# In[8]:


print(car_dict)


# In[12]:


# other method
car_dict.update({'year':2020})


# In[13]:


print(car_dict)


# In[16]:


# to delete item # pop method removes items with key name
print(car_dict.pop('year'))


# In[19]:


print(car_dict.popitem)


# In[1]:


del car_dict['model']


# In[25]:


print(car_dict)


# In[39]:


dicw={'name':'rohit','class':12}


# In[40]:


print(dicw)


# In[38]:


#to delete the dictionary
del dicw


# In[44]:


#method 1
dict1=dict(dicw)


# In[45]:


print(dict1)


# In[46]:


#method 2
dict1=dicw.copy()


# In[47]:


print(dict1)


# In[52]:


# nested dictionary -a dictionary can contain more dictonaries is called nested disctionary 
# Q-
myfamily={'member':{'name':'a','age':20},'member2':{'name':'b','age':45},'member3':{'name':'c','age':28}}


# In[53]:


print(myfamily)


# In[ ]:


# addition of two numbers
a=input("enter first number ")
b=input("enter second number ")
sum=int(a)+int(b)
print("sum of two numbers : ", sum)


# In[1]:


#substraction of two numbers
a=input("enter first number ")
b=input("enter second number ")
subs=int(a)-int(b)
print("substraction of two number is : ",subs)


# In[ ]:


# division of two numbers
a=input("enter first number ")
b=input("enter second number ")
div=int(a)/int(b)
print("division of two number is : ",div)


# In[1]:


#write a program to find two values which one is greater
a=input("enter first number ")
b=input("enter second number ")
if a>b:
    print("a is greater")
else:
    print("b is greater")


# In[ ]:


a=input("enter first number ")
b=input("enter second number ")
if a>b:
    print("a is greater")
elif a==b:
    print("a is equal to b")
elif a!=b:
    print("a is not equal to b")
else:
    print("b is greater")


# In[3]:


#write a prog to check whthr the given number is even or odd
a=7
if(a%2)==0:
    print("number is even ")
else:
    print("number is odd ")


# In[3]:


for i in "datascience":
    print(i)


# In[1]:


cars=['ford','audi','maruti']
for i in cars:
    if (i=='audi'):
        break
    print(i)


# In[2]:


cars=['ford','audi','maruti']
for i in cars:
    print(i)
    if (i=='audi'):
        break
 


# In[5]:


cars=['ford','audi','maruti']
for i in cars:
    if (i=='audi'):
        continue
    print(i)
        
 


# In[6]:


# range() function : to loop through a set of code a specified number of tyms we can use the range() function 
#the range() function returns a sequence of numbeer starting from 0 by default and increments by 1  and ends at a specified number


# In[7]:


for i in range(6):
    print(i)


# In[8]:


for  i in range(2,6):
    print(i)


# In[9]:


# the range() function defaults to increments the sequence by 1 however it is possible to specify the increment value by adding a third parameter range(2,30,3)


# In[10]:


for i in range(2,30,3):
    print(i)


# In[11]:


# else keyword: else keyword in a for loop specifies a block of code to be ecxexuted  when the loop is finished


# In[12]:


for x in range(6):
    print(x)
else:
    print("finally finished")


# In[14]:


for x in range(6):
    if x==3:
        break
    print(x)
else:
        print("finally finished")


# In[1]:


#funtion : it is a block of code which only runs when it is called ,we can pass data known as para meters, function can return data as a result ,it is also known as module

           #creating function

def my_funct():
    print('hello aaft')
    
            # calling function

my_funct()                
    


# In[2]:


# parameter: def fuct_name(parameter):
#statement
return expression
function return


# In[3]:


#types of fucntion : built in functions-standared functions already available in python 
# user define function- we can create our own function based in requirement


# In[4]:


# arguments- arguments are specified after function name inside the  parantesis
#parameter-it is the variable listed inside the paranthesis in the fucntiion defination and argyument is the value set 


# In[6]:


def add(n1:int,n2:int):
    n3=n1+n2
    return n3
n1,n2=5,38
result=add(n1,n2)
print('add is ',result)


# In[18]:


def even_odd(n):
    n=5
    if n%2==0:
        print("number is even ")
    else:
        print("number is odd ")

even_odd("n")


# In[7]:


# wap to find that thw number is prime or not?
# wap to fine that given number is armstrong number or not?
# wap to find given number is palindrome or not?
# wap to find fibonaci series ?
# wap to find factorial of any number number ?
# wap to swap numbers?


# In[5]:


#ans 2
i=int(input('enter number '))
n=i
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if n==sum:
    print('number is amstrong')
else:
    print('number is not amstrong')


# In[1]:


#ans 1
a=int(input('enter number'))
i=1
count=0
while (i<=a):
    if (a%i==0):
        count=count+1
    i=i+1
if (count==2):
    print('number is found')
else:
    print('number is not found')


# In[ ]:


numbers=input()
reverse_numbers=numbers[::-1]
print('reverse of numbers is',reverse_numbers)


# In[2]:


#without inbuilt function
i=int(input('enter the number'))
rev=0
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
print('reverse of numbers is',rev)


# In[4]:


# ans 3
i=int(input('enter the number : '))
n=i
rev=0
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
if n==rev:
    print('number is palindrome ')
else:
    print('number is not palindrome')


# In[13]:


n=int(input("enter the number series "))
a,b=0,1
if n>=0:
    print('enter a positive integer')
elif n==1:
    print('fobonacci series upto',n,'terms=')
    print(a)
else:
    print('fobonacci series upto',n,'terms=')
    print(a,b,end="")
    for _ in range(2,n):
        next_term=a+b
        print(next_term,end="")
        a,b=b,next_term
    


# In[7]:


# wap to print fibonacci series
n=int(input('enter last number'))
x=0
y=1
z=0
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y


# In[3]:


# wap to find weather the year is leap year?
n=int(input('enter the year : '))
if (n % 4 == 0 )and (n % 100 != 0):
    print('it is a leap year')
elif(n % 400 == 0) and(n % 100 == 0):
    print('it is a leap year')
else:
    print('it is not a leap year')

 


# In[2]:


n=int(input('enter a number : '))
factorial = 1
if n <0:
    ('factorial is not define for negetive integers ')
elif (n==0):
    print('the factorial for 0 is 1')
else:
    for i in range (1,n+1):
        factorial*=i
        print(f'the factorial {n} is {factorial}')


# In[ ]:


# python libararies - collection of modules that are link together are known as python libararies
# types of libr - for data analysi - pandas , matplotlib , numerical computation-numpy , seaborn , scipy -scientific computing, information or high level , scikit - open source machine learnig libr , tensorflow - for numerical calculation based on ml and dl, keras - open source neural network lib , nltk(natural language tool kit ) - for nlp , scrapy - for text analysis , pygame - , pybrain , statsmodels ,


# In[5]:


# Pandas
get_ipython().system('pip install pandas')


# In[3]:


import pandas as pd


# In[4]:


resultsheet ={'jack':pd.Series([91,92,93],index=['math','science','english']),
        'john':pd.Series([82,83,84],index=['math','science','english']),
        'jill':pd.Series([92,74,58],index=['math','science','english'])}
rdf=pd.DataFrame(resultsheet)
print(rdf)


# In[12]:


# operation on daraframes
#adding new column to a data frame
rdf['smith']=[89,53,76]
print(rdf)


# In[14]:


#adding new row to a data frame
rdf.loc['hindi']=[60,50,43,85]
print(rdf)


# In[30]:


#delete row or column from a data frame
#whenever we are deleting row or colums from a data frame the name of lables to be draw and thw axis from which need to be draw
# to delete a row axis value should be 0 and for column axis value should be 1
rdf=rdf.drop('math',axis=0)
print(rdf)


# In[31]:


rdf=rdf.drop('smith',axis=1)
print(rdf)


# In[37]:


#remane row lable of the dataframe
#row
rdf=rdf.rename({'english':'sub1','science':'sub2'},axis='index')
print(rdf)


# In[39]:


#column
rdf=rdf.rename({'jill':'saanp','jack':'Ld'},axis='columns')
print(rdf)


# In[5]:


# access dataframe elements
rdf.loc['science']


# In[6]:


print(rdf['jack'])


# In[8]:


rdf.loc[['english','math']]


# In[9]:


rdf.loc['math']>90


# In[10]:


#to check in which subject a particular student has scored more than 90
rdf.loc[:,'jill']>90


# In[14]:


# accessing data frame elements throug slicing
rdf.loc['math':'science']


# In[15]:


rdf.loc['math':'science','jack':'jill']


# In[18]:


# joining ,merging and concatination of data frame

dframe=pd.DataFrame([[1,2,3],[4,5],[6]],
                   columns=['c1','c2','c3'],
                   index=['r1','r2','r3'])

dframe2=pd.DataFrame([[10,20],[30],[40,50]],
                    columns=['c2','c5'],
                    index=['r4','r2','r5'])


# In[19]:


print(dframe)
print(dframe2)


# In[21]:


dframe=dframe.append(dframe2)
print(dframe)


# In[ ]:




