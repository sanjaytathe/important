
# string occurence
#x="sanjaytathe"
#d={}
#for i in x:
#    v=x.count(i)
#    d[i]=v
#print(d)


#x="sanjaytathe"
#y=[]
#for i in x:
#   if i not in y:
#       y.append(i)
#       print(i,"=",x.count(i))
#--------------------------------
'''
x="aaabbcccc"
k=""
count=0
s=x[0]
for i in x:
    if i==s:
        count=count+1
    else:
        k=k+(str(count)+s)
        s=i
        count=1
k=k+(str(count)+s)
print(k)
        

x="3a2b4c"
k=""
for i in x:
    if i.isdigit():
        num=int(i)
    else:
        var=i
        k=k+(num*var)
print(k)
'''
#------------------------------------------
# fabonacci series
'''
n1=0
n2=1
n3=0
while n3<130:
    print(n3)
    n1=n2
    n2=n3
    n3=n1+n2


def fabo(n):
  n1=0
  n2=1
  n3=0
  while n3<n:
    yield n3
    n1=n2
    n2=n3
    n3=n1+n2
v=fabo(100)
print(next(v))
print(next(v))
print(next(v))
print(next(v))
'''
'''
def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

n=10
if n<=0:
    print("invalid")
else:
    for i in range(n):
        print(fibonacci(i))
'''
#-----------------------------------------------------
'''
x='I_Am_Coder'
y=[]
z=x.split('_')
for i in z:
    y.append(i[0].lower()+i[1:].upper())
    v=".".join(y)
print(v)
'''
#-------------------------------------------
# sort string
'''
x=[2,5,6,3,9,4,7,8]
y=[]
for i in range(len(x)):
    v=min(x)
    y.append(v)
    x.remove(v)
print(y)
'''
#----------------------------------------------------
# largest no
'''
x=[12,45,63,25,11]
from functools import *
z=reduce(lambda x,y:x if x>y else y,x)
print(z)


x=[12,45,63,25,11]
large=0
for i in x:
    if i>large:
        large=i
print(large)

sec_large=0
for i in x:
    if i>sec_large and i!=large:
        sec_large=i
print(sec_large)
'''
#------------------------------------------------------
# reverse string
'''
x=[1,2,3,4,5,6]
k=[]
for i in x:
    k.insert(0,i)
print(k)


k=[]
for i in range(len(x)-1,-1,-1):
    k.append(x[i])
print(k)


x=[1,2,3,4,5,6]
x.reverse()
print(x)

x=[1,2,3,4,5,6]
y=[]
size=len(x)-1
while size>=0:
    y.append(x[size])
    size=size-1
print(y)


x=[1,2,3,4,5,6]
print(x[::-1])


x=[1,2,3,4,5,6]
i=0
j=len(x)-1
while i<j:
    temp=x[i]
    x[i]=x[j]
    x[j]=temp
    i +=1
    j -=1
print(x)
'''
#--------------------------------------------

# amstrong no
'''
x=int(input("enter the number :- "))
ori=x
sum=0
while x>0:
    sum=sum+(x%10)*(x%10)*(x%10)
    x=x//10
if sum==ori:
    print("amstrong")
else:
    print("not amstrong")
'''


''' 
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   sum = 0  
   temp = num  
   while temp > 0:  
       digit = temp % 10  
       sum += digit ** 3  
       temp //= 10  
       if num == sum:  
            print(num)    
'''
#------------------------------------------------
#x=int(input("enter the no :- "))
'''
ori=x
reverse=0
while x>0:
    reverse=reverse*10+(x%10)
    x=x//10
#print(reverse)

if ori==reverse:
    print("palindrome")
else:
    print("not palindrome")
'''
'''
x='nitin'
if x[::-1]==x:
    print('string palindrome')
else:
    print("not palindrome")
    '''
#----------------------------------------------------
'''
x='sanjay ganesh tathe'
y=[]
z=x.split()
for i in z:
    y.append(i[::-1])
y=" ".join(y)
print(y)


x='sanjay ganesh tathe nagpur'
y=[]
z=x.split()
for i,j in enumerate(z):
    if i%2==0:
      y.append(j)
y=" ".join(y)
print(y)
'''
#---------------------------------------------------------
# prime or not
'''
x=int(input("enter the no :- "))
if x<2:
      print("not prime")
else:
    for i in range(2,x):
        if x%i==0:
            print("not prime")
            break
    else:
        print("prime")

x=1
y=100
for i in range(x,y):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)

'''
#------------------------------------------------------

