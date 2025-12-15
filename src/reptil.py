from .animal import Animal

class Reptil(Animal):
    def __init__(self, nome: str, especie: str):
        super().__init__(nome, especie)

    def tomar_sol(self):
        print(f"{self.nome} está se aquecendo no sol.")

class Cobra(Reptil):
    def __init__(self, nome: str):
        super().__init__(nome, "Cobra")

    def emitir_som(self):
        print(f"{self.nome} sibila: Ssssssss...")
