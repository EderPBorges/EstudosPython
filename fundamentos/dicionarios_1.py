#!python3
pessoa = {'nome': 'Prof(a). Ana', 'idade': 38, 'cursos': ['Inglês', 'Portugues']}
print(type(pessoa))
print(len(pessoa))

print(pessoa['nome'])
print(pessoa['cursos'][0])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))
# print(pessoa.get('tags', [])) Retorna um valor default caso a proprierade não exista
