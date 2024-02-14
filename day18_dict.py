# a={}
# print(a)
# print()

# a={'name':'anu','phn':'123','place':'kolam'}
# print(a)
# print(type(a))                          #<class 'dict'>
# for i in a:
#     print(i)            #we get keys

# a={'name':'anu','phn':'123','place':'kolam'}
# print(a['name'])                #anu

                            #accessing items
                            
                            
thisdict={'brand':'ford','model':'mustang','year':1234}
# print(thisdict)

# x=thisdict['model1']
# print(x)        #key error model1 is not present

x=thisdict.get('model1','error')          #error is print
print(x)

# x=thisdict.get('model1')        #none
# print(x)

# for i in thisdict:
#     print(i)                          #key will be printed line by line

# for i in thisdict:
#     print(thisdict[i])                 #value will get line by line
    
# for i in thisdict:
#     print(i,thisdict[i])   

                            #output

                        # brand ford
                        # model mustang
                        # year 1234 

#......................................

# for x in thisdict.values():
#     print(x)   #we will get values 


    
                            # dictionary keyvalue pair
                            
                            

# for x, y in thisdict.items():
#     print(x,y)                     #get key and value

# print(len(thisdict))                  #number of items o/p: 3

# Q)  ..............................................................................


# name=input('enter name: ')
# place=input('enter the place: ')
# email=input('enter mail id: ')
# phno=int(input('enter ph number: '))

# a={'name':name, 'place':place, 'email':email, 'phno':phno}
# print(a)

# a={}
# name=input('enter name: ')
# place=input('enter the place: ')
# email=input('enter mail id: ')
# phno=int(input('enter ph number: '))

# a['name']=name
# a['place']=place
# a['email']=email
# a['phno']=phno

# print(a)


#...............................incorrect........................................

# n=int(input('enter a number from 1 to 5: '))
# if n>5:
#     print('invalid')
#     print(int(input('enter a number less than 5: ')))
#     a=int(input('enter a number: '))
#     b=int(input('enter a number: '))
#     print(n)
#     if n==1:
#         ADD=a+b
#         print(ADD)
#     elif n==2:
#         SUB=a-b
#         print(SUB)
#     elif n==3:
#         DIV=a/b
#         print(DIV)
#     elif n==4:
#         MULT=a*b
#         print(MULT)
# else:
    
#........................................................................................


# while True:
#     n=int(input('enter choice :'))
#     if n<5:
#         a=int(input('enter number1: '))
#         b=int(input('enter 2 number: '))
#         print('a: ',a)
#         print('b: ',b)
#         if n==1:
#             ADD=a+b
#             print(ADD)
#         elif n==2:
#             SUB=a-b
#             print(SUB)
#         elif n==3:
#             DIV=a/b
#             print(DIV)
#         elif n==4:
#             MULT=a*b
#             print(MULT)
#         elif n==5:
#             break
#     else:
#         print('invalid')




