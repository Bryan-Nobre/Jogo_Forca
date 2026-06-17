# 🎮 Jogo da Forca em Python

## 📝 Descrição
Um clássico Jogo da Forca desenvolvido inteiramente em Python para rodar direto no terminal. O jogador deve adivinhar a palavra secreta, letra por letra, antes de esgotar todas as suas 6 vidas. O projeto combina lógica de programação, manipulação de listas e estruturas de repetição para criar uma experiência interativa, fluida e divertida.

## ✨ Funcionalidades
* **Sorteio Aleatório:** Palavras escolhidas aleatoriamente a partir de uma lista predefinida usando a biblioteca `random`.
* **Arte em ASCII:** Estágios da forca desenhados no terminal que mudam dinamicamente conforme o número de vidas do jogador diminui.
* **Interface Limpa:** Integração com o módulo `os` para limpar o terminal a cada rodada, criando um visual focado de "tela fixa".
* **Sistema de Validação:** Inteligência para identificar letras repetidas (tanto acertos quanto erros) e avisar o jogador sem penalizá-lo.
* **Opção de Fuga:** Comando `exit` implementado para abortar a partida a qualquer momento de forma segura.

## 🚀 Como Executar o Jogo

1. Certifique-se de ter o [Python](https://www.python.org/) instalado em seu computador.
2. Salve o código em um arquivo chamado `forca.py`.
3. Abra o seu terminal (ou prompt de comando).
4. Navegue até a pasta onde o arquivo foi salvo e execute o comando:

```bash
python forca.py
```

## 🧠 Tecnologias e Conceitos Praticados
Durante o desenvolvimento deste projeto, os seguintes conceitos de Python foram explorados e aplicados:
* Estruturas de controle de fluxo (`if`, `elif`, `else`).
* Laços de repetição (`while` para o loop principal do jogo e `for` para varredura de strings).
* Manipulação de Listas e Strings (métodos como `.lower()`, `.append()`, `.join()`).
* Lógica booleana e indexação de listas.

## 🏆 Créditos e Agradecimentos
Projeto desenvolvido como desafio de aprendizado estruturado com base nos ensinamentos e propostas do **Diego Pinho Learning Hub**.
