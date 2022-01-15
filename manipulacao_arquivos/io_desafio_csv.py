#!python3
import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        dados = entrada.read().decode('latin1')
        print('Download completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    # o r \/ executa de forma literal, evita que caracteres especiais sejam interpretados de forma indevida.
    # normalmente usado quando se trabalha com url...(ex: evita caracteres como o \n que pula uma linha)
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
