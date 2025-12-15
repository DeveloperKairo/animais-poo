from typing import List
from .animal import Animal
from .ave import Ave
from .reptil import Reptil
from .mamifero import Mamifero

class SistemaZoologico:
    def __init__(self):
        self.jaulas: List[Animal] = []

    def adicionar_animal(self, animal: Animal):
        self.jaulas.append(animal)
        print(f"[+] {animal.nome} foi adicionado ao zoológico.")

    def listar_animais(self):
        print("\n--- LISTA DE ANIMAIS NO ZOO ---")
        for animal in self.jaulas:
            print(f"- {animal.nome} é um(a) {animal.especie}")

    def ouvir_barulho_do_zoo(self):
        print("\n--- BARULHO NO ZOO (POLIMORFISMO) ---")
        for animal in self.jaulas:
            animal.emitir_som()

    def realizar_rotina_diaria(self):
        print("\n--- ROTINA DIÁRIA (Type Checking) ---")
        for a in self.jaulas:
            print(f"- {a.nome}: ", end="")
            
            # Verifica se o animal é de um tipo específico (equivalente ao 'is' do C#)
            if isinstance(a, Ave):
                # Python não precisa de cast explícito como ((Ave)a), 
                # mas o isinstance garante que o método existe.
                a.voar()
            elif isinstance(a, Reptil):
                a.tomar_sol()
            elif isinstance(a, Mamifero):
                a.amamentar()
            else:
                print("Apenas existe.")
