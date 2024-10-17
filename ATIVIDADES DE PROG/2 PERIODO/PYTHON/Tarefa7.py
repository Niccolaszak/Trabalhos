#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('Se Suas notas foram {:.1f} e {:.1f}, entao a sua media eh {:.f1} '.format(n1, n2, ((n1+n2)/2)))