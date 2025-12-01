import random
import os

def limpar_tela():
    """Limpa o terminal para melhorar a experiência visual."""
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_palavra_secreta():
    """Retorna uma palavra aleatória de uma lista curada."""
    #Set() para remover duplicatas automaticamente caso a lista cresça
    palavras = list({
        "abelha", "andorinha", "coruja", "baleia", "besouro", "cobra", 
        "elefante", "gafanhoto", "jabuti", "koala", "anta", "aranha",
        "avestruz", "barata", "bezerro", "arara", "borboleta", "camundongo", 
        "capivara", "crocodilo", "galinha", "golfinho", "hamster", "iguana", 
        "jegue", "lebre", "lagartixa", "lagosta", "macaco", "morcego", 
        "mosquito", "orangotango", "panda", "ovelha", "porco", "pinguim", 
        "quati", "rato", "raposa", "touro", "texugo", "veado", "zebra"
    })
    return random.choice(palavras).upper() # UPPER case

def display_hangman(tentativas):
    stages = [
        # Estágio 0 (Perdeu)
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------""",
        # Estágio 1
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------""",
        # Estágio 2
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------""",
        # Estágio 3
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------""",
        # Estágio 4
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------""",
        # Estágio 5
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------""",
        # Estágio 6 (Início)
        """
           -----
           |   |
               |
               |
               |
               |
        --------"""
    ]
    return stages[tentativas]

def main():
    palavra_secreta = obter_palavra_secreta()
    letras_descobertas = ['_' for _ in palavra_secreta]
    letras_erradas = []
    tentativas = 6

    print('## Bem vindo ao jogo da forca! ##')
    print('Dica: só vale animais, insetos... seres vivos!')
    input('Pressione ENTER para começar...')

    while tentativas > 0 and '_' in letras_descobertas:
        limpar_tela()
        
        print(display_hangman(tentativas))
        print(f"Palavra: {' '.join(letras_descobertas)}")
        print(f"Erros ({len(letras_erradas)}): {', '.join(letras_erradas)}")
        print('---------------------------------------------------------')

        #Input
        chute = input('Digite uma letra: ').strip().upper()

        if len(chute) != 1 or not chute.isalpha():
            print("⚠ Entrada inválida! Digite apenas uma letra.")
            input("Pressione ENTER para continuar...")
            continue

        if chute in letras_erradas or chute in letras_descobertas:
            print(f"⚠ Você já tentou a letra '{chute}'.")
            input("Pressione ENTER para continuar...")
            continue

        # Lógica de Jogo
        if chute in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_descobertas[index] = chute
        else:
            letras_erradas.append(chute)
            tentativas -= 1
    
    # Fim de jogo
    limpar_tela()
    if '_' not in letras_descobertas:
        print(f"PARABÉNS! Você salvou o boneco. A palavra era: {palavra_secreta}")
    else:
        print(display_hangman(tentativas))
        print(f"GAME OVER! A palavra era: {palavra_secreta}")

if __name__ == "__main__":
    main()