# built in method in oops

# 1) getattr()


# class Person:
#     name = 'mohan'
#     age = 12
#     country = 'india'

# # v=Person()
# # x=getattr(v,'name')  #o/p

# # x=getattr(v,'name1','not present') #o/p not present
# # print(x)

# x=getattr(Person,'name','notpersent')
# print(x)   #o/p mohan

# x=getattr(Person,'name1','not persent')
# print(x)    #not persent

#2) delattr()

# class Person:
#     name = 'mohan'
#     age = 12
#     country = 'india'

# print(Person.age)
# x=getattr(Person,'age','not persent')
# print(x)

# delattr(Person,'age')
# print(Person.age)   #error

#3) hasattr()

# class Person:
#     name = 'mohan'
#     age = 12
#     country = 'india'

# x=hasattr(Person,'age')  #o/p True

# x=hasattr(Person,'age1')  #o/p False
# print(x)
    
#4) setattr()

# class Person:
#     name = 'mohan'
#     age = 12
#     country = 'india'
    
# x=getattr(Person,'age')
# print(x)
# # setattr(Person,'age',50)
# # x=getattr(Person,'age')
# # print(x)    #o/p age=50 update cheyth varum

# setattr(Person,'age1',50)
# x=getattr(Person,'age1')
# print(x)    #o/p age1=50 puthiyath create cheythvarum

#5) issubclass()

# class Parent:
#     age = 50
# class Child(Parent):
#     name = 'annu'
#     age = 8
# x=issubclass(Child,Parent)
# print(x)                   #o/p True
# x=issubclass(Parent,Child)
# print(x)                   #o/p False


#6) super()

# class Parent:
    
#     def __init__(self,txt):
#         self.message = txt
#         print('............................')
#     def printmessage(self):
#         print(self.message)
        
# class Child(Parent):
    
#     def __init__(self,txt):
#         print('child aaaaaaaaaaaaaaaaaaaaaaaa')
#         super().__init__(txt)
#     def printmessage(self):
#         print('python')
#     def show(self):
#         print('welcome')
#         Parent.printmessage()
        
# class Child1(Child):
    
#     def __init__(self,txt):
#         super().__init__(txt)
#     def show(self):
#         print('welcome')
#         super().printmessage()
        
        
# x=Child('haiii')
# x.printmessage()       
# y=Child1('hello')
# y.show()

# class Student:
#     def __init__(self):
#         print('////////////////////////////////////////')
#     def mark(self):
#         print('obtain mark')
#     def study(self):
#         print('study for mark')
# class Dancer(Student):
#     def __init__(self):
#         print('...................................')
#         super().__init__(self)
#     def study(self):
#         super().study()                      #it is used to call both student and dancer study method
#         print('study for passion')
        
        
# appu=Student()
# anu=Dancer()
# anu.study()


        
        

#.............................................

# n=int(input('enter the humman year: '))
# if n<=2:
#     d=n*10.5
#     print(d)
# else:
#    d=(2*10.5)+((n-2)*4)   
#    print(d) 


#................................................... 

# class Student:
#     school='ilahia'
#     def __init__(self,i,n,a):
#         self.id=i
#         self.name=n
#         self.age=a
# obj1=Student(1,'sara',10)   
# obj2=Student(2,'jose',20)
# print(getattr(obj1,'name'))
# print(getattr(obj1,'id'))
# print(getattr(obj1,'age'))
# print(getattr(obj2,'name'))
# print(getattr(obj2,'id'))
# print(getattr(obj2,'age'))
# setattr(obj2,'name','kris')  
# print(getattr(obj2,'name') )   
# x=hasattr(Student,'place') 
# if x==False:
#     x=setattr(Student,'place','none') 
#     print(getattr(Student,'place')) 

# ...................................................

# class Student:
#     def __init__(self,n,m):
#         self.name=n
#         self.mark=m
        
