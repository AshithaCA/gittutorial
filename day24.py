#functions


# l=[]
# n=int(input('enter the number of items: '))
# for i in range(n):
#     pro=int(input('enter the amount of items: '))
#     l.append(pro)
# print(l)
# def total(*a):
#     print(a)
#     s=0
#     for i in a:
#         for j in i:
#             s+=j
#     print(s)
# total(l)

#.........................

# def det(**name):
#     print(name)
# det(name='ash',place='klm')

# def sum(s1,s2,s3):
#     s=s1+s2+s3
#     return s
# def avg(s,n):
#     a=s/n
#     print('avg',a)
# b=sum(2,3,4)
# print(b)
# avg(b,3)


#.............................Qns)


#1) define a function that accpet lowercase words and return uppercase words
    
# l=[]
# sent=input('enter a sentence: ')
# def upper(*a):
#     print(a)
# for i in sent:
#     if i.islower():
#         print(i)
#         l.append(i)
# print(l)
# for i in l:
#     print(i)
# print(l.isupper())

                        # n='fizzbuzz'
                        # for i in range(0,n+1):
                        #     if n % 3 == 0 and n % 5 == 0:
                        #         print("fizzbuzz")
                        #     elif n % 3 == 0:
                        #         print("fizz")
                        #     elif n % 5 == 0:
                        #         print("buzz")
                        #     print(n)

#2) function that accpet radius and return area of a circle

# def area(r):
#     area=3.14*r*r
#     return area
# r=int(input('enter the radius: '))
# print(area(r))

#3) define a function that return factorial of a number

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input('enter a number: '))
# print(fact(n)) 

#4) which counts vowels and constants in a word 

c=0
d=0
v='aeiouAEIOU'
def count(n):
    for i in a:
        for j in v:
            if i==j:
                c+=1
            else:
                d+=1
    # print('vowels: ',c) 
  
    
a=input('enter a string: ') 
b=len(a)
print(count(c))
print(count(d))
  

#5) even or odd 

# def number(n):
#     if n%2==0:
#         return print('even')  
#     else:
#         return print('odd') 
# n=int(input('enter a number: ')) 
# number(n)      
    


