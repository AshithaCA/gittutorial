                            #   NOTES


# print(2**3**2)            # python is right to left so first 3**2=6 then 2**6=512
# print(2*3**3*4)           # exponation have high proirty so frist 3**3=27 then 2*27*3=216
# print(6%12)               # smaller number will be the answer
# x=100
# y=50
# print(x and y)
# y=10
# x=y+=2                    # error in this line because of two '='
# print(x)

# a=[10,20]
# b=a              #same reference ahn so b change akubol a change akum
# b+=[30,40]
# print(a)         #[10, 20, 30, 40]
# print(b)         #[10, 20, 30, 40]

# a=[10,20]
# b=[30,40]
# print(a+b)         #[10, 20, 30, 40]

# print(-18//4) #o/p -5 
# in the case of floor div operator become -ve the reslt is arounded to be next smallest integer or big -ve integer

#title :all words in the sentence first letter capital
#capitalize : only first word
#upper : for all letters to capital

# str1=str('pynative')
# str2='pynative'
# print(str1==str2)            #True
# print(str1 is str2)          #True
# == : value check cheyum 
# is : memory location ahn check cheyunnath

#find character at an odd postion in string input by user

# a=input('enter a string: ')
# l=len(a)
# for i in range (0,l,2):
#     print(a[i])

#add item 7000 after 6000 in the following list 

# list1=[10,20,[300,400,[5000,6000],30,40]]
# list1[2][2].append(7000)                      #append last position varum
# print(list1)

#program to change brad salary to 8500 in the dictionary
 
# d1={'emp1':{'name':'john','salary':7500},'emp2':{'name':'emma','salary':8000},'emp3':{'name':'brad','salary':5000}}
# d1['emp3']['salary']=8500
# print(d1)

            #NOTES
            
            
# a=('ch',)
# n=2
# for i in range(int(n)):
#     a=(a,)              
#     print(a)
    
                #o/p
    
            #(('ch',),)
            #((('ch',),),)