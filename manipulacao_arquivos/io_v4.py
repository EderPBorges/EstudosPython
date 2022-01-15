#!python3

try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
        # o * a cima é um operador de argumentos variaveis, pega todos os argumentos do arquivo e passa para ser interpolado pela string
finally:
    print('finally')
    arquivo.close()

if arquivo.closed:
    print('Arquivo já foi fechado!')
