import random
import os

palavras = [
    "python", "programacao", "desenvolvimento", "jogo", 
    "computador", "abacaxi", "algoritmo", "teclado", 
    "biblioteca", "internet", "engenharia", "framework"
]
palavra = random.choice(palavras)
letras_revelados = ["_"] * len(palavra)
letras_erradas = []
vidas = 6

# ADICIONADO: Lista com a arte em ASCII da forca. 
# A ordem é inversa (do 0 ao 6) para que o índice da lista seja exatamente igual ao número de vidas restantes.
estagios_forca = [
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """
]

while vidas > 0 and "_" in letras_revelados:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=== Jogo da Forca ===")
    
    # ADICIONADO: Imprime o estágio da forca correspondente à quantidade de vidas.
    print(estagios_forca[vidas])
    
    print("A palavra tem ", len(palavra) ," letras.")
    print("")
    print(f"Palavra: {' '.join(letras_revelados)}")
    print(f"Vidas restantes: {vidas}")

    print("Letras erradas: ", " ".join(letras_erradas))
    chute = input("Digite uma letra: ").lower()

    if (chute in letras_erradas) or (chute in letras_revelados):
        print("=" * 40) # ADICIONADO: Multiplicação de string para as linhas ficarem dinâmicas e limpas no código
        print("Você já tentou essa letra, tente outra.")
        print("=" * 40)

    elif (chute in palavra):
        print("=" * 40)
        print("Parabéns, você acertou uma letra!!")
        print("=" * 40)
        for i in range(len(palavra)):
            if (palavra[i] == chute):
                letras_revelados[i] = chute

    else:
        print("=" * 40)
        print("Que pena, você errou!")
        print("=" * 40)
        vidas -= 1
        letras_erradas.append(chute)
        
    # ADICIONADO: Pausa o jogo para que o jogador consiga ler se acertou ou errou 
    # antes do loop recomeçar e o 'os.system' limpar a tela.
    input("\nPressione Enter para continuar...")

# Fora do laço while, limpamos a tela uma última vez para o resultado final ficar em destaque
os.system('cls' if os.name == 'nt' else 'clear')

if (vidas == 0):
    # ADICIONADO: Imprime a forca completa (posição 0) no Game Over
    print(estagios_forca[0])
    print("Game Over! A palavra era: ", palavra)
else:
    print("Parabéns, você venceu! A palavra era: ", palavra)


# Observação: Explorando tags novas e recursos extras para deixar o código melhor, eu aprendi essas coisas:
#
# 1. Import do OS:
#    - os.name: O Python verifica o nome do sistema operacional. Se for Windows, o Python detecta como 'nt'.
#    - 'cls' if os.name == 'nt' else 'clear': Isso é um if simplificado em uma única linha. Ele diz: "Se o sistema for Windows (nt), use a palavra 'cls'. Se for qualquer outra coisa (Linux/Mac), use a palavra 'clear'".
#    - os.system(...): Envia o comando escolhido para o terminal limpar a tela.
#
# 2. Arte em ASCII e Índices de Lista:
#    - Usar uma lista de strings grandes (""") permite desenhar a forca. Organizando a lista de trás para frente, o número de 'vidas' se torna o índice exato para puxar o desenho correto na tela (ex: estagios_forca[vidas]).
#
# 3. Multiplicação de Strings:
#    - Usar print("=" * 40) é muito mais limpo do que digitar dezenas de sinais de igual manualmente.
#
# 4. Controle de Fluxo:
#    - Foi necessário usar um input("\nPressione Enter para continuar...") no final do while, senão a tela seria limpa pelo 'os' tão rápido que o jogador não conseguiria ler o feedback do seu chute.
