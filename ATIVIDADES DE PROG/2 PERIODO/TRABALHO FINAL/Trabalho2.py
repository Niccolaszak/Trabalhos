from time import sleep
import os

teste = list()
class Serviços:
    def __init__(self, servico, pet, porte, funcionario, valor):
        self.servico = servico
        self.pet = pet
        self.porte = porte
        self.funcionario = funcionario
        self.valor = valor
        self.lista = {"Serviço" : self.servico, "Pet" : self.pet, "Funcionario" : self.funcionario, "Valor" : self.valor}
class nota_fiscal(Serviços):
    def __init__(self):
        super().__init__()
    def gerar_nota(self):  
        teste.append(self.lista)
    def exibir_nota(self):
        os.system('cls')
        total = 0
        print("Nota Fiscal")
        print("| SERVIÇO |  PETs  |  FUNC.  |  VALOR  |")
        for i in teste:
            servico = i['Serviço']
            pet = i['Pet']
            func = i['Funcionario']
            valor = i['Valor']
            total += valor
            print(f"|{servico:9s}|{pet:8s}|{func:9s}|{valor:9.2f}|")
        print(f"| TOTAL:                      {total:9.2f}|")
        while True:
            esc = str(input("Insira 0 para retornar a tela inicial: "))
            if esc == "0":
                tela_inicio()
            else:
                print("Entrada invalida tente novamente")
                sleep(2)


funcionarios = ["Gessika", "Bruna", "Jonas"]


valores = [50.00, 30.00, 10.00]


serv = ["BANHO", "TOSA", "PASSEIO"]
def dados(a):
    while True:
        os.system('cls')
        print("Insira 0 para voltar a tela de serviços")
        pet = str(input("Qual o tipo de pet: ")).upper()
        if pet == "0":
            exibserv()
        elif pet not in ["GATO", "CACHORRO"]:
            print("Infelizmente não damos banho neste tipo de animal\npor favor tente novamente")
            sleep(3)
        else:
            break


    while True:
        os.system('cls')
        print("Insira 0 para voltar a tela de serviços")
        porte = str(input("Qual o porte do Pet: ")).upper()
        if porte == "0":
            exibserv()
        elif porte not in ["PEQUENO", "MEDIO", "GRANDE"]:
            print("Porte diferente de: pequeno, médio ou grande\nInsira um porte válido")
            sleep(2)
        else:
            break
    if a == 3:
        funcionario = funcionarios[a-1]
        servico = serv[a-1]
        while True:
            os.system('cls')
            d = input('Insira a distância do passeio em KM: ')
            if d.isnumeric():
                dist = float(d)
                valor = dist*valores[a-1]
                break
            else:
                print("Distancia precisa ser numerica, tente novamente")
                sleep(2)
    else:
        funcionario = funcionarios[a-1]
        valor = valores[a-1]
        servico = serv[a-1]


    os.system('cls')
    retorno = Serviços(servico, pet, porte, funcionario, valor)
    nota_fiscal.gerar_nota(retorno)
    print("Salvando serviço...")
    sleep(3)
    print("Serviço salvo com sucesso")
    sleep(2)
    tela_inicio()


def exibserv():
    os.system('cls')
    print("SERVIÇOS DISPONIVEIS")
    print("(1) Banho\n(2) Tosa\n(3) Passeio\n(0) Voltar")
    esc = int(input("Qual serviço deseja executar: "))
    if esc == 1:
        dados(1)
    if esc == 2:
        dados(2)
    if esc == 3:
        dados(3)
def exibprod():
    print('PRODUTOS')


def tela_inicio():
    os.system('cls')
    print("BEM VINDO AO PETSHOP CANTAGALO")
    esc = str(input("Deseja vizualizar nossos:\n(1) Serviços.  (2) Produtos.\n(3) Exibir Nota Fiscal.\nInsira a opção escolhida: "))
    if esc == "1":
        exibserv()
    elif esc == "2":
        exibprod()
    elif esc == "3":
        nota_fiscal.exibir_nota("")
    else:
        print('escolha invalida, tente novamente')
        sleep(2)
        os.system('cls')
        tela_inicio()


tela_inicio()
