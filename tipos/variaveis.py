#!python3
a = 3
b = 4.4
print (a + b)

texto = "Sua idade é..."
idade = 23

# print(texto + str(idade)) convertendo idade em string

print(f'{texto} {idade}')

# print(3 * 'bom dia ') possibilidade de multiplicar strings

PI = 3.14
raio = float(input('Informe o raio da circ? '))
#area = PI * raio * raio
area = PI * pow(raio, 2)
print(f'A área da circ é {area} m2. ')

# print(type(raio)) saber o tipo da variavel
