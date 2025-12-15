from .animal import Animal

class Reptil(Animal):
    def __init__(self, nome: str, idade: int, especie: str, temperatura_corporal: float):
        super().__init__(nome, idade, especie)
        self.temperatura_corporal = temperatura_corporal

    def tomar_sol(self):
        print(f"{self.nome} está se aquecendo no sol. Temperatura: {self.temperatura_corporal}°C")

class Cobra(Reptil):
    def __init__(self, nome: str, idade: int, venenosa: bool):
        # Temperatura padrão para cobras
        super().__init__(nome, idade, "Cobra", 25.0)
        self.venenosa = venenosa

    def emitir_som(self):
        print(f"{self.nome} sibila: Ssssssss...")

    def trocar_pele(self):
        print(f"{self.nome} está trocando de pele.")
