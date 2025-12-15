# 🦁 Sistema de Gestão de Zoológico (POO)

Este projeto foi desenvolvido como uma atividade prática para demonstrar e aplicar os **4 Pilares da Programação Orientada a Objetos** (POO): Abstração, Encapsulamento, Herança e Polimorfismo.

O sistema simula um gerenciador de zoológico onde é possível cadastrar diferentes tipos de animais e interagir com eles, observando seus comportamentos específicos e genéricos.

## 📚 Conceitos Abordados

- **Abstração**: Uso da classe base abstrata `Animal` que define o contrato (`emitir_som`) para todos os animais, impedindo a criação de animais genéricos.
- **Herança**: Classes como `Mamifero`, `Ave` e `Reptil` herdam características base de `Animal` e repassam para suas especializações (ex: `Leao`, `Papagaio`).
- **Polimorfismo**: Capacidade de tratar diferentes animais de forma uniforme na lista do zoológico, mas obtendo comportamentos distintos (ex: ao chamar `emitir_som()`, o leão ruge e o papagaio fala).
- **Encapsulamento**: A lógica de gerenciamento da lista de animais está protegida dentro da classe `SistemaZoologico`.

## 📂 Estrutura de Arquivos

O projeto está organizado da seguinte forma:

```
animais-poo/
│
├── main.py                 # Ponto de entrada da aplicação (Menu interativo)
├── README.md               # Documentação do projeto
└── src/                    # Pacote com as classes do domínio
    ├── __init__.py         # Exporta as classes para facilitar importação
    ├── animal.py           # Classe Abstrata Base (Animal)
    ├── mamifero.py         # Subclasses de Mamíferos (Leão, Elefante)
    ├── reptil.py           # Subclasses de Répteis (Cobra)
    ├── ave.py              # Subclasses de Aves (Papagaio)
    └── sistema_zoologico.py # Classe manipuladora (Controller) do zoológico
```

## 🚀 Como Executar

Certifique-se de ter o **Python 3** instalado.

1.  Abra o terminal na pasta raiz do projeto.
2.  Execute o comando:

```bash
# Se utilizar o launcher do Windows
py main.py

# Ou o comando padrão
python main.py
```

## ✨ Funcionalidades

1.  **Adicionar Animal**: Cadastre novos animais (Leão, Cobra, Papagaio) definindo seus nomes.
2.  **Listar Animais**: Veja todos os animais presentes no zoológico.
    - _Nota_: O sistema já inicia com alguns animais de exemplo (Simba, Dumbo, etc.).
3.  **Ouvir Animais (Polimorfismo)**: Faz todos os animais emitirem seus sons característicos.
4.  **Ações Específicas**: Demonstração de verificação de tipos (`isinstance`), onde Aves voam, Répteis tomam sol, etc.

---

Desenvolvido para fins educacionais.