# sorting list
'''
x=[4,6,8,2,1,58,95,23]
n=len(x)
for i in range(n):
    for j in range(i+1,n):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]
print(x)


x=[5,8,9,3,7,4]
for i in range(len(x)):
    for j in range(len(x)-i-1):
        if x[j]>x[j+1]:
            t=x[j]
            x[j]=x[j+1]
            x[j+1]=t
print(x)

x={1:'sanjay',5:'ganesh',3:'tathe'}
for i,j in sorted(x.items()):
    print(i,j)
'''
#-----------------------------------------------------------
'''
def largest(a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    else:
        return c
print(largest(20,45,43))
'''
#-------------------------------------------------------------
'''
x=[10,2,14,32,10,3]
y=35
leng=len(x)
for i in range(leng):
    for j in range(i+1,leng):
        if x[i]+x[j]==y:
            print(x[i],x[j])
'''
#---------------------------------------------------------------
'''
x="A palindrome is a word, phrase, number, or another sequence of units that can be read the same way in either direction, with general allowances for adjustments to punctuation and word dividers. When its digits are reversed, they turn out to be the same number as the original number. Palindromes can be numeric as well. For example, madam, 1234321. This blog will teach us how to create a Palindrome in Python."

n=int(input("enter repeated word :- "))
y=x.split()
for i in y:
    if x.count(i)>=n:
        print(i)

'''
#----------------------------------------------------------------------
# perfect no
'''
x=28
sum=0
for i in range(1,x):
   if x%i==0:
       sum=sum+i
if sum==x:
    print('perfect no')
else:
    print('not perfect no')

'''
#---------------------------------------------------------------------------
# find all possible substring
# eg bye->b,y,e,by,ye,bye
'''
x=input("enter the sring :- ")
y=[]
for i in range(0,len(x)):
    for j in range(i+1,len(x)+1):
        y.append(x[i:j])
print(y)
 '''                

#-----------------------------------------------------

'''
x="sanjay&tathe$"
k=""
g=""
l=[]
for i in x:
    if i.isalpha():
        k=i+k
    else:
        g=g+i
        l.append(x.index(i))
k=list(k)
for i in range(len(g)):
    k.insert(l[i],g[i])
print("".join(k))
    
'''

#------------------------------------------------------------------------
#*
#* *
#* * *
#* * * *
#* * * * *
'''
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
'''
#---------------------------------------------------------------------

'''
* * * * *
* * * *
* * *
* *
*

n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()
'''

#------------------------------------------------------------------------------

'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*


n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()


for i in range(n):
    for j in range(i,n-1):
        print("*",end=" ")
    print()
'''

#------------------------------------------------------------------------
'''

          *
        * *
      * * *
    * * * *
  * * * * *


n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
 '''
#-------------------------------------------------------------------------
'''
  * * * * *
    * * * *
      * * *
        * *
          *
n=5
for i in range(n):
    for j in range(i+1):
       print(' ',end=" ")
    for j in range(i,n):
       print('*',end=" ")
    print()

'''
#-------------------------------------------------------------------------
'''
          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

'''
#-------------------------------------------------------------------------

# n=5
# x=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(x,end=" ")
#         x=x+1
#     print()

# 1 
# 2 3 
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

#-------------------------------------------------------------------------

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
        
#     print()

# 1 
# 2 2 
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
#-------------------------------------------------------------------------


# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
        
#     print()


# 1 
# 1 2 
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

#-------------------------------------------------------------------------


# n=5
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
        
#     print()


# 1 
# 2 1 
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

#-------------------------------------------------------------------------


# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(f"{i}{j}",end=" ")
#     print()


# 11 
# 21 22 
# 31 32 33
# 41 42 43 44
# 51 52 53 54 55

#-------------------------------------------------------------------------

# n=5
# ch=65
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(ch),end=" ")
#         ch=ch+1
#     print()


# A 
# B C 
# D E F
# G H I J
# K L M N O    
        
#-------------------------------------------------------------------------

#array rotation
'''
x=[1,2,3,4,5]
for i in range(2):
    v=x.pop(0)
    x.append(v)
print(x)

'''

#-------------------------------------------------------------------------

# remove multiple element
'''
x=[1,2,3,4,5,6]
del x[:2]
print(x)
'''

#-------------------------------------------------------------------------
# lenght of list
'''
x=[1,2,3,4,5,6,7]
len=0
for i in x:
    len=len+1
print(len)
'''

#-------------------------------------------------------------------------
'''
x = "Learning Python is very Easy"
s=[]
# output: Easy Very is Python Learning
y=x.split(" ")
for i in y:
    s.insert(0,i)
d=" ".join(s)
print(d)

'''
#-------------------------------------------------------------------------

# Example 1: Count Number of Digits in an Integer using while loop

#x=12345
# count=0
# while x!=0:
#     x=x//10
#     count=count+1
# print(count)

#-------------------------------------------------------------------------

#  Python program to find the sum of all items in a dictionary
'''
x={'x':100,'y':200,'z':500}
sum=0
for i in x.values():
    sum=sum+i
