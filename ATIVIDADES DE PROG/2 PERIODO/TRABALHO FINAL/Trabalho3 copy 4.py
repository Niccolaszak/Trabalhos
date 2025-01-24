#importando as biblioteca utilizadas no codigo:
from time import sleep
import os
import csv
import pandas as pd
#dicionario de cores para deixar o output mais bonito
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
#listas usadas para adicionar serviços e produtos
teste = list()
testeprod = list()
#classe dos serviços
class Serviços:
    id_cont = 1 #variavel utilizada para contar o id dos serviços
    def __init__(self, servico, pet, porte, funcionario, valor):
        #definindo os objetos
        self.id = Serviços.id_cont
        Serviços.id_cont += 1
        self.servico = servico
        self.pet = pet
        self.porte = porte
        self.funcionario = funcionario
        self.valor = valor
        self.lista = {"ID" : self.id, "Servico" : self.servico, "Pet" : self.pet, "Funcionario" : self.funcionario, "Valor" : self.valor}
#classe dos produtos
class Produtos:
    prodid_cont = 1 #variavel utilizada para contar o id dos produtos
    def __init__(self,produto,quantidade,valor):
        #definindo os objetos
        self.id = Produtos.prodid_cont
        Produtos.prodid_cont += 1
        self.prod = produto
        self.quantidade = quantidade
        self.valor = valor
        self.listaprod = {'ID' : self.id , 'Produto' : self.prod , 'Quantidade' : self.quantidade , 'Valor' : self.valor}
