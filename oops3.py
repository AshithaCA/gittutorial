#python class bulid in methods

# class Rectangle:
#     def __init__(self,l,w):
#         self.length=l
#         self.width=w
#     def perimeter(self):
#         return 2*(self.length+self.width)
#     def area(self):
#         return self.length*self.width
#     def display(self):
#         print('length =' ,self.length)
#         print('Width =' ,self.width)
#         print('Area =' ,self.area())
#         print('Perimeter =' ,self.perimeter())
# class Parallelopiped(Rectangle):
#     def __init__(self,a,b,c):
#         self.height=c
#         Rectangle.__init__(self,a,b)
#     def volume(self):
#         print('volume = ',self.length*self.width*self.height)
    
    
# rect=Rectangle(2,4)    
# rect.display()  

# par=Parallelopiped(2,4,6)
# par.display()
# par.volume()


# .........................................................



# class Person:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#     def display(self):
#         print('name= ',self.name)
#         print('age= ',self.age)  
# class Student(Person):
#     def __init__(self,x,y,section):
#         self.section=section
#         Person.__init__(self,x,y)
        
#     def displaystudent(self):
#         print('name = ',self.name)
#         print('age = ',self.age)
#         print('section = ',self.section)

# # per=Person('appu','12')
# # per.display()
# stu=Student('appu','21','hai')
# stu.displaystudent()
         
#define a base class shape with methode to calculate area nad perimeter create subclass for specific shape like circle 
# and rectangle implement these methods in sub classes and calculate the area and perimeter for a circle and rectangle