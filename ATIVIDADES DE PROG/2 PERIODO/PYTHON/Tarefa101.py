from datetime import date
def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} não vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} o voto é opcional.'
    else:
        return f'Com {idade} o voto é obrigatorio.'
a = int(input('Insira o seu ano de nascimento: '))
print(voto(a))