#!python3

def fibonacci(quantidade):
    resultado = [0, 1]
    for i in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado
        

if __name__ == '__main__':
    # Listar os 20 primeiros numeros da sequência
    for fib in fibonacci(20):
        print(fib)