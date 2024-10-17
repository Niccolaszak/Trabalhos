import math

def fac(a, b=0):
    fat = math.factorial(a)
    if b > 0:
        for i in range(a, 0, -1):
            if i > 1:
                print(f'{i} x ', end='')
            if i == 1:
                print(f'{i}', end='')
        print(f' = {fat}')
    else:
        print(f'O resultado é {fat}')

n = int(input('Insira um número para ver o fatorial: '))
s = int(input('Deseja ver o processo? Insira zero para não e qualquer número para sim: '))
fac(n, s)
