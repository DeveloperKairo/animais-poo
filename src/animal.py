from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str, especie: str):
        self.nome = nome
        self.especie = especie

    def comer(self):
        print(f"{self.nome} ({self.especie}) está comendo...")

    @abstractmethod
    def emitir_som(self):
        pass
