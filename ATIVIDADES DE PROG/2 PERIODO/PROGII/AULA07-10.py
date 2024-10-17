class comp:
    def __init__(self):
        print("teste")

class desk(comp):
    def __init__(self):
        super().__init__()
        print("subclasse")
comp()
desk()