print(sum)

'''
#-------------------------------------------------------------------------
'''
x="sanjay,ganesh.tathe"
x=x.replace(',','temp')
x=x.replace('.',',')
x=x.replace('temp','.')
print(x)
'''
#-------------------------------------------------------------------------
# uncommon from two string
'''
def function(a,b):
    list_a=a.split()
    list_b=b.split()
    uc=' '
    for i in list_a:
        if i not in list_b:
            uc=uc+" "+i
    for j in list_b:
        if j not in list_a:
            uc=uc+" "+j
    return uc

a="apple banna ,mango"
b="banna,fruti,mango,"
print(function(a,b))





# x='nagpur'
# y='pune'
# a=set(x).difference(set(y))
# b=set(y).difference(set(x))
# a.update(b)
# print(str(a))
'''

#-------------------------------------------------------------------------
'''
x=[5,8,9,3,7,4]
for i in range(len(x)):
    for j in range(len(x)-i-1):
        if x[j]>x[j+1]:
            t=x[j]
            x[j]=x[j+1]
            x[j+1]=t
print(x)
'''
#-------------------------------------------------------------------------
'''
# linear search
# x=[5,8,9,3,7,4]
# key=int(input("enter the element :- "))
# for i in range(len(x)):
#     if key==x[i]:
#         print("element found :- ")
#         break
# else:
#         print("not found")
'''
#-------------------------------------------------------------------------
# leap year or not 


# year=int(input("Enter year to be checked:"))
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("The year is a leap year!")
# else:
#     print("The year isn't a leap year!")

#-------------------------------------------------------------------------
# y=['1011','1001','1111','1010']

# value = []

# for p in y:
#     intp = int(p, 2)
#     print(intp)
#     if  intp%5 ==0:
#         value.append(p)

# print (','.join(value))

#-------------------------------------------------------------------------
'''
def fabo(a):
    n=0
    while n<a:
        yield n
        n+=1
v=fabo(100)
print(next(v))
print(next(v))
'''
#-------------------------------------------------------------------------

'''
def ches(x,y):
  l=len(y)
  c=0
  for i in range(len(x)):
    if x[i:l+i]==y:
        c=c+1
  return c

x='ABCDCDCDC'
y='CDC'

print(ches(x,y))
'''

#-------------------------------------------------------------------------
'''
x="SanjayGaneshTathe"
k=""
for i in x:
    if i.isupper():
        k=k+" "+i
    else:
        k=k+i
print(k)
'''
#-------------------------------------------------------------------------
# dictionary
'''
x=['sanjay','rahul']
y=[125000,120000]
d={i:j for i,j in zip(x,y)}
print(d)
'''

'''
x={
   'math':25,
   'science':14,
   'English':35
    }
print(max(x,key=x.get))
'''
'''
course = {
    'python': {'duration': '2 month', 'fees': 8000},
    'java': {'duration': '4 month', 'fees': 10000},
    'c++': {'duration': '3 month', 'fees': 6000},
}

#print(course.keys())
#print(course.values())
#print(course.items())


#del course['python']
#print(course)

#course.pop('python')
#print(course)


#add={'Django': {'duration': '3 month', 'fees': 6000}}
#course.update(add)
#print(course)

#course.pop('python')
#print(course)

#print(course.get('python'))
'''
'''
person = {"name": "Jessa", 'country': "USA"}

person.update({"weight": 50, "height": 6})

print(person)
'''
'''
person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178}
key_name = 'country'
if key_name in person.keys():
    print("country name is", person[key_name])
else:
    print("Key not found")
'''
#----------------------------------------------------------------------------------



# v=lambda x,y:x+y
# print(v(5,3))

# x=lambda i : 1 if i==0 else i*x(i-1)
# print(x(5))

# ----------------------------------------------------------------------------

# filter
# x=[1,2,3,4,5,6]
# y=list(filter(lambda z: z%2==0,x))
# print(y)

# def evenodd(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# list1=[1,2,3,4,5,6,7,8,9]
# result=list(filter(evenodd,list1))     filter(function,sequence)

# print(result)

# -------------------------------------------------------------------------

# map
# x=[4,5,3,2,8]
# y=[5,9,7,2,3]
# z=list(map(lambda x,y:x+y,x,y))
# print(z)


# y=[5,9,7,2,3]
# z=list(map(lambda n:n*n,x))
# print(z)

# ------------------------------------------------------------------------------------

# from functools import reduce
# n=[1,5,2,3,4,5,3]
# z=reduce(lambda a,b:a+b,n)
# print(z)


# n=[1,5,2,7,4,5,3]
# c=reduce(lambda x,y:x if x>y else y,n)
# print(c)



# x=[1,2,3,4,5,6]
# y=list(map(lambda i: i if i%2==0 else 0,x))
# print(y)

#-----------------------------------------------------------------------------------
#Decorator
'''
def decor2(fun):
    def inner(x,y):
        d=fun(x,y)
        add=d+10
        return add
    return inner

