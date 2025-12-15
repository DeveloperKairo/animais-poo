from .animal import Animal

class Mamifero(Animal):
    def __init__(self, nome: str, especie: str):
        super().__init__(nome, especie)

    def amamentar(self):
        print(f"{self.nome} está amamentando seus filhotes.")

class Leao(Mamifero):
    def __init__(self, nome: str):
        super().__init__(nome, "Leão")

    def emitir_som(self):
        print(f"{self.nome} ruge: ROAAAR!")

class Elefante(Mamifero):
    def __init__(self, nome: str):
        super().__init__(nome, "Elefante")

    def emitir_som(self):
        print(f"{self.nome} brame: TROMBETA!")
