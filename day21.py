# .......................incorrect........................................
# ph={}

# while True:
#     choice=int(input('''enter your choice: 
#                        1...add
#                        2....view
#                        3....update
#                        4....delete
#                        5....exit : '''))
#     if choice==1:
#         sub={}
#         subb={}
#         name=input('enter your name: ')
#         email=input('enter mail id: ')
#         phno=int(input('enter ph number: '))
#         n=input('alternative phone number if any  yes/no: ')
#         if n=='yes':
#             altphno=int(input('enter alternative ph number: '))
#         sub['name']=name
#         sub['email']=email
#         sub['phno']=phno
#         ph[name]=sub
    
        
        
        
#     elif choice==2:
#         print(ph)
#     elif choice==3:
#         name=input('enter name : ') 
#         n=input('''enter the choice need to be updated: 
#                  a.....name
#                  b....email
#                  c....phno''')
#         if n=='a':
#             newname=input('enter the updated name: ') 
#             ph[name]['name']=newname
#             nn=ph.pop(name)
#             ph[newname]=nn
#         elif n=='b':
#             newemail=input('enter the updated email: ')
#             ph[name]['email']=newemail
#         elif n=='c':
#             newphno=input('enter the updated phno: ')
#             ph[name]['phno']=newphno
#     elif choice==4:
#         name=input('enter the name to be deleted: ')
#         if name in ph:
#             del ph[name]
#     elif choice==5:
#         break
    
    
#................................................................
    
# a='malayalam'
# for i in a:
#     c=0
#     for j in a:
#         if i==j:
#             c+=1
#     if c==1:
#         print(i)


#...................................................................
# l=[]
# avg=0
# n=int(input('enter how many numbers:  '))  
# for i in range(n):
#     a=int(input('enter the numbers: '))
#     if a==0:
#         break
#     else:
#         if a%2==0:
#             if a not in l:
#                 l.append(a)
# if len(l)>0:
#     print(l)
#     c=(len(l))
#     avg=sum(l)/c
#     print(avg)

#.python program to combine 2 dictionary by adding values for common keys.....................................

# a={'anu':'manu','age':12,'place':'elm'}  
# b={'anu':'kiran','age':23,'place':'klm','phn':234} 
# c={}

# for i in a:
#     for j in b:
#         if i==j:
#             c[i]=a[i]+b[j]
#         if j not in c:
#             c[j]=b[j]
#     if i not in c:
#         c[i]=a[i]
# print(c)


#..................................................

# a='recover'
# l=[]
# M=[]
# d={}
# b=a
# for i in a:
#     c=0
#     for j in b:
#             if i==j:
#                 c+=1
#     l.append(c)        
# print(l)
# for i in a:
#     print(i)
#     M.append(a)
# print(M)
    
#.......................................................

# a=input('enter a string: ')
# d={}
# for i in a:
#     if i in d:
#         n=d[i]
#         d[i]=n+1
#     else:
#         d[i]=1
# print(d)


 
 
       


    

     

    
 
 
 
 
 
 


    

        
        