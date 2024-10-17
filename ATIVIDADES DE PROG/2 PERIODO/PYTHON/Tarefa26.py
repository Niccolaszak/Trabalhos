#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Escreva uma Frase: ')).upper()
print('Analisando a frase a Letra A apareceu {} vezes sendo a primeira em {} e a ultima em {}'.format(frase.count('A'),frase.find('A')+1,frase.rfind('A')+1))