#!python3
#x = 0

#while x != -1:
#    x = float(input('INforme o número ou -1 para sair: '))
#print('Fim!')



#x = 10

#while x:    <-- em uma situação como essa, é melhor usar o for
#    print(x) 
#    x -= 1

#print('Fim!')    



total = 0
qtde = 0
nota = 0

while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair '))
    if nota != -1:
        qtde += 1
        total += nota

print(f'A média da turma é  {total / qtde}')
