#!python3

a = '123'
b = ' de Oliveira 4'
print(a + b)
print(a.__add__(b)) # <- na pratica NÃO é usado
print(str.__add__(a, b))
# a.__len__() == len(a)
# '1' in a == a.__contains__('1')
