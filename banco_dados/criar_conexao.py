import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=172.17.0.2"
    "Database=wm;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexao bem Sucedida")