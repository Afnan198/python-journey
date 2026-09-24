a='Amar shonar Bangla ami tomay valobashi'
b='I love my country'
print(a)
print(a.title()) # python string is immutable. means cant modify main variable's value.
a=a.title()
print(a)
print(a)

print(b.upper())
print(a.lower(),',', b. lower())
c='i lOvE My MoThEr'
print(c.swapcase())
print(c.replace('MoThEr','Father').swapcase())

print(a.count('a'),a.count('b'))

print(len(a))



firstStr=input('Enter first string: ')
print(firstStr)
c=firstStr.upper()

print("Upper case of your string is: ",c)