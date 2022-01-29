#!python3

lista_1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista_1)
print(list(dobro))

lista_2 = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26}
]

so_nomes = map(lambda p: p['nome'], lista_2)
so_idades = map(lambda i: i['idade'], lista_2)

print(list(so_nomes))
print(sum(so_idades))

# Desafio: usando map retorne frase '<Nome> tem <idade> anos.'
desafio_retorno = map(lambda p: f'{p["nome"]} tem {p["idade"]} anos.', lista_2)
print(list(desafio_retorno))
