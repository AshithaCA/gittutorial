                            #pop (return and remove)


thisdict={'brand':'ford','model':'mustang','year':1934}
# v=thisdict.pop('model')
# print(thisdict)                                 #{'brand': 'ford', 'year': 1934}
# print(v)                                        #mustang



# v=thisdict.pop()                                #error
# print(thisdict)


v=thisdict.popitem()
# print(thisdict)                   #{'brand': 'ford', 'model': 'mustang'}
print(v)                          #('year', 1234)

                            #delete

# del thisdict['model']
# print(thisdict)                     #{'brand': 'ford', 'year': 1934}


                            #clear
                            
# thisdict.clear()
# print(thisdict)                     #{}

#...............................dictionary and subdictinary problem..................................

# while True:
#     n=int(input('enter a choice: '))
#     name=input('enter name: ')
#     place=input('enter the place: ')
#     email=input('enter mail id: ')
#     phno=int(input('enter ph number: '))
#     name={'name':input('enter name: '),'email':input('enter mail id: '),'phno':int(input('enter ph number: '))}
    
#     if n<5:
#         if n==1:
#             print(name)
#         elif n==2:
#             for i in name:
#                 print(name[i]) 
#         elif n==3:
            


# print(name)