#classe da nota fiscal herdando os objetos das classes Serviços e Produtos
class nota_fiscal(Serviços,Produtos):
    def __init__(self):
        super().__init__() #utilizando o super para definir os objetos
    def gerar_nota(self): #Função utilizada para gerar nota de serviços 
        teste.append(self.lista) #adicionando serviço a lista de serviços
    def gerar_notaprod(self): #Função utilizada para gerar nota de produtos
        testeprod.append(self.listaprod) #adicionando produto a lista de produtos
    def exibir_nota(self): #Função utilizada para fazer a pré exibição da nota
        os.system('cls') #limpando o terminal
        total = 0 #Utilizado para setar o total dos valores dos serviços
        #Pré exibindo nota de serviços
        print(f"{cores['azul']}{cores['negrito']}{cores['fundo_branco']}|          Nota Fiscal de Serviços          |")
        print(f"{cores['preto']}| ID | SERVIÇO |  PETs  |  FUNC.  |  VALOR  |")
        for i in teste:
            ident = i["ID"]
            servico = i['Servico']
            pet = i['Pet']
            func = i['Funcionario']
            valor = i['Valor']
            total += valor
            print(f"|{ident:4}|{servico:9s}|{pet:8s}|{func:9s}|{valor:9.2f}|")
        print(f"| TOTAL:                           {cores['verde']}{total:9.2f}|{cores['reset']}")
        totalprod = 0 #Utilizado para setar o total dos valores dos produtos
        #Pré exibindo nota de serviços
        print(f"{cores['azul']}{cores['negrito']}{cores['fundo_branco']}|          Nota Fiscal de Produtos          |")
        print(f"{cores['preto']}| ID | PRODUTO |   QUANTIDADE   |   VALOR   |")
        for i in testeprod:
            identprod = i['ID']
            produto = i['Produto']
            quantidade = i['Quantidade']
            valorprod = i['Valor']
            totalprod += valorprod
            print(f"|{identprod:4}|{produto:9s}|{quantidade:16.2f}|{valorprod:11.2f}|")
        print(f"| TOTAL:                         {cores['verde']}{totalprod:11.2f}|{cores['reset']}")
        print(f"{cores['azul']}{cores['negrito']}{cores['fundo_branco']}|VALOR TOTAL A SER PAGO:           {cores['verde']}{total+totalprod:9.2f}|{cores['reset']}")
        #loop para as opções disponiveis
        while True:
            try: #tentativa até a escolha ser valida
                print("(1) Finalizar Nota Fiscal. \n(2) Excluir Item da nota. \n(0) Voltar.")
                esc = int(input(f"{cores['ciano']}{cores['negrito']}Insira sua escolha: {cores['reset']}"))
            except(TypeError,KeyboardInterrupt,ValueError): #erros possiveis na escolha
                print(f"{cores['vermelho']}{cores['negrito']}{cores['sublinhado']}ERRO: A escolha deve ser um numero inteiro.{cores['reset']}")
            else:
                if esc == 0:
                    tela_inicio()#chama a tela inicial
                    break
                elif esc == 1:
                    nota_fiscal.finalizarnf()#finaliza a nota gerando 1 arquivo csv para cada uma
                    break
                elif esc == 2:
                    nota_fiscal.excluiritem()#exclui itens das notas caso queira
                    break
                elif esc > 2:
                    print(f"{cores['vermelho']}{cores['negrito']}{cores['sublinhado']}Digite um número válido.{cores['reset']}")
                    sleep(2)
    #Variaveis para os numeros de notas
    numero_nfs = 1
    numero_nfp = 1 
    def finalizarnf(): #define como criar os arquivos csv das notas e reseta as pré exibições para mais notas
        print("Salvando Nf...")
        sleep(2)
        nome_arquivo_base = f"nota_fiscal"
        nota_fiscal.salvar_nota(nome_arquivo_base)
        teste.clear()
        testeprod.clear()
        print(f"{cores['verde']}{cores['negrito']}Notas fiscais salvas com sucesso!{cores['reset']}")
        sleep(2)
        tela_inicio()

    def salvar_nota(nome_arquivo_base): #gera os arquivos csv das notas
            '''Esta parte é utilizada para setar o numero atual da nota para o da ultima nota gerada que
             foi salvo em um arquivo .txt assim que for gerado a primeira nota, ambas as notas ficaram 
             com o mesmo numero mesmo que não seja gerado o arquivoz assim separando os pedidos comforme o numero'''          
            try:
                with open('ultimo_numero.txt', 'r') as f:
                    ultimo_numero = int(f.read())
                nota_fiscal.numero_nfs = ultimo_numero + 1
                nota_fiscal.numero_nfp = ultimo_numero + 1
            except FileNotFoundError:
                nota_fiscal.numero_nfs = 1
                nota_fiscal.numero_nfp = 1

            if len(teste) == 0:#caso não haja serviço não sera gerado nota
                print("A nota de serviços esta vazia, não foi gerado o arquivo.")
                sleep(2)
            else:#criação da nota de serviço
                nome_arquivo_servicos = f"{nota_fiscal.numero_nfs}_{nome_arquivo_base}_servicos.csv"
                with open(nome_arquivo_servicos, 'w', newline='') as csvfile:
                    fieldnames = ['ID', 'Servico', 'Pet', 'Funcionario', 'Valor']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(teste)
                    

            if len(testeprod) == 0:#caso não haja produtos na nota não sera gerado o arquivo
                print("A nota de produtos esta vazia, não foi gerado o arquivo.")
                sleep(2)
            else:#gera o arquivo da nota de produtos
                nome_arquivo_produtos = f"{nota_fiscal.numero_nfp}_{nome_arquivo_base}_produtos.csv" 
                with open(nome_arquivo_produtos, 'w', newline='') as csvfile:
                    fieldnames = ['ID', 'Produto', 'Quantidade', 'Valor']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(testeprod)
                    
            with open('ultimo_numero.txt', 'w') as f:#salva o ultimo numero para futuras emissões
                f.write(str(nota_fiscal.numero_nfs))

    def excluiritem():#função utilizada para excluir item da nota segundo o ID dele na nota,
                      #caso haja 2 ou mais IDs na nota e seja excluido um id do meio os maiores serão empurrados para os menores
        while True:#faz a seleção de qual item excluir
            try:
                os.system('cls')
                print(f"{cores['verde']}=="*20,cores['reset'])
                print(f"{cores['amarelo']}{cores['negrito']}           EXCLUSÃO DE ITENS".center(40),cores['reset'])
                print(f"{cores['verde']}=="*20,cores['reset'])
                print("Escolha a nota que quer excluir um item:\n(1) Serviços.\n(2) Produtos.\n(0) Voltar a exibição.")
                esc = int(input(f"{cores['ciano']}{cores['negrito']}Sua escolha: {cores['reset']}"))
            except(ValueError,TypeError,KeyboardInterrupt):
                print(f"{cores['vermelho']}{cores['negrito']}{cores['sublinhado']}ERRO: A escolha deve ser um número inteiro.{cores['reset']}")
                sleep(2)
            else:
                if esc == 0:
                    nota_fiscal.exibir_nota("")
                elif esc == 1:
                    if len(teste) == 0:
                        print(f"{cores['vermelho']}{cores['negrito']}{cores['sublinhado']}Não há serviços adicionados na nota.{cores['reset']}")
                        sleep(2)
                    else:
                        try:
                            print("Insira 0 para voltar a exibição.")
                            id_excluir = int(input(f"{cores['ciano']}{cores['negrito']}Insira o ID do Serviço que deseja excluir: {cores['reset']}"))
                            if id_excluir == 0:
                                nota_fiscal.exibir_nota("")
                            else: 
                                for i, item in enumerate(teste):
                                    if item["ID"] == id_excluir:
                                        del teste[i]
                                        print(f"{cores['verde']}{cores['negrito']}Serviço com o ID {id_excluir} excluido com sucesso!{cores['reset']}")
                                        sleep(2)
                                        break
                                else:
                                    print(f"Serviço com ID {id_excluir} não encontrado!")
                        except (ValueError,TypeError,KeyboardInterrupt):
                            print(f"{cores['vermelho']}{cores['negrito']}{cores['sublinhado']}ERRO: O ID precisa ser um número inteiro.{cores['reset']}")
                            sleep(2)
                elif esc == 2:
                    if len(testeprod) == 0:
                        print(f"{cores['vermelho']}{cores['negrito']}{cores['sublinhado']}Não há produtos adicionados na nota.{cores['reset']}")
                        sleep(2)
                    else:
                        try:
                            print("Insira 0 para voltar a exibição.")
                            idprod_excluir = int(input(f"{cores['ciano']}{cores['negrito']}Insira o ID do Serviço que deseja excluir: {cores['reset']}"))
                            if idprod_excluir == 0:
                                nota_fiscal.exibir_nota()
                            else:#exclui o item conforme id informado
                                for i, item in enumerate(testeprod):
                                    if item["ID"] == idprod_excluir:
                                        del testeprod[i]
                                        print(f"{cores['verde']}{cores['negrito']}Produto com o ID {idprod_excluir} excluido com sucesso!{cores['reset']}")
                                        sleep(2)
                                        break
                                else:
                                    print(f"Serviço com ID {idprod_excluir} não encontrado!")
                        except (ValueError,TypeError,KeyboardInterrupt):
                            print(f"{cores['vermelho']}{cores['negrito']}{cores['sublinhado']}ERRO: O ID precisa ser um número inteiro.")
                            sleep(2)
                elif esc > 2:
                    print(f"{cores['vermelho']}{cores['negrito']}{cores['sublinhado']}Digite um número válido.{cores['reset']}")
                    sleep(2)

