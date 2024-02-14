# l1=[1,2,3,4]
# l2=[7,8,9,10]
# l1.append(l2)                                     #o/p [1, 2, 3, 4, [7, 8, 9, 10]] 
# l1.extend(l2)                                     #o/p  [1, 2, 3, 4, 7, 8, 9, 10]
# print(l1)
# l1.append('hai')                                  #o/p [1, 2, 3, 4, 'hai']
# l1.extend('hai')                                    #o/p      [1, 2, 3, 4, 'h', 'a', 'i']
# l1.extend(123)                                      #o/p 123 is not iterable
# print(l1)

                            #del : index based
                            
vowels=['a','e','i','o','u']
# del vowels[1]                                  #['a', 'i', 'o', 'u']
# del vowels
# del vowels[0:2]                                #['i', 'o', 'u']
# print(vowels)


                        #remove : element based

# a=[1,2,3,4,5]
# a.remove(2)                             #[1, 3, 4, 5]
# print(a)
# a=[1,2,3,4,5,3,4,5]   
# a.remove(3)                              #[1, 2, 4, 5, 3, 4, 5]    only frist '3' is removed 
# print(a)


                        #pop : index based
                        
# a=['a','b','c','d','e','f','a','c'] 
# a.pop()                                             #  ['a', 'b', 'c', 'd', 'e', 'f', 'a'] last  index element deleted
# a.pop(3)                                          #['a', 'b', 'c', 'e', 'f', 'a', 'c'] 3rd index is removed
# a.pop(20)                                      #error out of range
# print(a) 


                            #clear : to delete full list


# a=['a','b','c','d','e','f','a','c']
# a.clear()                                          # [] null list
# print(a)


# a=['a','b','c','d','e','f','a','c'] 
# a[0:4]=[]                                           #['e', 'f', 'a', 'c']
# print(a)



                                #print given numbers into words  


# l1=['zero','one','two','three','four','five','six','seven','eight','nine'] 
# l2=['ten','eleven','tweleve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']  
# l3=['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']  
# n=int(input('enter any number: '))
# if n<10:
#     i=l1[n] 
#     print(i) 
# elif n<20 and n>=10:
#     i=l2[n-10]
#     print(i)
# elif n>=20 and n<100:
#     if n%10==0:
#         print(l3[n//10])
#     else:
#         a=n//10
#         b=n%10
#         print(l3[a]+l1[b])


# l1=['zero','one','two','three','four','five','six','seven','eight','nine'] 
# l2=['ten','eleven','tweleve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']  
# l3=['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']  
# n=int(input('enter any number: '))
# if n<10:
#     i=l1[n] 
#     print(i) 
# elif n<20 and n>=10:
#     i=l2[n-10]
#     print(i)
# elif n>=20 and n<100:
#     if n%10==0:
#         print(l3[n//10])
#     else:
#         a=n//10
#         b=n%10
#         print(l3[a]+l1[b])
# elif n>100 and n<1000:
#     if n%100==0:
#         print(l1+)
    
    