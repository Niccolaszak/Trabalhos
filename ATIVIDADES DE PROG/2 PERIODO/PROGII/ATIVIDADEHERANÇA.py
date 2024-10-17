class Computador:
    def __init__(self, proc, RAM, SO):
        self.proc = proc
        self.RAM = RAM
        self.SO = SO
    def sobre(self):
        print("COMPUTADOR")
        print(f"PROCESSADOR: {self.proc}")
        print(f"Memória RAM: {self.RAM}GB")
        print(f"Sistema Operacional: {self.SO}")

class Desktop(Computador):
    def __init__(self, proc, RAM, SO,Tamanho_tela):
        super().__init__(proc,RAM,SO)
        self.Tamanho_tela = Tamanho_tela
    def sobre(self):
        print("Desktop")
        print(f"PROCESSADOR: {self.proc}")
        print(f"Memória RAM: {self.RAM}GB")
        print(f"Sistema Operacional: {self.SO}")
        print(f"Tamanho da tela: {self.Tamanho_tela} Polegadas")
class Notebook(Desktop):
    def __init__(self, proc, RAM, SO,Tamanho_tela,peso):
        super().__init__(proc,RAM,SO,Tamanho_tela)
        self.peso = peso
    def sobre(self):
        print("Notebook")
        print(f"PROCESSADOR: {self.proc}")
        print(f"Memória RAM: {self.RAM}GB")
        print(f"Sistema Operacional: {self.SO}")
        print(f"Tamanho da tela: {self.Tamanho_tela} Polegadas")
        print(f"Peso: {self.peso}Kgs")
meu_computador = Computador("Core i5 3600GT", 8, "WINDOWS")
meu_desktop = Desktop("Intel Core i7", 16, "Windows 11", 27)
meu_notebook = Notebook("AMD Ryzen 7", 8, "macOS Monterey", 13.3, 1.5)
meu_computador.sobre()
print()
meu_desktop.sobre()
print()
meu_notebook.sobre()