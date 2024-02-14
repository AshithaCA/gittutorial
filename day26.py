# def feb(n):
#     if n<=1:
#         return n
#     else:
#         return feb(n-1)+feb(n-2)
# number=int(input('enter a number: '))
# if number<=0:
#     print('invalid')
# else:
#     for i in range(number):
#         print(feb(i))


# write a rescive function that accepts a number as it arugment and return the sum of digits


# def sum(num):
#     if (num<10):
#         return num
#     else:
#         return num%10 +sum(num//10)
# n=int(input('enter a number'))
# print(sum(n))


#calculate sum of first 10 natural number

# def sum(n):
#     if n==0:
#         return n
#     else:
#         return n + sum(n-1)
# num= int(input('enter a number: '))
# print(sum(num))


   
# user_data={}
# def register():
#     username=print('enter your username:')
#     password=print('enter your password: ')
#     user_data[username]=password
#     print('registration successful')
# def login():
#     username=print('enter your username:')
#     password=print('enter your password: ')
#     if username in user_data and user_data[username]==password:
#         print('login successful')
#     else:
#         print('invalid username or password')
# while True:
#     print('\nenter your choices: ')
#     print('1. Register  ')
#     print('2. Login ')
#     print('3. exit')
#     choice= input('enter your choice: ')
#     if choice==1:
#         register()
#     elif choice==2:
#         login()
#     elif choice==3:
#         print('exit')
#     else:
#         print('invalid choices')
        
        
        
# dict1={}
# def register():
#     name=input("enter ur name")
#     pwd=input("enter a password")
#     dict1[name]=pwd
#     print("registration successful")
# def login():
#     name=input("enter ur name")
#     pwd=input("enter a password")
#     if name in dict1 and dict1[name]==pwd:
#         print("log in successful")
#     else:
#         print("invalid username or password")    


# while(True):
#     ch=int(input('''enter ur choice
#             1.Register
#             2.log in
#             3.exit'''))
#     if ch==1:
#         register()
#     elif ch==2:
#         login()
#     elif ch==3:
#         break
#     else:
#         print("invalid entry1")
    





    

    