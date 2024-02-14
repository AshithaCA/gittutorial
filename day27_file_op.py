# f=open('anu.txt','r')  #error anu file isn't exist
# f=open('ancy.txt','w')
# f.write('my name is ashitha')
# f.write('\ni am from klm')
# f.write(',ernakulam')
# f.close()
# f.write('hi')   #ValueError: I/O operation on closed file. file closs ahn


# f=open('C:\Users\ASHITHA\Desktop\MAIN PROJECT\minha','w')  #r frontil vakanam allakil error
# f=open(r'C:\Users\ASHITHA\Desktop\MAIN PROJECT\minha','w')
# f.write('ashitha')
# f.write('\n123455')
# f.write('\nashkar')
# # print(f)   #adresss of file
# f=open(r'C:\Users\ASHITHA\Desktop\MAIN PROJECT\minha','r')
# # for n in f:
# #     print(n)   #file print with space
# print(f.read())  #file print without space
# f.close()

# f=open('anu.txt','a')
# f.write('hello manha')  #non exist file ahnakil new file undaki write cheyum
# f.close()

# f=open('ancy.txt','a')
# f.write('hello manha')    #exist file ahnakil aa fileil addon cheyth varum
# f.close()
   
   
#with

# # with open('ab.txt','w') as f:
#     # f.write('hy anjana')
# with open('ab.txt','r') as f:
#     print(f.read())
    
# f=open('anu.txt','r')  #error anu file isn't exist
# f=open('ancy.txt','w')
# f.write('my name is ashitha')
# f.write('\ni am from klm')
# f.write(',ernakulam')
# f.close()

# with open('ancy.txt','r') as f:
#     data=f.read()
#     print(data)

 #o/p           # my name is ashitha
            # i am from klm,ernakulam

# with open('ancy.txt','r') as f:
#     data=f.readlines()
#     # print(data)             #['my name is ashitha\n', 'i am from klm,ernakulam']
#     # print('-----------------------------------')
#     # print(data[1:4])            #i am from muthal varum
#     # print('-----------------------------------')
#     for line in data:
#         word=line.split('\n')
#         print(word)

# ['my name is ashitha', '']
# ['i am from klm,ernakulam']


# with open('ancy.txt','r') as f:
#     data=f.readlines()
# for line in data:
#         word=line.split()
#         print(word)
        
        
# ['my', 'name', 'is', 'ashitha']
# ['i', 'am', 'from', 'klm,ernakulam']


#work 10/10/23

#1)
# def count_words():
#     count = 0
#     f=open("asho.txt","r")
#     data=f.read()
#     lines = data.split()
#     for word in lines:
#         count += 1
#     print("Total no of words :",count)
#     f.close()
# count_words()

#2)

# def display_words():
#     c=0
#     f=open("asho.txt","r")
#     data=f.read()
#     words = data.split()
#     for i in words:
#         if len(i)<4:
#             print(i)
#     f.close()
# display_words()