def ler_e_exibir_csv(arquivo):
    """Lê um arquivo CSV e exibe seus dados em formato de tabela."""
    try:
        df = pd.read_csv(arquivo, encoding='utf-8')
        print(cores['amarelo'], df.to_string(index=False))
    except FileNotFoundError:
        print(f"Arquivo '{arquivo}' não encontrado.")
    except pd.errors.ParserError:
        print("Erro ao ler o arquivo CSV. Verifique se o formato está correto.")

def exibir_nota_csv():
    """Permite ao usuário escolher o tipo de nota e o arquivo a ser exibido."""
    while True:
        try:
            esc = int(input(f"Deseja visualizar uma nota de:\n(1) Serviços.\n(2) Produtos.\n{cores['negrito']}{cores['ciano']}Digite sua opção: {cores['reset']}"))
            if esc not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print(f"{cores['vermelho']}{cores['negrito']}{cores['sublinhado']}Opção inválida.{cores['reset']}")

    numero = input(f"{cores['negrito']}{cores['ciano']}Insira o número da nota: {cores['reset']}")
    tipo = "servicos" if esc == 1 else "produtos"
    arquivo = f"{numero}_nota_fiscal_{tipo}.csv"
    os.system('cls')
    ler_e_exibir_csv(arquivo)
    try:
        esc = int(input(f"{cores['negrito']}{cores['ciano']}Insira 0 para retornar a tela de inicio: {cores['reset']}"))
        if esc == 0:
            tela_inicio()
        else:
            raise ValueError
    except(ValueError,KeyboardInterrupt,TypeError):
        print(f"{cores['vermelho']}{cores['negrito']}{cores['sublinhado']}Para retornar o numero digitado deve ser 0.{cores['reset']}")

               