# @decor2
def decor1(x,y):
    c=x+y
    return c
# print(decor1(5,9))

x=int(input("enter the value :- "))
y=int(input("enter the value :- "))
v=decor2(decor1)
print(v(x,y))
'''

'''
def decor1(num):
    def inner(x,y):
        d=num(x,y)
        add=d*10
        return add
    return inner
def decor2(num):
    def inner(x,y):
        d=num(x,y)
        add=d+3.5
        return add
    return inner
# @decor2            last execution
# @decor1            first execution
def decor(x,y):
    c=x+y
    return c
# print(decor(3,9))
v=decor2(decor1(decor))
print(v(3,9))  # 123.5

'''


# def decor2(fun):
#     def inner():
#         d=fun()
#         totalbal=d-withdraw*0.10
#         return totalbal
#     return inner
# @decor2
# def decor1():
#     bal=amt-withdraw
#     return bal
# amt=int(input("enter your amount :- "))
# withdraw=int(input("enter withdraw amount :- "))
# print(decor1())


'''
def decor1(num):
    def inner():
        print('-----------------------------')
        num()
        print('-----------------------------')
        
    return inner
def decor2(num):
    def inner():
        print('*****************************')
        num()
        print('*****************************')
        
    return inner
@decor1
@decor2
def decor():
    print('welcome')
decor()
'''
#     --------------
#     **************
#       welcome
#     --------------
#     **************
# -----------------------------------------------------------------------------

# defining a decorator
# def hello_decorator(func):

#     def inner1():
#         print("Hello, this is before function execution")
#         func()
#         print("This is after function execution")
         
#     return inner1
# def function_to_be_used():
#     print("This is inside the function !!")
# function_to_be_used = hello_decorator(function_to_be_used) 
# function_to_be_used()

# --------------------------------------------------------------------------------------------

# def abc(num):
#     def inner(name):
#         # d=num(name)
#         if name=="sunny":
#             print("hello SUNNY bad morning")
#         else:
#             num(name)
#     return inner
# @abc
# def wish(name):
#     print("hello",name,"good morning")
# wish("sanjay")
# wish("rohit")
# wish('sunny')

# --------------------------------------------------------------------------------------------

# return multiple value

# def cal(x,y):
#     sum=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return sum,sub,mul,div
# a,b,c,d=cal(2,4)
# print(a,b,c,d)

#-----------------------------------------------------------------------------------

# recursion 

# def facto(x):
#     if x==0:
#         fact=1
#     else:
#         fact=x*facto(x-1)
#     return fact
# print(facto(4))


#-----------------------------------------------------------------------------------


# x='A3G4B2'
# k=""
# for i in x:
#   if i.isalpha():
#     y=i
#     g=ord(i)

#   else:
#     digit=int(i)
#     k=k+(y+chr(g+digit))

# print(k)

# output= 'ADGKBD'

#-----------------------------------------------------------------------------
'''
for i in x:
  if i.isalpha():
    y=i
    g=ord(i)

  else:
    digit=int(i)
    t=g+digit
    if t<90:
      k=k+(y+chr(t))
    else:
      k=k+(y+chr(64+(t-90)))
print(k)
'''
#-----------------------------------------------------------------------
# n program to find Cumulative sum of a list Break a list into chunks of size N in
l=[1,2,3,4,5,6,7,8,9]
n = 4
x = [l[i:i + n] for i in range(0, len(l), n)]
print(x)
#-------------------------------------------------------------------------


# Python program to sort values of first list based on second list
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
a = list(set(list2))
a.sort()
res = []
for i in a:
    for j in range(0, len(list2)):
        if(list2[j] == i):
            res.append(list1[j])
print(res)

#-------------------------------------------------------------------
# Python Ways to remove i’th character from string
x="sanjay"
n=3
a=x[:n]
b=x[n+1:]
print(a+b)
#-------------------------------------------------------------------
## Python | Program to accept the strings which contains all vowels
s=input("enter the string :- ")
v="aeoiu"
t=set(s).intersection(v)
print(type(t))
if t==set(v):
    print("yes")
else:
    print("no")
#-------------------------------------------------------------------


#######################################################################
##########################################################################


'''
class Employee:
    def __init__(self):
        self.salary=22000
        self.age=21
e1=Employee()
print(e1.__dict__)
print(e1.salary)
'''
#----------------------------------------
'''
class Employee:
    def __init__(self,salary,age):
        self.salary=salary
        self.age=age
    def display(self):
        print(f"salary is {self.salary} and agr is {self.age}")
        
