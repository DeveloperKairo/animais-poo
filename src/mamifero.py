from .animal import Animal

class Mamifero(Animal):
    def __init__(self, nome: str, idade: int, especie: str, cor_pelo: str):
        super().__init__(nome, idade, especie)
        self.cor_pelo = cor_pelo

    def amamentar(self):
        print(f"{self.nome} está amamentando seus filhotes.")

class Leao(Mamifero):
    def __init__(self, nome: str, idade: int, tem_juba: bool):
        super().__init__(nome, idade, "Leão", "Amarelo")
        self.tem_juba = tem_juba

    def emitir_som(self):
        print(f"{self.nome} ruge: ROAAAR!")

    def cacar(self):
        print(f"{self.nome} está caçando uma presa!")

class Elefante(Mamifero):
    def __init__(self, nome: str, idade: int, tamanho_tromba: float):
        super().__init__(nome, idade, "Elefante", "Cinza")
        self.tamanho_tromba = tamanho_tromba

    def emitir_som(self):
        print(f"{self.nome} brame: TROMBETA!")