#listas e dicionarios com informações fixas como funcionarios, serviços, produtos e preços
funcionarios = ["Gessika", "Bruna", "Jonas"]
prod = ["Ração", "Camas", "Come/Bebe", "Casinhas", "T.H. 30UN"]
valores_prod = [10.99, 43.00, 19.99, 79.90, 85.99]
serv = ["BANHO", "TOSA", "PASSEIO"]
valores = [50.00, 30.00, 10.00]

def dados(a):#Coleta os dados do serviço e o adiciona na lista de serviços 
    while True:
        try:
            os.system('cls')
            print(f"{cores['verde']}=="*20,cores['reset'])
            print(f"{cores['amarelo']}{cores['negrito']}        COLETANDO AS INFORMAÇÕES".center(40),cores['reset'])
            print(f"{cores['verde']}=="*20,cores['reset'])
            print("Insira 0 para voltar a tela de serviços")
            pet = str(input(f"{cores['ciano']}{cores['negrito']}Qual o tipo de pet: {cores['reset']}")).upper().strip()
            if not pet:
                raise TypeError('O Pet não pode ser vazio ou conter apenas espaços!')
            elif pet not in ["GATO","CACHORRO","0"]:
                raise TypeError("Não temos suporte para este tipo de pet!")
        except TypeError as e:
            print(f"{cores["vermelho"]}{cores['negrito']}{cores['sublinhado']}ERRO: {e}{cores['reset']}")
            sleep(2)
        else:
            if pet == "0":
                exibserv()
            else:
                break


    while True:
        try:
            os.system('cls')
            print(f"{cores['verde']}=="*20,cores['reset'])
            print(f"{cores['amarelo']}{cores['negrito']}        COLETANDO AS INFORMAÇÕES".center(40),cores['reset'])
            print(f"{cores['verde']}=="*20,cores['reset'])
            print("Insira 0 para voltar a tela de serviços")
            porte = str(input(f"{cores['ciano']}{cores['negrito']}Qual o porte do Pet: {cores['reset']}")).upper().strip()
            if not porte:
                raise TypeError("O porte não pode estar vazio ou apenas com espaços!")
            elif porte not in ["PEQUENO","MEDIO", "MÉDIO", "GRANDE", "0"]:
                raise TypeError("O porte não pode ser diferente de pequeno, médio ou grande!")
        except TypeError as e:
            print(f"{cores["vermelho"]}{cores['negrito']}{cores['sublinhado']}ERRO: {e}{cores['reset']}")
            sleep(2)
        else:
            if porte == "0":
                exibserv()
            else:
                break

    if a == 3:
        funcionario = funcionarios[a-1]
        servico = serv[a-1]
        while True:
            try:
                os.system('cls')
                print(f"{cores['verde']}=="*20,cores['reset'])
                print(f"{cores['amarelo']}{cores['negrito']}        COLETANDO AS INFORMAÇÕES".center(40),cores['reset'])
                print(f"{cores['verde']}=="*20,cores['reset'])
                print("Insira 0 para voltar a tela de serviços")
                d = str(input(f"{cores['ciano']}{cores['negrito']}Insira a distância do passeio em KM: {cores['reset']}")).replace(',', '.')
                d = float(d)
            except (ValueError, TypeError, KeyboardInterrupt):
                print(f"{cores["vermelho"]}{cores['negrito']}{cores['sublinhado']}ERRO: A distancia precisa ser um numero real!{cores['reset']}")
                sleep(2)
            else:
                if d == 0:
                    exibserv()
                else:    
                    valor = d*valores[a-1]
                    break
    else:
        funcionario = funcionarios[a-1]
        valor = valores[a-1]
        servico = serv[a-1]


    os.system('cls')
    retorno = Serviços(servico, pet, porte, funcionario, valor)
    nota_fiscal.gerar_nota(retorno)
    print(f"{cores['verde']}=="*20,cores['reset'])
    print(f"{cores['amarelo']}{cores['negrito']}          SALVANDO SERVIÇO".center(40),cores['reset'])
    print(f"{cores['verde']}=="*20,cores['reset'])
    sleep(3)
    print(f"{cores['verde']}=="*20,cores['reset'])
    print(f"{cores['ciano']}{cores['negrito']}       SERVIÇO SALVO COM SUCESSO!".center(40),cores['reset'])
    print(f"{cores['verde']}=="*20,cores['reset'])
    sleep(2)
    tela_inicio()

