def escreva(msg):
    tam=len(msg)+4
    print('~'*tam)
    print(msg)
    print('~'*tam)
nome = str(input('Insira seu nome: '))
escreva(nome)