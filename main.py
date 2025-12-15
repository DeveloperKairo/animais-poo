import os
import time
from src import SistemaZoologico, Leao, Cobra, Papagaio, Elefante

def limpar_tela():
    # Limpa a tela de forma multiplataforma
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPressione ENTER para continuar...")

def menu_adicionar_animal(zoo: SistemaZoologico):
    limpar_tela()
    print("--- ADICIONAR NOVO ANIMAL ---")
    print("1. Leão")
    print("2. Cobra")
    print("3. Papagaio")
    print("0. Voltar") # Added option to go back safely
    
    tipo = input("Qual espécie deseja adicionar? ")
    
    if tipo == '0':
        return

    nome = input("Digite o nome do animal: ")
    novo_animal = None

    if tipo == "1":
        novo_animal = Leao(nome)
    elif tipo == "2":
        novo_animal = Cobra(nome)
    elif tipo == "3":
        novo_animal = Papagaio(nome)
    else:
        print("Espécie inválida! Animal não criado.")
        pausar()
        return

    if novo_animal:
        zoo.adicionar_animal(novo_animal)
    
    pausar()

def main():
    meu_zoo = SistemaZoologico()

    # --- POPULANDO O ZOO COM EXEMPLOS ---
    print("Populando o zoológico com animais padrão...")
    meu_zoo.adicionar_animal(Leao("Simba"))
    meu_zoo.adicionar_animal(Elefante("Dumbo"))
    meu_zoo.adicionar_animal(Cobra("Nagini"))
    meu_zoo.adicionar_animal(Papagaio("Zé Carioca"))
    time.sleep(1) # Pequena pausa para o usuário ver
    # ------------------------------------
    continuar = True

    while continuar:
        limpar_tela()
        print("=======================================")
        print("      SISTEMA DE GESTÃO - ZOOLÓGICO    ")
        print("=======================================")
        print("1. Adicionar Animal")
        print("2. Listar Animais na Jaula")
        print("3. Ouvir todos os animais (Polimorfismo)")
        print("4. Executar Ações Específicas (Voar/Nadar)")
        print("0. Sair")
        print("=======================================")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_adicionar_animal(meu_zoo)
        elif opcao == "2":
            meu_zoo.listar_animais()
            pausar()
        elif opcao == "3":
            meu_zoo.ouvir_barulho_do_zoo()
            pausar()
        elif opcao == "4":
            meu_zoo.realizar_rotina_diaria()
            pausar()
        elif opcao == "0":
            continuar = False
            print("Saindo do sistema...")
        else:
            print("Opção inválida!")
            pausar()

if __name__ == "__main__":
    main()
