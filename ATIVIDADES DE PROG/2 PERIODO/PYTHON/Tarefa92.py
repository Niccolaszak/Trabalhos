#Exercício  Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
#o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Insira o nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = int(datetime.now().year-nasc)
dados['CTPS'] = int(input('Insira a CTPS (0 não possui): '))
if dados['CTPS'] > 0:
    dados['Ano de contratação'] = int(input('Insira o ano de contratação: '))
    dados['Salario'] = float(input('Insira o salario: '))
    dados['Aposentadoria'] = dados['idade']+35
print('--'*20)
for k,v in dados.items():
    print(f'{k} é {v}')
print('--'*20)