from .animal import Animal

class Ave(Animal):
    def __init__(self, nome: str, idade: int, especie: str, tipo_bico: str):
        super().__init__(nome, idade, especie)
        self.tipo_bico = tipo_bico

    def voar(self):
        print(f"{self.nome} levantou voo e está batendo asas!")

class Papagaio(Ave):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade, "Papagaio", "Curvo")

    def emitir_som(self):
        print(f"{self.nome} diz: Loro quer biscoito!")

    def repetir_frase(self, frase: str):
        print(f"{self.nome} repete: '{frase}'")
