from typing import List
from .animal import Animal
from .ave import Ave, Papagaio
from .reptil import Reptil, Cobra
from .mamifero import Mamifero, Leao

class SistemaZoologico:
    def __init__(self):
        self.jaulas: List[Animal] = []

    def adicionar_animal(self, animal: Animal):
        self.jaulas.append(animal)
        print(f"[+] {animal.nome} foi adicionado ao zoológico.")

    def listar_animais(self):
        print("\n--- LISTA DE ANIMAIS NO ZOO ---")
        for animal in self.jaulas:
            print(f"- {animal.nome} é um(a) {animal.especie} de {animal.idade} anos.")

    def ouvir_barulho_do_zoo(self):
        print("\n--- BARULHO NO ZOO (POLIMORFISMO) ---")
        for animal in self.jaulas:
            animal.emitir_som()

    def realizar_rotina_diaria(self):
        print("\n--- ROTINA DIÁRIA (UML Methods) ---")
        for a in self.jaulas:
            print(f"- {a.nome}: ", end="")
            
            # Verificações específicas para os métodos novos do UML
            if isinstance(a, Leao):
                a.cacar()
            elif isinstance(a, Cobra):
                a.trocar_pele()
            elif isinstance(a, Papagaio):
                a.repetir_frase("Olá, mundo!")
            elif isinstance(a, Ave):
                a.voar()
            elif isinstance(a, Reptil):
                a.tomar_sol()
            elif isinstance(a, Mamifero):
                a.amamentar()
            else:
                a.dormir()
