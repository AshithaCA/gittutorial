# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in a:
#     print(i)

# for i in a:
#     # print(i)
#     for j in i:
#         print(j,end=' ')
#         print()

# for i in range(3):
#     # print(a[i])
#     for j in range(3):
#         print(a[i][j],end=' ')
#     print()


# a=[]
# row=3
# for i in range(row):
#     b=[]
#     for j in range(row):
#         n=int(input('enter element: '))
#         b.append(n)
#         print(b)                     #upto here we get separate list in the matrix b[] [1, 2, 3] [4, 5, 6] [7, 8, 9]
#     a.append(b)                         # in here the list we get will be append to the null list a[] [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     print(a)
        

a=[]
b=[]
row=3
for i in range(row):
    for j in range(row):
        n=int(input('enter element: '))
        b.append(n)
        print(b)                     
    a.append(b)                         
    print(a)



