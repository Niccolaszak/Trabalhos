from time import sleep
import os

class Serviços:
    def __init__(self, servico, pet, porte, funcionario, valor):
        self.servico = servico
        self.pet = pet
        self.porte = porte
        self.funcionario = funcionario
        self.valor = valor
    def __str__(self):
        return f"Serviço: {self.servico} \nPet: {self.pet} \nPorte: {self.porte} \nFuncionário: {self.funcionario} \nValor: R$ {self.valor:.2f}"

class Nfse(Serviços):
    def __init__(self,servico,pet,funcionario,valor):
        super().__init__(servico,pet,funcionario,valor)
    def info(self):
        print("NOTA DE SERVIÇOS")
        print(Serv_nf)



funcionarios = ["Gecika", "Brhunna", "Jhonnas"]

valores = [50.00, 30.00, 10.00]

serv = ["banho", "tosa", "passeio"]

Serv_nf = list()
def dados(a):
    while True:
        os.system('cls')
        print("Insira 0 para voltar a tela de serviços")
        pet = str(input("Qual o tipo de pet: ")).upper()
        if pet == "0":
            exibserv()
        elif pet not in ["GATO", "CACHORRO"]:
            print("Infelizmente não atendemos este tipo de animal\npor favor tente novamente")
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
            sleep(3)
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
    else:
        funcionario = funcionarios[a-1]
        valor = valores[a-1]
        servico = serv[a-1]

    os.system('cls')
    retorno = Serviços(servico, pet, porte, funcionario, valor)
    print(retorno)
    Serv_nf.append(retorno)
    if a == 3:
        print(f"Distancia: {dist}")
    print("Salvando serviço...")
    sleep(5)
    print("Serviço salvo com sucesso")
    sleep(3)

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
    esc = int(input("Deseja vizualizar nossos:\n(1) Serviços.  (2) Produtos.\nInsira a opção escolhida: "))
    if esc == 1:
        exibserv()
    elif esc == 2:
        exibprod()
    else:
        print('escolha invalida, tente novamente')
        sleep(3)
        os.system('cls')
        tela_inicio()

tela_inicio()