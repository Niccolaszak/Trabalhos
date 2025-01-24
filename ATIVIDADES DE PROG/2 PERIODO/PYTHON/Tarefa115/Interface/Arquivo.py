from time import sleep as pause
def arqexist(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print("Houve um qrro ao criar o arquivo!")
        pause(1)
    else:
        print(f"O arquivo {nome} foi criado com sucesso!")
        pause(1)

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao abrir o arquivo!")
    else:
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()
    

def cadastrar(arq,nome='desconhecido',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("ERRO: não foi possivel adicionar ao arquivo")
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print("ERRO: Dados não foram escritos")
        else:
            print("Cadastro efetuado com sucesso")
            a.close()