# a=[12,12.32,True,'hai']
# a[2]='b'
# print(a)
# for i in a:
#     print(i)
# b=[1,2,34]
# print(a+b)
# print(a*2)
# print(a**2)                                     #error list and int can't support operand


a=[1,2,3,4,1,2]
# print(a.count(1))
# print(a.count(1,5))                             #error count only one variable
# print(len(a))
print(a[::-1])



# a='welcome'
# print(a.count('e',3))                           #for string there is 3 variables
# l1=[1,2,3]
# l2=[2,3,4]
# print(l1*l2)                                   #error


                              #append,update,insert
                    

a=['anu','ammu','sana','manu']
# a[2]='sana abu'                                #update
# print(a)

# a.append('veena')                              #append added to the end of the list
# print(a)

# a.insert(3,'abu')
# print(a)

# a.insert(7,'abu')
# print(a)
# print(a[7])                                   #error
# print(a[4])                                   #we get abu 

 
 

# l=[]
# for i in range(10):
#     a=input('enter element: ')                    #using append
#     l.append(a)
# print(l)
  
  
# l=[]
# for i in range(10):
#     a=input('enter element: ')                        #using insert
#     l.insert(i,a)
# print(l)

                                                #reverse a list without inbuilt methond
                                                
                                                
                                                
# l=[]
# r=[]
# n=int(input('enter the limit: '))
# for i in range(n):
#     a=input('enter element: ')
#     l.append(a)
# for i in l:
#     r=[i]+r
# print(r)

                    #or
                    
# a=[1,2,3,4,5]
# l=len(a)
# r=[]
# for i in range(l-1,-1,-1): 
#     r.append(a[i])
# print(r)    

                #sum of element in a list
                
                
# a=[1,2,3,4]
# s=0
# for i in a:
#     s+=i
# print(s)    

#or

# a=[1,2,3,4]
# print(sum(a))


                    #sum of element of two list

# a=[1,2,3,4]
# b=[5,6,7,8]
# c=[]
# if len(a)==len(b):
#     for i in a:
#         a[i]
#     for j in b:
        
#         c=a[i]+b[j]
# print(c)
        
        
                           
                            # minimum number
# a=[22,33,1,23]
# m=a[0]
# for i in a:
#     if m>i:
#         m=i
# print(m)
