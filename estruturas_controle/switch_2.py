#!python3

# desafio \/

# def dia_semana(dia):
#    dias = {
#        1: 'Domingo',
#        2: 'Segunda',
#        3: 'Terça',
#        4: 'Quarta',
#        5: 'Quinta',
#        6: 'Sexta',
#        7: 'Sábado',
#    }
#    return dias.get(dia)


# if __name__ == '__main__':
#
#    dia_informado = int(input('Informe o dia: '))
#
#    if dia_informado < 1 or dia_informado > 7:
#        print('Dia invalido! ')
#    else:
#        dia_semana(dia_informado)
#        if dia_informado >= 2 and dia_informado <= 6:
#            print(f'{dia_semana(dia_informado)} é um dia util')
#        else:
#            print(f'{dia_semana(dia_informado)} é fim de semana')

# resposta \/

def get_tipo_dia(dia):
    dias = {
        1: 'Fim de semana',
        2: 'Dia de semana',
        3: 'Dia de semana',
        4: 'Dia de semana',
        5: 'Dia de semana',
        6: 'Dia de semana',
        7: 'Fim de semana',
    }
    return dias.get(dia, '** inválido **')

if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia}: {get_tipo_dia(dia)}')