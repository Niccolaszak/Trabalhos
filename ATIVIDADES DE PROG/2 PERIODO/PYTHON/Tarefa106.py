#Faça um dicionario com as possibilidade de cores de escrita no python
cores = {
    # Cores de primeiro plano (texto)
    'preto': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'branco': '\033[37m',

    # Cores de fundo
    'fundo_preto': '\033[40m',
    'fundo_vermelho': '\033[41m',
    'fundo_verde': '\033[42m',
    'fundo_amarelo': '\033[43m',
    'fundo_azul': '\033[44m',
    'fundo_magenta': '\033[45m',
    'fundo_ciano': '\033[46m',
    'fundo_branco': '\033[47m', 


    # Estilos
    'negrito': '\033[1m',
    'italico': '\033[3m',
    'sublinhado': '\033[4m',
    'riscado': '\033[9m',

    # Resetar formato
    'reset' : '\033[0m'
}
print(cores['fundo_vermelho'], cores['ciano'],cores['sublinhado'],'Este texto esta com o fundo vermelho em ciano e sublinhado')
print(cores['reset'])