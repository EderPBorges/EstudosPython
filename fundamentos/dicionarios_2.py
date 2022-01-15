#!python3
pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
print(pessoa)
pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
print(pessoa)

# pessoa.pop('idade') Retorna o valor idade mas o retira da variavel
print(pessoa)

pessoa.update({'idade': 40, 'Sexo': 'M'})
print(pessoa)

del pessoa['cursos']
print(pessoa)

pessoa.clear() #apaga toda a estrutura
print(pessoa)