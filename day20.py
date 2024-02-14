                        #sort

# prices={'Appple':1.99,'Banana': 0.99,'Orange':1.49,'Cantaloup':3.99,'Grapes':0.39}
# print(prices)                                             #{'Appple': 1.99, 'Banana': 0.99, 'orange': 1.49, 'cantaloup': 3.99, 'Grapes': 0.39} ..... here item as dictinory
# print(sorted(prices))                                     #['Appple', 'Banana', 'Cantaloup', 'Grapes', 'Orange']
# print(sorted(prices.values()))                            #[0.39, 0.99, 1.49, 1.99, 3.99]
# print(sorted(prices.keys()))                              #['Appple', 'Banana', 'Cantaloup', 'Grapes', 'Orange']
# print(sorted(prices.items()))                             #[('Appple', 1.99), ('Banana', 0.99), ('Cantaloup', 3.99), ('Grapes', 0.39), ('Orange', 1.49)] ....... here items as list
# print(sorted(prices.values(),reverse=True))               #[3.99, 1.99, 1.49, 0.99, 0.39] ..... reverse orderr              


# a=[1,2,3,4,5]
# b=[100,200,300,400,500]
# c={}
# for i in range (5):
#     c[a[i]]=b[i]
# print(c)                            #{1: 100, 2: 200, 3: 300, 4: 400, 5: 500}
  
#........................  Q*0...........................


# a=int(input('enetr a number: '))
# b={}
# for i in range(1,a+1):                #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#     b[i]=i*i
# print(b)

#.......................Q*1....................................

# d={'a':1,'b':2,'c':3}
# v=d.pop('b')
# print(d) 
# print(v) 

#..........................   PHONE BOOK   .................................
ph={}

while True:
    choice=int(input('''enter your choice: 
                       1...add
                       2....view
                       3....update
                       4....delete
                       5....exit : '''))
    if choice==1:
        sub={}
        name=input('enter your name: ')
        email=input('enter mail id: ')
        phno=int(input('enter ph number: '))
        sub['name']=name
        sub['email']=email
        sub['phno']=phno
        ph[name]=sub
    elif choice==2:
        print(ph)
    elif choice==3:
        name=input('enter name : ') 
        n=input('''enter the choice need to be updated: 
                 a.....name
                 b....email
                 c....phno''')
        if n=='a':
            newname=input('enter the updated name: ') 
            ph[name]['name']=newname
            nn=ph.pop(name)
            ph[newname]=nn
        elif n=='b':
            newemail=input('enter the updated email: ')
            ph[name]['email']=newemail
        elif n=='c':
            newphno=input('enter the updated phno: ')
            ph[name]['phno']=newphno
    elif choice==4:
        name=input('enter the name to be deleted: ')
        if name in ph:
            del ph[name]
    elif choice==5:
        break
        
    



    

    

   
    
    