def dados_prod(a):#coleta dados dos produtos e o adiciona na lista de produtos
    if a == 1:
        while True:
            try:
                os.system('cls')
                print(f"{cores['verde']}=="*20,cores['reset'])
                print(f"{cores['amarelo']}{cores['negrito']}        COLETANDO AS INFORMAÇÕES".center(40),cores['reset'])
                print(f"{cores['verde']}=="*20,cores['reset'])
                print("Insira 0 para voltar a tela de serviços")
                quantidade = float(input(f"{cores['ciano']}{cores['negrito']}Insira a quantidade em KG que deseja de ração: {cores['reset']}"))
            except (ValueError, TypeError, KeyboardInterrupt):
                print(f"{cores['vermelho']}{cores['negrito']}{cores['sublinhado']}ERRO: A Quantidade precisa ser um número real, tente novamente!{cores['reset']}")
                sleep(2)
            else:
                break
    else:
        while True:        
            try:
                os.system('cls')
                print(f"{cores['verde']}=="*20,cores['reset'])
                print(f"{cores['amarelo']}{cores['negrito']}        COLETANDO AS INFORMAÇÕES".center(40),cores['reset'])
                print(f"{cores['verde']}=="*20,cores['reset'])
                print("Insira 0 para voltar a tela de serviços")
                quantidade = int(input(f"{cores['ciano']}{cores['negrito']}Insira a quantidade em UN do produto: {cores['reset']}"))
            except(ValueError, TypeError, KeyboardInterrupt):
                print(f"{cores['vermelho']}{cores['negrito']}{cores['sublinhado']}ERRO: A quantidade precisa ser um número inteiro!{cores['reset']}")
                sleep(2)
            else:
                break
        if quantidade == 0:
            tela_inicio()

    if a == 2 or a == 3 or a == 4:
        while True:
            try:
                os.system('cls')
                print(f"{cores['verde']}=="*20,cores['reset'])
                print(f"{cores['amarelo']}{cores['negrito']}        COLETANDO AS INFORMAÇÕES".center(40),cores['reset'])
                print(f"{cores['verde']}=="*20,cores['reset'])
                tamanho = str(input(f"{cores['ciano']}{cores['negrito']}Digite P, M ou G para o tamanho: {cores['reset']}")).upper().strip()
                if not tamanho:
                    raise TypeError("O Tamanho não pode estar vazio ou apenas com espaços!")
                elif tamanho not in ["P", "M", "G", "0"]:
                    raise TypeError("O Tamanho não pode ser diferente de P, M ou G!")
            except TypeError as e:
                print(f"{cores['vermelho']}{cores['negrito']}{cores['sublinhado']}ERRO: {e}{cores['reset']}")
                sleep(2)
            else:
                if tamanho == "M":
                    valor = valores_prod[a-1]*1.5*quantidade
                    break
                elif tamanho == "G":
                    valor = valores_prod[a-1]*2*quantidade
                    break
                else:
                    valor = valores_prod[a-1]*quantidade
                    break
    else:
        valor = valores_prod[a-1]*quantidade
    produto = prod[a-1]
    os.system('cls')
    retorno = Produtos(produto, quantidade, valor)
    nota_fiscal.gerar_notaprod(retorno)
    print(f"{cores['verde']}=="*20,cores['reset'])
    print(f"{cores['amarelo']}{cores['negrito']}          SALVANDO PRODUTO".center(40),cores['reset'])
    print(f"{cores['verde']}=="*20,cores['reset'])
    sleep(3)
    print(f"{cores['verde']}=="*20,cores['reset'])
    print(f"{cores['ciano']}{cores['negrito']}       PRODUTO SALVO COM SUCESSO!".center(40),cores['reset'])
    print(f"{cores['verde']}=="*20,cores['reset'])
    sleep(2)
    tela_inicio()
        
    

