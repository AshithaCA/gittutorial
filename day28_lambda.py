# x=lambda a:10+2
# print(x)  #address of x 
# print(x(1)) #o/p 12

# x=lambda a:12+a
# print(x(8))                       #8 will be pass to the a and o/p 20

# x1=lambda a:v=4*a
# print(x1(2))                      # cannot assign lambda #o/p ERROR

# x2=lambda a,b,c: print(c)         #1
# print(x2(3,2,1))                  #none because expression is print c 

# x2=lambda a,b,c: print(a+b)       #5
# print(x2(3,2,1))                  #none because expression is print c 

# x2=lambda a,b,c: a+b       
# print(x2(3,2,1))                  #5 because a+b is assign to x2

# def myfun(n):
#     return lambda a:a*n           #n=2 , a=9
# d=myfun(2)              
# print(d(9))                       #o/p 18


# f=myfun(3)
# print(f(10))         #o/p  30   #oru function ullil thanne randum work cheyth o/p print cheyum

#..............lambda built in functions..............................
# 1)filter

# li=[3,12,7,12,36,87,100,77]
# odd_list=list(filter(lambda x: (x%2!=0),li))
# print(odd_list)                          #[3, 7, 87, 77]


# 2)map

# li=[3,12,7,12,36,87,100,77]
# new_list=list(map(lambda x:x*2,li))
# print(new_list)                          #[6, 24, 14, 24, 72, 174, 200, 154]   #2 is mult to all the numbers in the list

# 3)reduce

# from functools import reduce

# li=[3,12,7,12,36,87,100,77]
# sum=reduce((lambda x,y: x+y),li)
# print(sum)                               #334    #  3+12+7+.....+77  

# funct=(lambda x:(x+3)*(5/2))
# print(funct(3))    #15.0