e1=Employee(125000,25)
print(e1.salary)  # access attribute outside class
e1.salary=130000
print(e1.salary) # upadte attribute
e1.display()
'''
#------------------------------------------------
'''
class Employee:
    def __init__(self,salary,age):
        self.salary=salary
        self.age=age
    def display(self):
        print(f"salary is {self.salary} and agr is {self.age}")
        
e1=Employee(125000,25)
e1.display()
print(getattr(e1,'age'))
print(setattr(e1,'salary',200000))
print(e1.__dict__)
delattr(e1,'age')
print(e1.__dict__)
'''
#----------------------------------------------------
'''
class Employee:
    # this is details of employee 
    def __init__(self,salary,age):
        self.salary=salary
        self.age=age
    def display(self):
        print(f"salary is {self.salary} and agr is {self.age}")
        
e1=Employee(125000,25)
print(Employee.__doc__)
print(e1.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(isinstance(e1,Employee))
'''
#----------------------------------------------------
'''
class Employee:
    
    def __init__(self,salary,age):
        self.salary=salary
        self.age=age
    def display(self):
        print(f"salary is {self.salary} and agr is {self.age}")
        
e1=Employee(125000,25)
e1.city='nagpur'  # create new instance variable outside class
print(e1.__dict__)
del e1.age
print(e1.__dict__)
'''
#---------------------------------------------------------------
# class method
''' 
class Employee:
    company='google'  # class variable
    def __init__(self,salary,age):
        self.salary=salary
        self.age=age
    @classmethod
    def display(cls):
        cls.company='tcs'
        print("comany :- ",cls.company)
        
        
e1=Employee(125000,25)
print(Employee.company)
print(e1.company)
#Employee.company='facebook'
print(Employee.company)
e1.display()
'''
#---------------------------------------------------------
#setter and getter
'''
class Employee:
    def setname(self,nm):
        self.name=nm
    def getmethod(self):
        print(self.name)
e1=Employee()
e1.setname(input("enter the name : - "))
e1.getmethod()
'''
#-----------------------------------------------------------
# static method
'''
class Bank:
    bank='SBI'
    rate=12.25
    @staticmethod
    def simple(prin,n):
        si=(prin*n*Bank.rate)/100
        print(si)
Bank.simple(100,2)
'''
#---------------------------------------------------------------
# Inheritance
# Single level inheritance
'''
class employee:
    def inputdata(self):
       self.a=int(input("enter the no :- "))
       self.b=int(input("enter the no :- "))
class manager(employee):
    def calculation(self):
       super().inputdata()
       c=self.a+self.b
       print(c)
emp=manager()
#emp.inputdata()
emp.calculation()
'''
#---------------------------------------------------------------
# multiple inheritance
'''
class student:
    def class1(self):
        self._mark1=(int(input("enter the marks 1: ")))
        self._mark2=int(input("enter the marks 2: "))
        self._mark3=int(input("enter the marks 3: "))
class cricket():
    def class2(self):
        self._score1=int(input("enter the score 1: "))
        self._score2=int(input("enter the score 2: "))

class total(student,cricket):
    def class3(self):
        super().class1()
        super().class2()
        self.__tm=self._mark1+self._mark2+self._mark3
        self.__ts=self._score1+self._score2
        print(self.__tm)
        print(self.__ts)
c=total()
# c.class1()
# c.class2()
c.class3()
'''
#---------------------------------------------------------------
# multilevel inheritance
'''
class A:
    def method1(self):
       self.a=int(input("enter the no :- "))
       self.b=int(input("enter the no :- "))
class B(A):
    def method2(self):
       self.c=self.a+self.b
class C(B):
    def method3(self):
       d=self.c*10
       print(d)
o=C()
o.method1()
o.method2()
o.method3()
'''
#---------------------------------------------------------------
#Hierarchiel inheritance
'''
class A:
    def method1(self):
       self.a=int(input("enter the no :- "))
       self.b=int(input("enter the no :- "))
class B(A):
    def method2(self):
       self.c=self.a+self.b
       print(self.c)
class C(A):
    def method3(self):
       self.d=self.a*self.b
       print(self.d)
      
o=B()
o.method1()
o.method2()
k=C()
k.method1()
k.method3()
'''
#----------------------------------------------------------------------
# hybrid inheritance
'''
class student:
    def msg1(self):
        print("hello")
class cs(student):
    def msg2(self):
        print("welcome")
class ce(student):
    def msg3(self):
        print("to")
class college(cs,ce):
    def msg4(self):
        print("nagpur")
d=college()
d.msg1()
d.msg2()
d.msg3()
d.msg4()
'''
#--------------------------------------------------------------------------------
# # self call method

# class A:
#     def method1(self):
#       print("Hello.. nagpur")
# class B:
#     def method2(self):
#       self.z=A()
#       self.z.method1()
#       print("Hello... pune")
# obj=B()
# obj.method2()
#-------------------------------------------------------------------

# encapsulation

# class Car:
#     def __init__(self):
#         self.x="sanjay"
#     def drive(self):
#         print("driving : ",self.x)
# backcar=Car()
# backcar.drive()

#--------------------------------------------------------------------------

# # overloading

# # class A:
# #     def method1(self,a,b):
# #         print(a+b)
# #     def method1(self,a,b):
# #         print(a*b)
# # obj=A()
# # obj.method1(20,21)



# # # overriding

'''
class A:
     def method1(self,a,b):
         self.a=a
         self.b=b
         print(self.a+self.b)
class B(A):
     def method1(self,a,b):
        super().method1(10,3)
        print(self.a*self.b)
obj=B()
obj.method1(20,21)
'''
#--------------------------------------------------------------------------

# abstract method

# from abc import ABC, abstractmethod

# class Father(ABC):
#     @abstractmethod
#     def dis(self):
#         pass

#     def show(self):
#         print("concrete method")

# class  Child(Father):
#     def dis(self):
#         print("child class")
#         print("defining abstract method")
# obj=Child()
# obj.show()
# obj.dis()
#--------------------------------------------------------------------------
#static method
'''
class Employee:
    @staticmethod
    def sample(x):
        print('Inside static method', x)

# call static method
Employee.sample(10)

# can be called using object
emp = Employee()
emp.sample(10)
'''
#--------------------------------------------------------------------------
# instance method
'''
class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method to access instance variable
    def show(self):  # instance method
        print('Name:', self.name, 'Age:', self.age)
emma = Student("Jessa", 14)
# call instance method
emma.show()
'''
#-------------------------------------------------------------------------------
# class method
'''
class Student:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, school_name):
        # class_name.class_variable
        cls.school_name = school_name

    # instance method
    def show(self):
        print(self.name, self.age, 'School:', Student.school_name)

