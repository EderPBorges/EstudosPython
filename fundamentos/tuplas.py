#!python3

tupla = tuple()
tupla = ()
print(type(tupla))
# print(dir(tupla))
# print(help(tuple))
tupla = ('um', )
print(tupla[0])
# tupla[0] = 'novo' não é possivel alterar um elemento de uma tupla
cores = ('verde', 'amarelo', 'azul', 'branco')
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index('amarelo'))
print(cores.count('azul'))
print(len(cores))