def exibserv():#exibe as escolhas de serviços disponiveis
    while True:
        os.system('cls')
        print(f"{cores['verde']}=="*20,cores['reset'])
        print(f"{cores['amarelo']}{cores['negrito']}          SERVIÇOS DISPONIVEIS".center(40))
        print(f"{cores['verde']}=="*20,cores['reset'])
        print("(1) Banho\n(2) Tosa\n(3) Passeio\n(0) Voltar")
        try:
            esc = int(input(f"{cores['ciano']}{cores['negrito']}Qual serviço deseja executar: {cores['reset']}"))
        except(ValueError,TypeError,KeyboardInterrupt):
            print(f"{cores["vermelho"]}{cores['negrito']}{cores['sublinhado']}ERRO: A escolha deve ser um número inteiro, tente novamente!{cores['reset']}")
            sleep(2)
        else:    
            if esc == 1:
                dados(1)
                break
            if esc == 2:
                dados(2)
                break
            if esc == 3:
                dados(3)
                break
            if esc == 0:
                tela_inicio()
                break
       


def exibprod():#exibe as escolhas de produtos disponiveis
     while True:
        try:
            os.system('cls')
            print(f"{cores['verde']}=="*20,cores['reset'])
            print(f"{cores['amarelo']}{cores['negrito']}          PRODUTOS DISPONIVEIS".center(40))
            print(f"{cores['verde']}=="*20,cores['reset'])
            print("(1) Ração\n(2) Camas\n(3) Comedouro/Bebedouro\n(4) Casinhas\n(5) Tapete Higienico(pac.30UN)\n(0) Voltar")
            esc = int(input(f"{cores['ciano']}{cores['negrito']}Qual produto deseja pedir: {cores['reset']}"))
        except(TypeError,ValueError,KeyboardInterrupt):
            print(f"{cores['vermelho']}{cores['negrito']}{cores['sublinhado']}ERRO: A escolha deve ser um numero inteiro, tente novamente!")
            sleep(2)
        else:
            if esc == 1:
                dados_prod(1)
                break
            if esc == 2:
                dados_prod(2)
                break
            if esc == 3:
                dados_prod(3)
                break
            if esc == 4:
                dados_prod(4)
                break
            if esc == 5:
                dados_prod(5)
                break
            if esc == 0:
                tela_inicio()
                break


def tela_inicio():#exibe a tela inicial do programa
    os.system('cls')
    print(f"{cores['verde']}=="*20,cores['reset'])
    print(f"{cores['amarelo']}{cores['negrito']}     BEM VINDO AO PETSHOP CANTAGALO".center(40),cores['reset'])
    print(f"{cores['verde']}=="*20,cores['reset'])    
    try:
        esc = int(input(f"(0) Finalizar Programa.\n(1) Serviços.\n(2) Produtos.\n(3) Exibir Nota Fiscal.\n(4) Vizualizar nota existente.{cores['ciano']}\n{cores['ciano']}{cores['negrito']}Sua escolha: {cores['reset']}"))
    except(TypeError, ValueError, KeyboardInterrupt): 
        print(f'{cores["vermelho"]}{cores['negrito']}{cores['sublinhado']}ERRO: a escolha deve ser um número inteiro, tente novamente.{cores["reset"]}')
        sleep(2)
        os.system('cls')
        tela_inicio()
    else:
        if esc == 0:
            print(f"{cores['amarelo']}Programa finalizado.")
        elif esc == 1:
            exibserv()
        elif esc == 2:
            exibprod()
        elif esc == 3:
            nota_fiscal.exibir_nota("")
        elif esc == 4:
            exibir_nota_csv()
        elif esc > 4 or esc < 0:
            print(f"{cores["vermelho"]}{cores['negrito']}{cores['sublinhado']}ERRO: Número invalido, tente novamente.{cores["reset"]}")
            sleep(2)
            tela_inicio()

tela_inicio()#Chama a tela inicial para executar o codigo