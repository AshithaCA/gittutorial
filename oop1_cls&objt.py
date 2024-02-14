# class Human:
#     legs=2
#     eyes=2
#     def walking():
#         print('can walk')
#     def eating():
#         print('can eat')
        
# aby=Human
# aby.eating()
# print(aby.eyes)

# ash=Human
# ash.walking()
# print(ash.legs)

#12/10/23

# class Human:
#     legs=2
#     eyes=2
#     def walking():
#         print('can walk')
#     def eating():
#         print('can eat')
# anu=Human
# amu=Human
# print(id(anu))    
# print(id(amu))         #same id for anu and amu
# print(anu.legs)        #2
# print(amu.legs)        #2
# anu.legs=1
# print(anu.legs)        #1
# print(amu.legs)        #1  changes randinum vannu ath correct ayi varan vendi ahn function bracket
 
#..............................................................#


# anu=Human()
# amu=Human()        
# print(id(anu))    
# print(id(amu))           #different id for anu and amu
# print(anu.legs)        #2
# print(amu.legs)        #2
# anu.legs=1
# print(anu.legs)        #1
# print(amu.legs)        #2   function bracket koduthath kond changes vannilla
 
# Human.legs=5
# print(anu.legs)        #1
# print(amu.legs)        #5
# appu=Human
# print(appu.legs)       #5

#................................................................#

# class Human:
#     legs=2
#     eyes=2
#     def walking():
#         print('can walk')
#     def eating():
#         print('can eat')
# anu=Human()
# anu.walking()   #takes 0 positional arguments but 1 was given

# class Human:
#     legs=2
#     eyes=2
#     def walking(self):
#         print('can walk')
#     def eating():
#         print('can eat')
# anu=Human()
# anu.walking()   #can walk


# class Human:
#     legs=2
#     eyes=2
#     def __init__(self):
#         print('i am human')
#     def walking(self):
#         print('can walk')
#     def details(self,name,ph):
#         print('my name is',name)
# anu=Human()                     # ethra pravishem nammel object create cheyando appoyake init function print akum
# ash=Human()
# anu.details('anu thomas',123456)     #my name is anu thomas 

#o/p

# i am human
# i am human
# my name is anu thomas

#.....................................

# class Human:
#     legs=2
#     eyes=2
#     def __init__(self,n,p):
#         print('i am human my name is ',n,'my place is ',p)
#     def walking(v):
#         print(self.name,'can walk')   #.....here the name of self is v so itsa ERROR
# anu=Human('anu mohan', 'elkm')
# anu.walking()
#...................................................

# class Human:
#     legs=2
#     eyes=2
#     def __init__(self,n,p):
#         self.name=n
#         self.place=p
#         print('i am human my name is ',n,'my place is ',p)
#     def walking(v):
#         print(v.name,'can walk')
#         print(v.place, 'is a nice place')
# anu=Human('anu mohan', 'elkm')
# aniesh=Human('aniesh kumar','tvm')
# anu.walking()
# aniesh.walking()

#o/p ......... self object oriented ahn soname mari mari varm objectn anusarich

# i am human my name is  anu mohan my place is  elkm
# i am human my name is  aniesh kumar my place is  tvm
# anu mohan can walk
# aniesh kumar can walk
  
#........................................................

  
#1) write a program to create a class by name student and initialise attributes like name age & grade while creating an object        
#2) write a program to create a valid empty with the name students with no propersities
#3) write a program to create a class and using the class instant print all of the attributes of that object
#4) write a python class square define two methods that returns the square area and perimeter


#1) initialize

# class Student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
#     def details(self):
#         print('name:',self.name)
#         print('age:',self.age)
#         print('grade:',self.grade)
# anu=Student('abi',20,'A')


#print them

# class Student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
#     def details(self):
#         print('name:',self.name)
#         print('age:',self.age)
#         print('grade:',self.grade)
# anu=Student('abi',20,'A')
# anu.details()

#2)

# class Student:
#         pass   

#3)

# class Student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
#     def details(self):
#         print('name:',self.name)
#         print('age:',self.age)
#         print('grade:',self.grade)
# anu=Student('abi',20,'A')
# anu.details()
        

#4)  

# class Square:
#     def area():
#         return side*side
#     def perimeter():
#         return 4*side
# side=int(input('enter the side of a square: '))
# square=Square
# print(square.area())
# print(square.perimeter())

#....................OR......................


        
        
       
    


