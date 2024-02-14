# exceptional handling

# try:
#     x='asla'
#     a=[1,2,4]
#     print(x)
#     print(a[6])
# except NameError:
#     print('name error')
# except IndexError:
#     print('index erroe')
# else:
#     print('correct')
# finally:
#     print('completed')

# x=-21
# if x<0:
#     raise Exception('soory, number below zero') #Exception: soory, number below zero

# x='6'
# if not type(x) is int:
#     raise IndexError('only integer are allowed') #IndexError: only integer are allowed

# x=4/0
# print(x) #ZeroDivisionError: division by zero

class Lessthan10(Exception):
    def __str__(self):
        return 'enter number greater than 10'
try: 
    a=5/0
    a=int(input('enter number greater than 10:'))
    if a<10:
        raise Lessthan10()
    


    
    