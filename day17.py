# a=[1,5,2,8,3,6,9,0]
# a=[1,5,2,8,3,6,9,'aa']   #error string it not support only numeric values
# print(sum(a))           #sum of all numbers



# a=[1,5,2,8,3,6,9,0]         #sort
# a.sort()
# print(a)

# a=[1,5,2,8,3,6,9,0]             #reverse
# a.reverse()
# print(a)

                        #descending  order

# a=[1,5,2,8,3,6,9,0] 
# a.sort()
# # print(a)
# a.reverse()
# print(a)    

# a='get'                       #with for loop
# b='set'
# for i in a:
#     for j in b:
#         print(i,j)

# a='get'                         #without for loop
# b='set'
# m=[i+j for i in a for j in b]                        #['gs', 'ge', 'gt', 'es', 'ee', 'et', 'ts', 'te', 'tt'] we get it as a list
# print(m)  

                                # get even numbers            

# s=[12,3,5,13,54,10]                   #[12, 54, 10]
# a=[]
# for i in s:
#     if i%2==0:
#         a.append(i) 
# print(a) 

# s=[12,3,5,13,54,10]  
# a=[i for i in s if i%2==0]                  #if their is only 'if'  if will  be placed after for loop
# print(a)               

                                    #for even and odd numbers
                                #if ther is 'elif' if and elif condition should be placed before for loop

# s=[12,3,5,13,54,10]
# a=['e'if i%2==0 else 'o' for i in s]
# print(s)                                                    #[12, 3, 5, 13, 54, 10]
# print(a)                                                    #['e', 'o', 'o', 'o', 'e', 'e']




                    #Q2
                    
                    
# list1=['m','na','i','ke']
# list2=['y','me','s','lly']
# a=[i+j for i in list1 for j in list2]
# print(a)

# list1=['hello','take']
# list2=['dear','sir']
# a=[i+j for i in list1 for j in list2]
# print(a)
 
list1=['m','na','i','ke']
list2=['y','me','s','lly'] 
for i in list1:
    for j in list2:
        print(i+j)
                          