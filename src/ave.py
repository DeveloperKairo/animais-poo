from .animal import Animal

class Ave(Animal):
    def __init__(self, nome: str, especie: str):
        super().__init__(nome, especie)

    def voar(self):
        print(f"{self.nome} levantou voo e está batendo asas!")

class Papagaio(Ave):
    def __init__(self, nome: str):
        super().__init__(nome, "Papagaio")

    def emitir_som(self):
        print(f"{self.nome} diz: Loro quer biscoito!")
