#!python3
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


def help(script):
    print("É necessário informar o raio do círculo.")
    print("Sintaxe: {} <raio>".format(script))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help(sys.argv[0])
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do círculo: ', area)
