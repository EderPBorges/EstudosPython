#!python3
a = 'valor' #true
a = 0 #false
a = -0.00001 #true
a = '' #false
a = ' ' #true
a = [] #false
a = {} #false

if a:
    print('Existe!!!')
else:
    print('não existe ou zero ou vazio...')