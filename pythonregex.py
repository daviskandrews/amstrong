import re
#square brackets [] specify a set of charecters which we wish to match
s="abc"
re.search('[abc]',s)

#period . matches any single chareccter except '\n'
s="bchkj"
re.search('.',s)

#caret ^ used to check if a string starts with a certain charecter
s="mumbai"
x=re.search('^m',s)
print(x)

#dollar $ used to check if a string ends with a certain charecter
a=re.search('a$','Delhi')
print(a)
b=re.search('a$','Orissa')
print(b)

#star * matches zero or more occurences of the pattern left to it
a=re.search('ma*','man')
print(a)
b=re.search('ma*','woman')
print(b)

#plus + matches one or more occurences of the pattern left to it
a=re.search('ma+','man')
print(a)
b=re.search('ma+','woman')
print(b)

#braces {} matches exact specified number of occurences of the pattern left to it
a=re.search('a{2}','abc') 
print(a)
b=re.search('a{2}','aabc')
print(b)

#vertical bar | either or
a=re.search('a|b','mango') 
print(a)
b=re.search('a|b','pune')
print(b)

#paranthesis () group sub patterns
a=re.search('(a)m','amm') 
print(a)
b=re.search('(a)m','abm')
print(b)

#backslash \ escape various characters including metacharacters
a=re.search('\$a','$abc') 
print(a)

