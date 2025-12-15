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
    print("0. Voltar") 
    
    tipo = input("Qual espécie deseja adicionar? ")
    
    if tipo == '0':
        return

    nome = input("Digite o nome do animal: ")
    # Perguntamos a idade agora, pois é atributo obrigatório
    try:
        idade = int(input("Digite a idade do animal: "))
    except ValueError:
        print("Idade inválida! Usando 0.")
        idade = 0
        
    novo_animal = None

    if tipo == "1":
        # Leão precisa de (nome, idade, tem_juba)
        tem_juba = input("O leão tem juba? (s/n): ").lower() == 's'
        novo_animal = Leao(nome, idade, tem_juba)
    elif tipo == "2":
        # Cobra precisa de (nome, idade, venenosa)
        venenosa = input("A cobra é venenosa? (s/n): ").lower() == 's'
        novo_animal = Cobra(nome, idade, venenosa)
    elif tipo == "3":
        # Papagaio precisa de (nome, idade)
        novo_animal = Papagaio(nome, idade)
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
    # Atualizado com novos construtores
    meu_zoo.adicionar_animal(Leao("Simba", 5, True))
    meu_zoo.adicionar_animal(Elefante("Dumbo", 10, 2.5))
    meu_zoo.adicionar_animal(Cobra("Nagini", 3, True))
    meu_zoo.adicionar_animal(Papagaio("Zé Carioca", 15))
    time.sleep(1) 
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
        print("4. Executar Ações Específicas (UML Methods)")
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
