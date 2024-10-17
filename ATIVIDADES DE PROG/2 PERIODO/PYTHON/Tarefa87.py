'''Exercício  Python 087: Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.                                                                                                  
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.'''
matriz = [[[],[],[]],[[],[],[]],[[],[],[]]]
pares = []
somapares = 0
print('VAMOS PREENCHER UMA MATRIZ 3x3')
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c].append(int(input(f'Insira o valor da posição {l}x{c}: ')))
print('Matriz preenchida com sucesso')
print('Ela ficou assim:')
for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]}', end='')
    print()
for l in range(0,3):
    for c in range(0,3):
     if (num % 2 for num in matriz) == 0:
        pares.append(matriz[l][c])
        somapares += matriz[l][c]
print(f'Os numeros pares digitados foram {pares} e a soma total deles é {somapares}')
print(f'A soma total dos valores da terceira coluna é {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
if matriz[1][0]>matriz[1][1] and matriz[1][0]>matriz[1][2]:
    print(f'O maior valor da segunda linha é {matriz[1][0]}')
elif matriz[1][1]>matriz[1][0] and matriz[1][1]>matriz[1][2]:
    print(f'O maior valor da segunda linha é {matriz[1][1]}')
elif matriz[1][2]>matriz[1][0] and matriz[1][2]>matriz[1][1]:
    print(f'O maior valor da segunda linha é {matriz[1][2]}')