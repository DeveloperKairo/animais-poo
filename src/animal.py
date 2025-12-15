from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str, idade: int, especie: str):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def comer(self):
        print(f"{self.nome} ({self.especie}) está comendo...")

    def dormir(self):
        print(f"{self.nome} está dormindo...")

    @abstractmethod
    def emitir_som(self):
        pass
