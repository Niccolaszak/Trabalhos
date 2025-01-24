#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
#da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat()
#com a mesma funcionalidade.
def leiaint(msg):
    valor = 0
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError, KeyboardInterrupt):
            print("ESTA ENTRADA NÃO É VALIDA, TENTE NOVAMENTE")
        else:
            print("entrada valida.")
            return n
n = leiaint('Insira um numero: ')
print(f'Voce digitou o numero {n}')