jessa = Student('Jessa', 20)
jessa.show()

# change school_name
Student.change_school('XYZ School')
jessa.show()
'''
#--------------------------------------------------------------------------
# private variable
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

# creating object of a class
emp = Employee('Jessa', 10000)

# calling public method of the class
emp.show()

#---------------------------------------------------------------------

# mangling method

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Jessa', 10000)

print('Name:', emp.name)
# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)


############################################################################################
###########################################################################################

# Regular Expression
'''
import re
x="Sanjay Ganesh tathe team Brain Work123"
print(re.findall("[A-Z][a-z]+",x)) #['Sanjay', 'Ganesh', 'Brain', 'Work']

print(re.findall("[A-Z][a-z]+[0-9]+",x)) # ['Work123']

x='sanjay@tathe$team'
print(re.findall("\W",x)) # ['@', '$']

x='sanjay@tathe$team123'
print(re.findall("\w",x)) # ['s', 'a', 'n', 'j', 'a', 'y', 't', 'a', 't', 'h', 'e', 't', 'e', 'a', 'm']

x="sanjay tathe"
print(re.findall("\s",x)) # [' ']

x="sanjay tathe"
print(re.findall("\S",x)) # ['s', 'a', 'n', 'j', 'a', 'y', 't', 'a', 't', 'h', 'e']

x="sanjay 123 tathe" 
print(re.findall("\d+",x)) # ['123']

x="sanjay 123 tathe" 
print(re.findall("\D+",x)) # ['sanjay ', ' tathe']


a=re.finditer("an","sanjay")
for i in a:
     print(i.start(),i.group())  #1 an


x="sanjay 123 tathe" 
print(re.sub("sanjay","SANJAY",x)) #SANJAY 123 tathe

x='sanjay@tathe@team'    
print(re.split("@",x))   # ['sanjay', 'tathe', 'team']

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x.group())     # ai

x="^[a-z][a-zA-Z0-9]+[@][a-z]+[.com]"
y=input("enter the email :- ")
if re.search(x,y):
    print("valid email")
else:
    print("Invalid email")