# obj=Student('ammu',50)
# print(getattr(obj,'name')) 
# print(getattr(obj,'mark')) 
# print('.............................')
# setattr(obj,'name','appu') 
# setattr(obj,'mark',100)
# print(getattr(obj,'name')) 
# print(getattr(obj,'mark'))    


# .....................................................

# n= int(input('enter your unit usage: '))
# if n<=100:
#     print('no charge')
# elif n>100 and n<=200:
#     print((n-100)*5)
# else:
#     print(500+((n-200)*10))


#1) create a python class with name bank account with attribute for  holders name and  balance implement methods for 
# deposite and withdrawal ensuring that balance cannot go below 0  create an object and demonstarte deposite and withdrawal operation. 

# class Bank_account:
#     def __init__(self,h,b):
#         self.holdername=h
#         self.balance=b
#     def deposite(self,d):
#         self.balance=self.balance+d
#         print(self.balance)
#     def withdrawal(self,w):
#         if self.balance-w<0:
#             print('no withdrawal possible')
#         else:
#             print(self.balance-w)
            
# ash=Bank_account('annu',100)
# # ash.deposite(100)
# ash.withdrawal(100)
        
#define a base class shape with methode to calculate area and perimeter create subclass for specific shape like 
#circle and rectangle implement these methods in sub classes and calculate the area and perimeter for a circle and rectangle.


# from abc import ABC,abstractmethod

# class Shape:
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class Circle(Shape):
#     def __init__(self,r):
#         self.radius=r
#     def area(self):
#         print('area: ',3.14*(self.radius**2))
#     def perimeter(self):
#         print('perimeter: ',2*3.14*self.radius)
# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.length=l
#         self.breadth=b
#     def area(self):
#         print('area: ',self.length*self.breadth)
#     def perimeter(self):
#         print('perimeter: ',2*(self.length+self.breadth))

# # a=Shape()
# # a.area()
# # a.perimeter()

# b=Circle(2)
# b.area()
# b.perimeter()

# c=Rectangle(2,3)
# c.area()
# c.perimeter()


#create a abstract class with basic functionlity of a calculator and then implemnet a class with proper funtionality 
#the abstract class should  having all methods like addition, subtraction,multiplication and divide with basic implementation.

# from abc import ABC,abstractmethod

# class Calculator:
#     @abstractmethod
#     def addition(self):
#         pass
#     @abstractmethod
#     def subtraction(self):
#         pass
#     @abstractmethod
#     def multiplication(self):
#         pass
#     @abstractmethod
#     def division(self):
#         pass
# class Calk(Calculator):
#     def __init__(self,a,b):
#         self.num1=a      #public accessifers
#         self.num2=b
#     def addition(self):
#         print('Add: ',self.num1+self.num2)
#     def subtraction(self):
#         print('Sub: ',self.num1-self.num2)
#     def multiplication(self):
#         print('mul: ',self.num1*self.num2)
#     def division(self):
#         print('divi :',self.num1/self.num2) 


# c=Calk(3,6)
# c.addition()
# c.subtraction()
# c.multiplication()
# c.division()
  
  
  
#..........................................................



        #ACCESS MODIFERS
        
        
# class A:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print('name: ',self.name, 'age: ',self.age)
# # a=A('abi',20)
# # a.display()

# class B(A):
#     def __init__(self,name,age):
#         A.__init__(self,name,age)
#     def displaydetails(self):
#         self.display
        

#PROTECTED ASSCESS


# class A:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def _display(self):
#         print('name: ',self.name, 'age: ',self.age)
# # a=A('abi',20)
# # a.display()

# class B(A):
#     def __init__(self,name,age):
#         A.__init__(self,name,age)
#     def displaydetails(self):
#         self._display
        
        
#private ASSCESS
        
# class A:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __display(self):
#         print('name: ',self.name, 'age: ',self.age)
# # a=A('abi',20)
# # a.display()

# class B(A):
#     def __init__(self,name,age):
#         A.__init__(self,name,age)
#     def displaydetails(self):
#         self.__display



       
       
       

    

