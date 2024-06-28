#-----------------------------------------------------------------------------18-04-024--------------------------------------------------------------------------------------------------------------
'''n=int(input( ))
count=0
while(count<n):
    count=count+1
    print("hey")
'''
'''for i in range(6):
    for j in range(i):
        print("*",end="")
    print("")'''
'''for i in range(1,6):
    print('*'*i)
'''
'''for i in range(5,0,-1):
    print('*'*i)'''
'''def palindrome():
    s=s.lower()
    return s==s[::-1]
print("dhyana")
'''
'''a=int(input("enter number for a:"))
b=int(input("enter number for b:"))
c=int(input("enter number for c:"))
d=b**2-4*a*c
sol1=(-b+(d**0.5))/(2*a)
sol2=(-b-(d**0.5))/(2*a)
print("the solution {0} and {1}".format(sol1,sol2))'''
'''num=int(input("enter any number:"))
sum=0
for i in range(num):
    sum = sum + int(i)
print(sum)'''
'''def palindrome(s):
    s = s.replace("","").lower()
    return s == s[::-1]
word = input("enter the word:")
if palindrome(word):
    print("palindrome")
else:
    print("not palindrome")
    '''
'''first=0
second=1
print(first)
print(second)
for i in range(2,10):
    next = first + second
    first = second
    second = next
    print(next)'''
'''for i in range(1,6):
    print(chr(64+i)*i)
   '''
'''def add(a,b):
    return a+b
x = int(input("enter a number:"))
y = int(input("enter a number:"))
result = add(x,y)
print(result)


def sub(a,b):
    return a-b
x = int(input("enter a number:"))
y = int(input("enter a number:"))
result = sub(x,y)
print(result)


def mul(a,b):
    return a*b
x = int(input("enter a number:"))
y = int(input("enter a number:"))
result = mul(x,y)
print(result)


def div(a,b):
    return a%b
x = int(input("enter a number:"))
y = int(input("enter a number:"))
result = div(x,y)
print(result)'''
'''list = []
for i in range(0,101):
    if i%10 == 0:
        print(i)'''
'''divisible = [num for num in range(1,101) if num%10==0]
print(divisible)
'''
'''def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result
x = int(input("enter any number:"))
y = int(input("enter any number:"))
for num in range(x,y+1):
    print("the factorial is:")'''
#-----------------------------------------------------------------------------------19-04-2024------------------------------------------------------------------------------------------------------
'''a=int(input("enter a number:"))
b=int(input("enter a number:"))
a=a+b
b=a-b
a=a-b
print(a)
print(b)'''
'''def f1(n):
    s=n(n+1)/2
    return(s)
n=int(input("enter any number:"))
result=f1(n)
print(result)'''
'''str1=str(input(""))
str2=str(input(""))
str=str1+" " +str2
print(str)
print(str.upper())
print(str.capitalize())'''
'''list=[2,6,87,9,5,7,8,8,88,8,9,9,0,00,0]
print(len(list))
user=int(input("enter any number:"))
print(list.count(user))
l=list.append(100)
print(list)
l=list.remove(87)
print(list)
#index
print(list.index(2))
#insert
l=list.insert(0,1000)
print(list)
print(list.index(10))'''
'''l=[2,4,65,7,8,98,6,54,43,3]
for i in l:
    print(i)'''
'''l = [1,2,3,4,6,76,8,98,9,99]
i = 0
while i < len(l):
  print(l[i])
  i = i + 1
'''
'''l=[1,4,6,7,878,9,9,00,87,6,6,6,4,3,333]
sindex=int(input("enter starting slicing index:"))
eindex=int(input("enter ending slicing index:"))
print(l[sindex:eindex])'''
'''l=[]
for i in range(10,21):
    if i %2==0:
        l.append(i)
print(tuple(l))
'''
''''e=tuple(x for x in range(10,21) if x%2==0)
print(e)'''
'''t=(1,2,4,6,8,9,87,5,4,3,5,13,8,9,3,4,8,7,6,3,3)
print(t.index(8))
print(t[2:6])
t1=(1,2,3,4)
t2=(5,6,7,8)
t3=t1+t2
print(t3)
t4=t3*2
print(t4)
t5=t.append(10)
print(t)'''
'''s=str(input("enter any string:"))
for i in range(0,10):
    print(s)
'''
'''s=str(input("enter any word:"))
s1=s.replace("is","was")
print(s1)
'''
'''s="hi nanna"
a=s.find("nanna")
print(a)
b=s.index("hi")
print(b)
'''
'''str1=str(input("enter a string:"))
str2=str(input("enter a string:"))
if(len(str1)==len(str2)):
    if(sorted(str1)==sorted(str2)):
        print("true")
    else:
        print("false")
'''
'''num=int(input("enter a number:"))
if num%1==0 and num%num==0:
    print("prime")
else:
    print("not prime")'''
