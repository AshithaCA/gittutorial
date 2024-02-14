#REGULAR EXPRESSION


import re   #importing module regular expression

#findall()

# txt='my name is amina'
# x=re.findall('am',txt)
# print(x)                            #['am', 'am']

# x=re.findall('ai',txt)
# print(x)                            #[]

#search()

# txt='my name is amina'
# x=re.search('am',txt)
# print(x)                               #<re.Match object; span=(4, 6), match='am'>    4th and 5th position ahnn am ullath last index excluded ahn  oru match mattaram ahn tharollu
# print('start with: ',x.start())               #start with:  4

# x=re.search('ai',txt)
# print(x)                                       #none

# txt='my Name iS Amina'        
# x=re.findall('[a-z]',txt)
# print(x)                                        #['m', 'y', 'a', 'm', 'e', 'i', 'm', 'i', 'n', 'a']
# x=re.findall('[A-Z]',txt)
# print(x)                                        #['N', 'S', 'A']
# x=re.findall('[a-zA-Z]',txt)
# print(x)                              #['m', 'y', 'N', 'a', 'm', 'e', 'i', 'S', 'A', 'm', 'i', 'n', 'a']


# txt='my N1ame i5S A3min9a'
# x=re.findall('[1-5]',txt)
# print(x)                           #['1', '5', '3']


#subsitution or repalce(sub())

# txt='my Name iS Amina'
# x=re.sub('\s','10',txt) 
# print(x)                           #my10Name10iS10Amina
# x=re.sub('\s','10',txt,2) 
# print(x)                           #my10Name10iS Amina

# txt='m2y 1Nam9e iS A3mina'
# x=re.findall('[0123]',txt)
# print(x)                          #['2', '1', '3']
# x=re.findall('[mi]',txt)
# print(x)                          #['m', 'm', 'i', 'm', 'i']

# txt='my Name iS Amina'
# x=re.findall('^my',txt)
# print(x)                               #['my']
# x=re.findall('^Na',txt)
# print(x)                                       #[]

# txt='my Name iS Amina'
# x=re.findall('a$',txt)
# print(x)                                    #['a']  ahnnakil a return tharum
# x=re.findall('n$',txt)
# print(x)                                    #[] null


# txt='my Name iS Amina'
# x=re.findall('[^am]',txt)
# print(x)                            #['y', ' ', 'N', 'e', ' ', 'i', 'S', ' ', 'A', 'i', 'n']

# txt='The Sain in Span'
# x=re.search(r'\bS\w+',txt)
# print(x)                           #<re.Match object; span=(4, 8), match='Sain'>
# print(x.span())                 #(4, 8)

# txt='The Sa_in in Span'
# x=re.search(r'\bS\w+',txt)
# print(x)                           #<re.Match object; span=(4, 9), match='Sa_in'>
# print(x.span())                    #(4, 9)

# txt='The Sa_ in in Span'
# x=re.search(r'\bS\w+',txt)
# print(x)                       #<re.Match object; span=(4, 7), match='Sa_'>                
# print(x.span())                #(4, 7)

# txt='The Sa#in in Span'
# x=re.search(r'\bS\w+',txt)
# print(x)                      #<re.Match object; span=(4, 6), match='Sa'>         
# print(x.span())                #(4, 6)

# txt='The Sain in Span'
# x=re.search(r'\bS\w+',txt)
# print(x)                                    #<re.Match object; span=(4, 8), match='Sain'>
# print(x.start())                            #4                  
# print(x.span())                             #(4, 8)
# print(x.string)                             #The Sain in Span
# print(x.group())                            #Sain

# txt= 'the rain in spain falls mainly in plain'
# x=re.findall('al{2}',txt)
# print(x)                           #['all']
# x=re.findall('ai{1}',txt)
# print(x)                         #['ai', 'ai', 'ai', 'ai']

# txt= 't$he rAin i4n spa#in Fall7s ma_inly'
# x=re.findall('\At',txt)  ['t']
# print(x)           #['t']

# x=re.findall('\d',txt)
# print(x)           #['4', '7']

# x=re.findall('\D',txt)
# print(x)           #['t', '$', 'h', 'e', ' ', 'r', 'A', 'i', 'n', ' ', 'i', 'n', ' ', 's', 'p', 'a', '#', 'i', 'n', ' ', 'F', 'a', 'l', 'l', 's', 
#' ', 'm', 'a', '_', 'i', 'n', 'l', 'y']

# x=re.findall('\s',txt)
# print(x)          #[' ', ' ', ' ', ' ', ' ']

# x=re.findall('\S',txt)
# print(x)          #['t', '$', 'h', 'e', 'r', 'A', 'i', 'n', 'i', '4', 'n', 's', 'p', 'a', '#', 'i', 'n', 'F', 'a', 'l', 'l', '7', 's', 'm', 'a', '_', 'i', 'n', 'l', 'y']

# x=re.findall('\w',txt)
# print(x)           #['t', 'h', 'e', 'r', 'A', 'i', 'n', 'i', '4', 'n', 's', 'p', 'a', 'i', 'n', 'F', 'a', 'l', 'l', '7', 's', 'm', 'a', '_', 'i', 'n', 'l', 'y']

# x=re.findall('\W',txt)
# print(x)           #['$', ' ', ' ', ' ', '#', ' ', ' ']

# x=re.findall('ly\Z',txt)
# print(x)             #['ly']

