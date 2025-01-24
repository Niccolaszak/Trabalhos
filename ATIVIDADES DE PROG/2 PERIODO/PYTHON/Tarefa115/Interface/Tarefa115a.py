import os
from time import sleep as pause
import Arquivo
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
arq = "arquivoteste.txt"

if not Arquivo.arqexist(arq):
    print("Arquivo não encontrado!")
    pause(1)
    Arquivo.criararquivo(arq)

def limpar():
    os.system('cls')

def menu_incio():
    limpar()
    print("=="*20)
    print(cores['amarelo'],"MENU PRINCIPAL".center(40),cores['reset'])
    print("=="*20)
    print(cores['azul'],"Opções disponiveis: ",cores['reset'])
    print(" (1) Ver pessoas cadastradas.\n (2) Cadastrar Novas pessoas.\n (3) Finalizar programa.")
    print("=="*20)
    while True:
        try:
            esc = int(input("Insira uma opção: "))
        except(TypeError,KeyboardInterrupt,ValueError):
            print("=="*20)
            print(cores['vermelho'],"Digite uma opção valida.",cores['reset'])
            print("=="*20)
        else:
            if esc < 4 and esc > 0:    
                break
            else:
                print("=="*20)
                print(cores['vermelho'],"Numero invalido, tente novamente",cores['reset'])
                print("=="*20)
                pause(3)
    if esc == 1:
        limpar()
        print("=="*20)
        print("PESSOAS CADASTRADAS".center(40))
        print("=="*20)
        Arquivo.lerarquivo(arq)
        print("=="*20)
        pause(5)
        menu_incio()
    if esc == 2:
        limpar()
        print("=="*20)
        print("NOVO CADASTRO".center(40))
        print("=="*20)
        try:
            nome = str(input("Nome: "))
            idade = int(input("Idade: "))
        except(KeyboardInterrupt,ValueError,TypeError):
            print(f"{cores['vermelho']}ERRO:Nome e idade não podem estar vazios e a idade deve ser inteira.")
        Arquivo.cadastrar(arq,nome,idade)
        pause(2)
        menu_incio()
    if esc == 3:
        limpar()
        print("=="*20)
        print("OPÇÃO 3".center(40))
        print("=="*20)
        print("Finalizando sistema...")
        pause(5)
        print("=="*20)
        print(f"{cores['ciano']}Sistema finalizado",cores['reset'])
        print("=="*20)

menu_incio()