def ficha(nome='Não informado',gols='Não informado'):
    print(f"O nome do jogador é")
    print(f'{nome}')
    print(f"Ele fez está quantia de gols:")
    print(f"{gols}")
n = str(input('insira o nome do jogador: '))
g = str(input('Insira quantos gols ele fez: '))
print(ficha(n,g))