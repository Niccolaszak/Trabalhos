#Exercício  Python 086: Crie um programa que declare uma matriz de dimensão 3×3
#e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [[[],[],[]],[[],[],[]],[[],[],[]]]
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
#print(matriz[0][0],matriz[0][1],matriz[0][2])
#print(matriz[1][0],matriz[1][1],matriz[1][2])
#print(matriz[2][0],matriz[2][1],matriz[2][2])