#--------------------------------------------------------------------------------------20-04-2024---------------------------------------------------------------------------------------------------
'''def vowels(string):
    string=str(input("enter any string:"))
    vowels='aeiouAEIOU'
    count=0
    for i in string:
        if i in vowels:
            count+=1
    return(count)'''
'''s=str(input("enter any string:"))
vowels='aeiouAEIOU'
count=0
for i in s:
    if i in vowels:
        count+=1
print("the vowels count is:",count)'''
'''def prime(n):
    c=0
    for i in range(0,n):
        if i%2==0:
            c+=1
    if c<=2:
        return 1
    else:
        return 0
n=int(input("no:"))
print(prime(n))'''
'''#pattern
def pattern(n):
    for i in range(1,2*n):
        for j in range(1,2*n):
            print(max(abs(i-n),abs(j-n))+1,end="")
    print()
    '''
#------------------------------------------------------------------------------------------22-04-2024-----------------------------------------------------------------------------------------------
'''for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end='')
    print()'''
'''n=int(input(""))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
        i=i-1
    print()
'''
'''start=1
stop=2
num=stop
for i in range(2,6):
    for j in range(start,stop):
        num-=1
        print(num,end="")
    print("")
    start=stop
    stop+=i
    num=stop'''
'''for i in range(1,6):
    n=1
    for j in range(6,0,-1):
        if j>i:
            print(" ",end=' ')
        else:
            print(n,end=' ')
            n+=1
    print(" ")'''
'''b = lambda a : a ** a
print(b(2))'''



'''b = lambda a : print(*range(1,a+1))
b(10)'''


'''word=input("enter word:")
n=list(filter(lambda x:(len(x)>5), word))
print(n)'''


'''word = str(input("enter any word:"))
for i in word:
    if words<=5:
        print("")
else:
    print("")
'''



'''l=['dhanalakshmi','hai nanna','hellooo','okay']
x=list(filter(lambda b:len(b)>5,l))
print(x)'''

'''palindrome=str(input())
x=list(((filter(lambda b:b==b[::-1],palindrome))))
print(x)'''



#----------------------------------------------------------------------------------------23-04-2024--------------------------------------------------------------------------------------------------
'''prime=lambda n:all(n%i!=0 for i in range(2,int(n**0.5)+1))
print([x for x in range(2,101) if prime(x)])
'''



'''marks={"dhana":90,"abhi":99}
passingstudent=dict(filter(lambda x:x[1]>=60,marks.items()))
print(passingstudent)'''


'''for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
for i in range(5,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print(" ")'''



'''for i in range(0,5):
    print("*"*i)
for i in range(5,0,-1):
    print("*"*i)'''





#----------------------------------------------------------------------------------------------------24-04-2024-------------------------------------------------------------------------------------



'''for i in range(0,5):
    for j in range(i,-1,-1):
        print(2**j,end=" ")
    print()'''



'''n=int(input())
res=bin(n)
print(res)
'''



'''n=int(input())
binary=decimal_to_binary(n)
print(binary)'''
'''def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary
decimal = int(input("Enter a decimal number: "))
binary = decimal_to_binary(decimal)
print("Binary: " + binary)'''



#----------------------------------------------------------------------------------------------25-04-2024--------------------------------------------------------------------------------------------
'''rows=int(input())
for i in range(rows):
    for j in range(i,rows%2==0):
        print(j)
    print('')'''
