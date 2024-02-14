                                    #string

# a='hai'
# b='hello'
# print(a+b)
# # print(a*3)
# a='python'
# print(type(a))
# print(len(a))
# print(a[3])
# print('y'in a)


                                # slicing
                               
# a='python'    
# print(a[1:5]) 
# print(a[1:5:2]) 
# print(a[:5]) 
# print(a[1:]) 
# print(a[:-3]) 
# print(a[-1:-5:-1]) 
#   print(a[1:5:-1])
# print(a[::])  
# print(a[0:])       
# print(a[0:3])      


                                                                                                                                       
# var='mY Name iS ashiTHa'
# print(var)
# print(var.capitalize())
# print(var.lower())
# print(var.upper())  
# print(var.title())
# print(var.swapcase()) 


                                        #string comparison function


# var='a'
# print(var)
# print(var.islower())
# print(var.isupper())
# print(var.isalpha())
# print(var.isnumeric())
# print(var.isalnum())


                                    #work


# S1='abcde'
# S2='uvwxyz'  

# s=S1[0]+S2[0]    
# l=S1[-1]+S2[-1] 
# m=S1[len(S1)//2]+S2[len(S2)//2] 
# print(s+m+l)                                                                                                                                     


#2 question


# a="P@#ym26at^&i5ve"
# c=0
# l=0
# d=0
# u=0
# s=0
# for i in a:
#     if i.isalpha():
#         c+=1
#         if i.isupper():
#             u+=1
#         else:
#             l+=1
#     elif i.isnumeric():
#         d+=1
#     else:
#         s+=1
# print("spcl: ",s)
# print("dig: ",d)
# print("upper: ",u)
# print("lower: ",l)
# print("char: ",c)

                    #3 question same length
                    
# a='abc'
# b='xyz'
# b=b[::-1]
# l=len(a)
# s=''
# for i in range(l):
#     s+=a[i]
#     s+=b[i]
# print(s)


                    #3 question different length


# a='abcde'
# b='mno' 
# b=b[::-1]
# la=len(a) 
# lb=len(b)
# if la<lb:
#     l=lb 
# else:
#     l=la
# s="" 
# for i in range(l):
#     if i<la:
#         s+=a[i]
#     if i<lb:
#         s+=b[i]
# print(s)
   
   
# a='abc'
# b='mnopq'
# b=b[::-1]
# la=len(a)
# lb=len(b)

            