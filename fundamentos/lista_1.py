#!python3
lista = []
print(len(lista))
print(lista)
lista.append(1)
lista.append(5)
# lista.append([1, 2, 3]) tambêm é possivel adicionar novas listas 
print(lista)
print(len(lista))

nova_lista = [1, 5, 'Ana', 'Bia'] #MUITO CUIDADO com o uso de LISTAS HETEROGENEAS
print(nova_lista)
nova_lista.remove(5)
print(nova_lista)
nova_lista.reverse()
print(nova_lista)

print(lista)