'''
#----------------------------------------------------------------------------------------

# try:
#     x=int(input("enter the age :- "))
#     if x<0:
#         raise ValueError
#     print("your age is : ",x)
# except ValueError:
#     print("you entered invalid age")
# ---------------------------------------------------------
# try:
#     amt=int(input("enter the amount : - "))
#     withd=int(input("enter the withdraw amount : - "))
#     bal = amt-withd
#     if bal<0:
#         raise Exception
#     print("your balance is : ",bal)
# except Exception:
#     print("your amount low")
# --------------------------------------------------------------
# try:
#     c=10/3
#     print(c)
#     print("code executed successfully")
# except Exception as e:
#     print(e)
# else:
#     print("welcomee")
# --------------------------------------------------------------------
# try:
#     c=10/0
#     print(c)
#     print("code executed successfully")
# except Exception as e:
#     print(e)
# else:
#     print("welcomee")
# --------------------------------------------------------------------
# a = [1, 2, 3]
# try: 
#     print ("Second element = %d" %(a[1]))
#     print ("Fourth element = %d" %(a[3]))
# except:
#     print ("An error occurred")
# -----------------------------------------------------------------------------
# def fun(a):
#     if a < 4:
  
#         b = a/(a-3)
    
#     print("Value of b = ", b)     
# try:
#     fun(2)
#     fun(5)

# except ZeroDivisionError:
#     print("ZeroDivisionError Occurred and Handled")
# except NameError:
#     print("NameError Occurred and Handled")
# -----------------------------------------------------------------------------------------

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# --------------------------------------------------------------------------------

# try:
#   f = open("sanjay.txt",'w')
#   try:
#     f.writa("Lorum Ipsum sanjay 111")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")


#-----------------------------------------------------------------------------


# Python program to read file word by word
# 1) x=open("test2.txt","r")
# f=x.read()
# for i in f.split():
#     print(i)

#-------------------------------------------------------------------------------------
#  Python program to read character by character from a file
# 2) x=open("test2.txt","r")
# f=x.read()
# for i in f:
#     print(i)

#-----------------------------------------------------------------------------------------
#  Python – Get number of characters, words, spaces and lines in a file

# 3) character
# x=open("test2.txt","r")
# f=x.read()
# count=0
# for i in f:
#     count=count+1
# print(count)
#

# word
# x=open("test2.txt","r")
# f=x.read()
# count=0
# for i in f.split():
#     count=count+1
# print(count)
#
# # space
# x=open("test2.txt","r")
# f=x.read()
# count=0
# for i in f:
#     if i==" ":
#      count=count+1
# print(count)

#--------------------------------------------------------------------------------------------------------
# 4. Python | Finding ‘n’ Character Words in a Text File
# 4) x=open("test2.txt","r")
# f=x.read()
# n=int(input("enter the no of character :- "))
# for i in f.split():
#     if len(i)==n:
#         print(i)
#
#-------------------------------------------------------------------------------------------------------------
# Python Program to obtain the line number in which given word is present

# 5) x = open("test2.txt", "r")
# z = x.readlines()
# # print(z)
# d = 1
# h = "taxpayer"
# for i in z:
#     if h in i:
#         print(d)
#     d += 1
# x.close()

#------------------------------------------------------------------------------------------------------------------
# 6. Count number of lines in a text file in Python

# 6)x=open("test2.txt","r")
# f=x.readlines()  return line in list
# count=0
# for i in f:
#     count=count+1
# print(count)

#--------------------------------------------------------------------------------------------------------------------
#  Python Program to Eliminate repeated lines from a file
# 7) x=open("test2.txt","r")
# z=x.readlines()
# print(set(z))

#-----------------------------------------------------------------------------------------------------------------------
#  Python – Append content of one text file to another
# 

#8) x=open("test.txt","r")
# f=x.read()
# print(f)
#
# x=open("test2.txt","a")
# x.write("\n")
# x.write(f)

#-------------------------------------------------------------------------------------------------------------------------------
# 1. Python program to Reverse a single line of a text file
# 
# 11)f1=open("test2.txt","r")
# lines=f1.readlines()
# c=0
# line=lines[c].split()
# r=" ".join(line[::-1])
# lines.pop(c)
# lines.insert(c,r)
# z=open("test",'w')
# z.writelines(lines)
# z.close()
#------------------------------------------------------------------------------------------------------------------------
#  Python program to reverse the content of a file and store it in another file

# 12) writeFile = open("test.txt", "w")
# with open("test2.txt", "r") as readFile:
#     txt = readFile.read()
# reversedContent = txt[::-1]
# writeFile.write(reversedContent)
# writeFile.close()
#------------------------------------------------------------------------------------------------------------------------
# for reading

# with open("C:\\Users\\Asus\\Desktop\\111.txt","r") as e:
#   y=e.read()
#   print(y)

# ------------------------------------------------------------------
# for writing and crating file

# with open("C:\\Users\\Asus\\Desktop\\222.txt","w") as e:
#   e.write("Hello....")
  
#--------------------------------------------------------------------

# x=open('sanjay.txt','r+')

# t=x.read()
# print(t)
# x.write('llll')
# x.close()

# -----------------------------------------------------------------------------

# file = open("sanjay.txt", "r")
# print (file.read())


# --------------------------------------------------------------------------------------

# file = open("sanjay.txt", "r")
# print (file.read(5))

# -----------------------------------------------------------------------------

# file = open('sanjay.txt','w')
# file.write("This is the write command")
# file.write("\n")
# file.write("It allows us to write in a particular file")
# file.close()


# -----------------------------------------------------------------------------


# import os
# os.remove("sanjay1.txt")

# import os
# if os.path.exists("sanjay1.txt"):
#   os.remove("sanjay1.txt")
# else:
#   print("The file does not exist")

# -------------------------------------------------------------------------------


# # for delete file
# import os
# os.remove("demofile.txt")


# # for removing folder
# import os
# os.rmdir("sanjay")

#-----------------------------------------------------------------------------------------

# dic to string
# import json
# x={"a":30,"b":50}
# y=json.dumps(x)
# print(y)
# print(type(y))

# ------------------------------------------
#  string to dictionary
# import json
# x='{"a":30,"b":50}'
# print(type(x))
# y=json.loads(x)
# print(y)
# print(type(y))

# ----------------------------------------------------------------

# data load from json file
# import json
# data=open("D:\\vscode\\v.json","r")
# y=json.load(data)
# print(y)
# print(type(y))
# print(type(data))

# ------------------------------------------------------------------
# add data in json file

# import json
# data=open("D:\\vscode\\v.json","r")
# y=json.load(data)
# x=[{"rohit": 100}]
# y.append(x)
# z=json.dump(y,open("D:\\vscode\\v.json","w"))
# print(y)
# ---------------------------------------------------------------------------------

# import json
'''
 print("Started Reading JSON file")
 with open("D:\\vscode\\developer.json", "r") as read_file:
     print("Converting JSON encoded data into Python dictionary")
     developer = json.load(read_file)

     print("Decoded JSON Data From File")
     for key, value in developer.items():
         print(key, ":", value)
     print("Done reading json file")
