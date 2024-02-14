# s='haii'
# print(s.endswith('i',0,2))
# print(s.startswith('i',0,2))


# i=10
# f=2.9876
# s='67'
# print(''' i am integer.. my value is %d \n 
#       i am float.. my value is %f \n 
#       i am integer.. my value is %s''' %(f,i,s))


                    # string formating


# print('{} is {}'.format('she', 'ayisha'))   
# print('{1} is {0}'.format('she', 'ayisha'))  
# print('{0} is {}'.format('she', 'ayisha'))                          #error     
# print('{} is {0}'.format('she', 'ayisha'))                                         #error
# print('{} is {}'.format('she', 'ayisha', 'my'))   
# print('{} is {} {}'.format('she', 'ayisha'))                                       #error

# print('{} is {name} {}'.format('she', name="ayisha"))   #error
# print('{} is {name} {email}'.format('she', name='ayisha', email='ayisha@gamil.com'))               #error
# print('{0} is {name} {email}'.format('she', name='ayisha', email='ayisha@gamil.com'))   
# print('{} is {name} '.format('she', name='ayisha', email='ayisha@gamil.com'))


# print('the site  is {0:f} securely {1}!!'. format(100, 'encryted'))
# print('my average of this {0} was {1:.2f}'. format('semster', 67.234))
# print('my average of this {0} was {1:.2f}'. format('semster', 67.2399))
# print('my average of this {0} was {1:.0f}'. format('semster', 67.234))                  #for convertingto digit 
# print('my average of this {0} was {1:.0f}'. format('semster', 67.834))                 #for convertingto digit 
# print('my average of this {0} was {1:d}'. format('semster', 67.234))                   #error digit cann't be writen
# print('my average of this {0} was {1:b}'. format('binary', 21))                        #printing binary number

# a=float(input('enter a number: '))
# print('{0:.2f}'.format(a))

                             #work 13


# a=input('enter a string: ')
# c=0
# for i in a[0:4]:
#     if i.isupper():
#         c+=1
# if c>=2:
#     print(a.upper())
# else:
#     print(a)


# a=input('enter a string: ')
# l=len(a)
# c=a[-2:]
# s=c*4
# if l>=4:
#     print(a+s)
# else:
#     print(a)   
    

















