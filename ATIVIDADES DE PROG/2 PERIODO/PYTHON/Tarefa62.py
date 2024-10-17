#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
c = 0
p1 = float(input('Insira o primeiro term da PA: '))
ra = float(input('Insira a Razão da PA: '))
print('Os 10 primeiros termos da PA são: ')
while c < 10:
    print(p1,end=", ")
    p1=p1+ra
    c +=1
esc = 'S'
while esc == 'S':
    esc = str(input('\nQuer mostrar mais termos da PA?(S/N)')).upper()
    if esc == 'S':
        mais= int(input('Quants mais?'))
        print('Os proximos {} termos são:'.format(mais))
        c=0
        while c < mais:
            print(p1,end=", ")
            p1=p1+ra
            c +=1
    elif esc != 'S' and esc != 'N':
        print('escolha invalida')
print('Programa Finalizado')