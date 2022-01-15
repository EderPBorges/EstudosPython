#!python3

def nota_conceito(valor):
    nota = float(valor)

    if (nota < 0 or nota > 10):
        print('Nota invalida. ')
    elif (nota >= 9.1):
        print('A')
    elif (nota > 8.1 and nota <= 9.0):
        print('A-')
    elif (nota >= 7.1 and nota <= 8.0):
        print('B')
    elif (nota > 6.1 and nota <= 7.0):
        print('B-')
    elif (nota >= 5.1 and nota <= 6.0):
        print('C')
    elif (nota > 4.1 and nota <= 5.0):
        print('C-')
    elif (nota >= 3.1 and nota <= 4.0):
        print('D')
    elif (nota > 1.1 and nota <= 2.0):
        print('E')
    elif (nota >= 0.0 and nota <= 1.0):
        print('E-')

if __name__ == '__main__':
    nota = input('Informe a nota: ')
    conceito = nota_conceito(nota)
