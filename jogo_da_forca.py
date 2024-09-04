import random

print('## Bem vindo ao jogo da forca! ##')
print('')
print('---------------------------------------------------------')
print('Dica: só vale animais, insetos.. enfim seres vivos hehe ')
print('---------------------------------------------------------')
print('')

palavras_definidas = ["abelha", "andorinha", "coruja", "baleia", "besouro",
"cobra", "elefante", "gafanhoto", "jabuti", "koala", "andorinha", "anta", "aranha",
"avestruz", "barata", "bezerro", 'arara', 'borboleta', 'camundongo', 'capivara', 'crocodilo',
'galinha', 'golfinho', 'hamster', 'iguana', 'jabuti', 'jegue', 'lebre', 'lagartixa', 'lagosta',
'macaco', 'morcego', 'mosquito', 'orangotango', 'panda', 'ovelha', 'porco', 'pinguim', 'quati',
'rato', 'raposa', 'touro', 'texugo', 'veado', 'zebra']

palpite = random.choice(palavras_definidas)

# Só pr ateste pra verificar a funcionalidade 
print(palpite) 

progresso = ['_'] * len(palpite)
letras_erradas = []
tentativas = 6

while tentativas > 0 and '_' in progresso:
    print('---------------------------------------------------------')
    chute = input('Digite uma letra: ').lower()

    if chute in palpite:
        for i, letra in enumerate(palpite):
            if letra == chute:
                progresso[i] = chute

    elif chute not in letras_erradas:
        letras_erradas.append(chute)
        tentativas -= 1
        print(f'Erro! a letra {letras_erradas} não está na palavra')
    else:
        print(f'Vc já tentou a letra {letras_erradas} ')

    print('Progresso: ' + ' '.join(progresso))

if '_' not in progresso:
    print('Parabens, vc adivinhou a palavra')
else:
    print(f'Vc perdeu! a palavra era "{palpite}"')











































