# a=10
# b=2
# c=3
# if a>b and a>c:
#     print('a is larger :',a)
# elif b>a and b>c:
#     print('b is larger :',b)
# else:
#     print('c is larger :',c)


# a=int(input('enter starting no: '))
# b=int(input('enter stop no: '))
# sum=0
# while a<=b:
#     sum=sum+a
#     a+=1
# print('sum is:',sum)
    
a=int(input('enter your number: ')) 
no=0
while a>0:
    a=a//10
    no+=1 
print('no of digit: ',no) 
    