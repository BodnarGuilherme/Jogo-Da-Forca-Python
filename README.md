# 🐍 Jogo da Forca (Hangman Game)

Um clássico jogo da forca desenvolvido em **Python**, rodando diretamente no terminal. Este projeto foi criado para praticar lógica de programação, manipulação de strings e controle de fluxo.

## 📋 Sobre o Projeto

O jogo seleciona aleatoriamente uma palavra secreta de uma lista curada (tema: Animais/Seres Vivos) e desafia o jogador a adivinhá-la antes que as tentativas acabem.

### ✨ Funcionalidades

- **Banco de Palavras:** O jogo possui uma lista interna variada de animais.
- **Interface Limpa:** Função dedicada para limpar o terminal (`cls` no Windows ou `clear` no Linux/Mac) a cada rodada, melhorando a experiência visual.
- **Validação de Entrada:**
  - Impede a entrada de números ou símbolos.
  - Avisa se o usuário digitar mais de uma letra.
  - Detecta se a letra já foi jogada anteriormente.
- **Arte ASCII:** Visualização gráfica do "boneco" progredindo a cada erro.

## 🚀 Como Executar

Certifique-se de ter o **Python 3.x** instalado em sua máquina.

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/NOME-DO-REPO.git](https://github.com/SEU-USUARIO/NOME-DO-REPO.git)
   ```
2. Entre na pasta do projeto:
   ```bash
   cd NOME-DO-REPO
   ```
3. Execute o jogo:
   ```bash
   python nome_do_arquivo.py
   ```
   
## 🛠️ Tecnologias Utilizadas
  - Python 3
  - Biblioteca os (para interação com o sistema operacional)
  - Biblioteca random (para sorteio aleatório)

## 🧠 Aprendizados
Durante o desenvolvimento deste projeto, pude aprimorar:

- Estruturação de código em funções.
- Uso de List Comprehensions e estruturas condicionais.
- Tratamento de entradas do usuário (Input Validation).
- Lógica de loop while para controle de estados do jogo.

<br>
  <b> Desenvolvido por Guilherme Bodnar 
