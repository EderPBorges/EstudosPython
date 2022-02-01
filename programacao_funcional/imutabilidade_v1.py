#!python3
from locale import setlocale, LC_ALL
from calendar import month_name, mdays
from functools import reduce
from xml.dom import NoModificationAllowedErr

# Potugues do Brasil
setlocale(LC_ALL, '')

# Listar todos os meses do ano com 31 dias
# 1. (filter) pegar os indices de todos os meses com 31 dias...
# 2. (map) transformar os índices em nome
# 3. (reduce) juntar tudo para imprimir
meses = filter(lambda mes: mdays[mes] == 31, range(1, 13))
meses_nome = map(lambda mes: month_name[mes], meses)
juntar_meses = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
                      meses_nome, 'Meses com 31 dias:')
print(juntar_meses)

# /\ BEM MAIS ORGANIZADO

print(
    reduce(
        lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
        map(
            lambda mes: month_name[mes],
            filter(
                lambda mes: mdays[mes] == 31,
                range(1, 13)
            )
        ),
        'Meses com 31 dias:'
    )
)