#!python3
compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14}
)
# a = (1, 2, 3)
# tuple(map(lambda i: i ** 2, a))
# Funçoes lambdas geralmente são feitas em uma unica linha
totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['preco'],
        compras
    )
)

print('Preços todais:', list(totais))
print('Total geral:', sum(totais))
