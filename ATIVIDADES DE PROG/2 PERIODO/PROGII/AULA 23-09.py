from time import sleep
'''class Classe:
    def __init__(self,a,b):

        self.a = a

        self.b = b
    def introdução(self):
        print(f"tributo a: {self.a}")
        print(f"tributo b: {self.b}")
classe1 = Classe('aspirador de pó','xevette')
classe1.introdução()
'''

class Classe:
    def __init__(self,RAM,CPU,SO):
        self.RAM = RAM
        self.CPU = CPU
        self.SO = SO
    def ligar(self):
        print('Estou ligando')
    def info(self):
        print(f"O sistem operacional é: {self.SO}")
        print(f"A memoria RAM é: {self.RAM}")
        print(f"A CPU é: {self.CPU}")
    def desligar(self):
        print('Estou desligando')
classe1 = Classe('8gb','corei5','Windows')
classe1.ligar()
sleep(1);
classe1.info()
sleep(25)
classe1.desligar()
sleep(2)
print('the program has ended itself')