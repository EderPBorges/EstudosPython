#!python3

def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError("dividir() deve receber apenas argumentos inteiros")
    try:
        aux = dividendo / divisor
    except:
        print(f"Não foi possivel dividir {dividendo} por {divisor}")
        raise

    return aux    

def testa_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f"O resultado da divisão de 10 por {divisor} é {resultado}")


try:
    testa_divisao(2.5)
except ZeroDivisionError as E:
    print("Erro de divisao por zero")
except AttributeError as E:
    print("Tratamento generico")


print("Programa encerrado")
