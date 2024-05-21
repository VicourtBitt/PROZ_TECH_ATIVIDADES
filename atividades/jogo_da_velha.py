import random as rd

palavras = [
    "banana", "chocolate", "macarrao", 'cadeira', 'biscoito',
    'tiradentes', 'flor', 'rosa', 'mesa'
]

def jogo_da_forca(palavra=rd.choice(palavras)):

    palavra_completa = palavra
    letras_certas = ''
    tentativas = 0

    while True:
        letra = input('Digite uma letra a sua escolha: ')
        tentativas += 1

        if len(letra) > 1:
            print('Digite apenas uma letra.')
            continue

        if letra in palavra_completa:
            letras_certas += letra

        palavra_incompleta = ''
        for letras in palavra_completa:
            if letras in letras_certas:
                palavra_incompleta += letras
            else:
                palavra_incompleta += '*'

        print('Palavra formada:', palavra_incompleta)

        if palavra_incompleta == palavra_completa:
            print('Parabéns. A palavra era:', palavra_completa)
            print(f"Você tentou {tentativas} vezes!")
            break

jogo_da_forca()