'''
#------------------------------------------------------------------------------------------
# multithrading
'''
from threading import *
def twice(num):
    for i in num:
        print(2*i)
def display(num):
    for i in num:
        print(i*i)
num=[1,2,3,4,5,6,7,8,9]
t1=Thread(target=twice,args=(num,))
t2=Thread(target=display,args=(num,))
t1.start()
t1.join()
t2.start()
'''

#------------------------------------------------------------
# logging
'''
from logging import *
basicConfig(filename='sanjay.log',level=DEBUG,format="%(asctime)s-----%(message)s",filemode='w')
x=10
y=15
sum=x+y
debug(f"dum of {sum}")
'''
#----------------------------------------------------------------

# x=(1,8,5,6,3,7)
# print(sorted(x))  # [1, 3, 5, 6, 7, 8] 

# -------------------------------------------------------------------------

# def gen(n):
#     x=0
#     while x<n:
#         yield x
#         x +=1
# v=gen(4)
# print(next(v))
# print(next(v))
# print(next(v))
# print(next(v))
# print(next(v)) # generator shows stops iteration

#--------------------------------------------------------------------------------------------

# x=50
# def func(x):
#     print(x) # 50
#     x=2
#     print(x) # 2
# func(x)
# print(x)     # 50

#--------------------------------------------------------------------------

# class Dog:
#     def walk(self):
#         return 'walking'
#     def speak(self):
#         return 'woof'
# class Animal(Dog):
#     def talks(self):
#         return super().speak()
# bobo=Animal()
# print(bobo.talks())  # woof

#--------------------------------------------------------------------------
# x=[1,2,3,4,5,6]
# y=list(map(lambda x:x%2==0,x))
# print(y) #[False, True, False, True, False, True]
#--------------------------------------------------------------------------
# x=[1,2,3,4,5,6]
# y=list(filter(lambda x:x*2,x))
# print(y) # [1, 2, 3, 4, 5, 6]
#--------------------------------------------------------------------------
# tuple1=(1,2,3)
# tuple1[0]=5
# print(tuple1)   #'tuple' object does not support item assignment

#--------------------------------------------------------------------------
# print({'a':1,'b':2,'a':3})  # {'a': 3, 'b': 2}
#--------------------------------------------------------------------------
# for i in range(5):
#     for j in range(i,5-1):        
#         print("*", end=" ")
#     for j in range(i+1):
#         print("$",end=" ")
#     print()

# # * * * * $ 
# # * * * $ $ 
# # * * $ $ $
# # * $ $ $ $
# # $ $ $ $ $
# ---------------------------------------------------------------------------------
# s1={1,2,3,4,5}
# s2={2,5,6}
# print(s1 ^ s2)  # {1, 3, 4, 6}
# U-Union
# n- intersection
# ^-differnce
# ---------------------------------------------------------------------------------
# 2) match  only match with start

# import re
# a=re.match('sa','sanjay')
# print(a.start(),a.group())



































