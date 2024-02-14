# ABSTRACTION
            
            
# from abc import ABC,abstractmethod

# class Polygon:
#     @abstractmethod     #decorate
#     def area(self):
#         pass
#     def mymthd(self):
#         print('hello')
# class Rectangle(Polygon):
#     def hai(self):
#         print('i am rectangle')
#     def area(self):
#         print('rect area')

# # book=Rectangle()   #to create object for subclass of abstract class we need to create object for child class
# app=Polygon()
# app.area()
# app.mymthd()   #o/p hello


# POLYMORPHISM


#1)overload


# class Calculator:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# abi=Calculator
# abi.Calculator(2,3)  #it will not work because in python last funtion only work     