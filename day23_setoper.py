# a={5,3,1,2,6}
# b={2,9,8,1,10}
# print('union = ',a|b)
# print('intersection = ',a&b)
# print('difference = ',a-b)
# print('symmetric difference = ',a^b)

#output

# union =  {1, 2, 3, 5, 6, 8, 9, 10}
# intersection =  {1, 2}
# difference =  {3, 5, 6}
# symmetric difference =  {3, 5, 6, 8, 9, 10}


#membership operator


# a={5,3,1,2,6}
# b={2,9,8,1,10}
# print(5 in a)
# print(12 in a)
# print(5 not in a)

#given an list of elemnets, remove the duplicate elements

# l=[1,2,3,2,4,5]
# print(l)
# c=set(l)
# print(c)

#read a string and find the number of unique character in string

                    # a=input('enter a string: ')
                    # c=set(a)
                    # print(c)
                    # print(len(c))


# a='hello'
# b=set(a)
# c=list(a)
# for i in b:
#     c.remove(i)
# d=set(c)
# print(len(b-d))


#give two set of numbers write a python program to find missing numbers in the second set as comparied to the first

# a={5,3,1,2,6}
# b={2,9,8,1,10}
# print(a-b)

#

# n={1,2,3,4,5,6,7,8,9,10}
# e={2,4,6,8,10}
# o={1,3,5,7,9}
# print(e.isdisjoint(o))            #true
# print(e.issubset(n))              #true
# print(n.issuperset(e))            #true
# print(e.issuperset(n))            #false







