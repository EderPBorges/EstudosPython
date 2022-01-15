#!python3

# for i in range (1, 11):
#    if i == 6:
#        break
#    print(i)
# else:
#    print('Fim!')

# Funcao sortear_dado numeros entre 1 e 6
# For com range 1 a 6
# se for impar continue
# se o numero for par e for igual ao valor sorteado
# pela funcao dado imprimir 'Aceito' e depois chamar o break
# se não acertar chama o else...print('Não acertou o numero!')

from random import randint


def sortear_dado():
    return randint(1, 6)

# \/ DESAFIO!

#numero_informado = -1

# for i in range(1, 7):
#    numero_sorteado = sortear_dado()
#    numero_informado = int(input('Informe o numero: '))
#    if numero_informado % 2 == 1:
#        continue
#    if numero_informado % 2 == 0 and numero_informado == numero_sorteado:
#        print('Acertou!')
#        break
#    else:
#        print('Não acertou o numero:')

# Resposta \/


for i in range(1, 7):
    if i % 2 == 1:
        continue

    if sortear_dado() == i:
        print('Acertou!', i)
        break
else:
    print('Não acertou o número! ')
