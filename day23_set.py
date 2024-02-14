# a={}
# print(a)
# print(type(a)) #<class 'dict'>

# a={1,2}
# print(a)
# print(type(a)) #<class 'set'>

# a={2,1,2,3,8,4,6,7}
# print(a) #{1, 2, 3, 4, 6, 7, 8} unordered and repetation ella

# mutable elements mathram add akollu immutable elements add akulla
# a={2,5,44,11,3,88,2,44,(1,2)}
# print(a)   #{2, (1, 2), 3, 5, 88, 11, 44}

# a={1:100,2:300,3:200,1:900}
# print(a)               #{1: 900, 2: 300, 3: 200}
# c=set(a)
# print(c)               #{1, 2, 3} #only keys

# a={1,2,3,1,'haiii'}
# c=set(a)
# print(c)               #{1, 2, 3, 'haiii'}

# a={1:100,2:300,3:200,1:900}
# n=a.values()
# m=set(n)
# print(m)        #{200, 900, 300} values get without repetation

# a={1:100,2:300,3:200,1:900}
# n=a.items()
# m=set(n)
# print(m)            #{(1, 900), (3, 200), (2, 300)}


#2methods for adding

# a={11,33}
# print(a)
# a.update([55,33])
# print(a)    #{33, 11, 55} 


# a={11,33}
# print(a)
# a.add([55,33])
# print(a)           #list not work in add

# a={11,33}
# a.update('python')
# print(a)            #{33, 'y', 'h', 11, 'p', 't', 'n', 'o'}

# a={11,33}
# a.add('python')
# print(a)         #{'python', 33, 11}

# a={11,33}
# a.update((1,2,2)) 
# print(a)             #{33, 2, 11, 1}

# a={11,33}
# a.add((1,2,2))
# print(a)              #{33, (1, 2, 2), 11}

# a={11,33}
# a.update(1.33)
# print(a)              #not iterable

# a={11,33}
# a.add(1.33)
# print(a)        #{33, 11, 1.33}


# a={11,33}
# a.update(('hai','welcome'))
# print(a)               #{'welcome', 33, 11, 'hai'}

# a={11,33}
# a.add(('hai','welcome'))
# print(a)            #{33, ('hai', 'welcome'), 11}

# remove: error #element is not present
# discard: no error element print akum

# a={1,8,2,4,7,5,9}
# a.remove(8)
# print(a)        #{1, 2, 4, 5, 7, 9}

# a={1,8,2,4,7,5,9}
# a.remove(11)
# print(a)             #error

# a={1,8,2,4,7,5,9}
# a.discard(8)
# print(a)             #{1, 2, 4, 5, 7, 9}

# a={1,8,2,4,7,5,9}
# a.discard(11)
# print(a)             #{1, 2, 4, 5, 7, 8, 9}




