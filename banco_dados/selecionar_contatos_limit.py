#!python3
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'SELECT * FROM contatos LIMIT 5'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        contatos = cursor.fetchall() # em uma tabela com muitos dados, esse comando pode gerar um problema de desempenho
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato[2]:2d} = {contato[0]:10s} Telefone: {contato[1]}')    