'''class Demo:
    a=10
demoobj=Demo()
print(demoobj.a)
'''
'''class Demo:
    def sumvalue(self):
        print(20+30)
demoobj=Demo()
demoobj.sumvalue()'''
'''class Demo:
    a=int(input())
    def value(self):
        print(self.a)
obj=Demo()
obj.value()'''
'''class Demo:
    a=int(input())
    b=a*a
    def value(self):
        print(self.b)
obj=Demo()
obj.value()'''
'''class Demo:
    def __init__(self,name):
        self.name=name
obj=Demo("remo")
print(obj.name)'''
'''rows=5
for i in range(1,rows+1):
    for j in range(1,rows+1):
        square=i*j
        print(i*j,end='')
    print()'''
'''n=int(input())
count=0
for i in range(0,n+1):
    for j in range(0,i+1):
        print(count, end=' ')
        count=2**(i+1)
    print()'''
'''for i in range(4,0,-1):
    for j in range(1,i+1):
        if j==i:
            print(j,end="")
        else:
            print(j,end="*")
    print()'''
'''rows=int(input())
for i in range(rows):
    for j in range(i+1):
        print(i*j,end=" ")
    print()'''
'''for i in range(3,0,-1):
    for j in range(i*i):
        print(j,end=" ")
    print()'''
#--------------------------------------------------------------------------------------------26-04-2024----------------------------------------------------------------------------------------------
'''for i in range(3):
    for j in range(i):
        print('#')
    ##    print('')
 '''   
'''def calculate(self):
        self.avg = sum(self.scores)/len(self.scores)
        self.grade = ''
        if self.avg <= 100 and self.avg >=90:
            self.grade = 'O'
            return self.grade
        elif self.avg < 90 and self.avg >=80:
            self.grade = 'E'
            return self.grade
        elif self.avg < 80 and self.avg >=70:
            self.grade = 'A'
            return self.grade
        elif self.avg < 70 and self.avg >=55:
            self.grade = 'P'
            return self.grade
        elif self.avg < 55 and self.avg >=40:
            self.grade = 'D'
            return self.grade
        elif self.avg < 40:
            self.grade = 'T'
            return self.grade'''
'''# Import required modules 
from abc import ABC, abstractmethod 

# Create Abstract base class 
class Car(ABC): 
def __init__(self, brand, model, year): 
	self.brand = brand 
	self.model = model 
	self.year = year 
	
# Create abstract method	 
@abstractmethod
def printDetails(self): 
	pass
	
# Create concrete method 
def accelerate(self): 
	print("speed up ...") 
	
def break_applied(self): 
	print("Car stop") 
	
# Create a child class 
class Hatchback(Car): 
	
def printDetails(self): 
	print("Brand:", self.brand); 
	print("Model:", self.model); 
	print("Year:", self.year); 
	
def Sunroof(self): 
	print("Not having this feature") 
	
# Create a child class 
class Suv(Car): 
	
def printDetails(self): 
	print("Brand:", self.brand); 
	print("Model:", self.model); 
	print("Year:", self.year); 
	
def Sunroof(self): 
	print("Available") 

	
car1 = Hatchback("Maruti", "Alto", "2022"); 

car1.printDetails() 
car1.accelerate() '''
#----------------------------------------------------------------------------------------27-04-2024--------------------------------------------------------------------------------------------------
'''from abc import ABC, abstractmethod
import math
class Shape(ABC):
        @abstractmethod
        def area(self):
                pass
class Rectangle(Shape):
        def __init__(self,width,height):
                self.width=width
                self.height=height
        def area(self):
                return self.width*self.height
class Circle(Shape):
        def __init__(self,radius):
                self.radius=radius
        def area(self):
                return math.pi*self.radius**2
rectangle=Rectangle(5,4)
circle=Circle(3)
print(rectangle.area())
print(circle.area())'''
class Employee:
        def __init__(self):
                self.__salary=0
        def set_salary=salary(self,salary):
                self.__salary=salary
        def get_salary(self):
                return self.__salary
e=Employee()
e.set_salary(50000)
print(e.get_salary())
	









































































































































