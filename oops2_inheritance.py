#Destructor
 
# class Soap:
#     def __init__(self,n):
#         self.name=n
#         print(self.name,'created')
#     def ingredients(self):
#         return 'colour','salt'
#     def __del__(self):
#         print(self.name,'lost.............')
# dove=Soap('dove')
# v=dove.ingredients()
# print(v)
# del dove
# chandrika=Soap('chandrika')
# v=chandrika.ingredients()
# print(v)

#inheritance

# class Human:
#     def __init__(self):
#         print('i am human')
#     def eat(self):
#         print('can eating')
# class Student(Human):     # inherite cheyan vandi function bracket ullil inherite cheyanda class name ezhutham
#     def __init__(self):
#         print('i am student')
#     def study(self):
#         print('can study')
# anu=Student()
# anu.study()
# anu.eat()

# class Father:
#     def __init__(self):
#         print('i am father')
#     def work(self):
#         print('can work')
# class Mother:
#     def __init__(self):
#         print('i am mother')
#     def multitasking(self):
#         print('always multitasking')
# class Child(Father,Mother):
#     def __init__(self):
#         print('i am a student')
#     def study(self):
#         print('can study')
        
# anu=Child()
# anu.multitasking()
# anu.study()
# anu.work()




#MULTILEVEL INHERITANCE


# class Grandfather:
#     def _init_(self):
#         print('i am grandfather')
    
#     def swim(self):
#         print('can swim ')

# class Father(Grandfather):
#     def _init_(self):
#         print('i am father')
#     def work(self):
#         print('can work')

# class Child(Father):
#     def _init_(self):
#         print('i am child')
#     def study(self):
#         print('study')

# anu=Child()
# anu.swim()
# anu.study()
# anu.work()


#..............................................................................................................................................

#HIERARCHIAL INHERITANCE


# class Father:
#     def _init_(self):
#         print('i am father')
#     def work(self):
#         print('can work')

# class Child1(Father):
#     def _init_(self):
#         print('i am child1')
#     def sing(self):
#         print('can sing')

# class Child2(Father):
#     def _init_(self):
#         print('i am child2')
#     def dance(self):
#         print('can dance')

# anu=Child1()
# anu.sing()
# anu.work()
# print('//////////////////////////////////////////////////////////////////////////////////////////////////')
# ammu=Child2()
# ammu.dance()
# ammu.work()



