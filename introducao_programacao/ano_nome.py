ANO_ATUAL = 2024

def ano_nome(year= ANO_ATUAL):
    while True:
        try:
            ano_nascimento = int(input("Escreva o ano em que nasceu: "))
            non_usable = ano_nascimento <= 1924 or not ano_nascimento

        except TypeError:
            print("Não foi inserido número inteiro. ")
            continue

        if non_usable:
            print("Idade inválida. ")
            continue

        nome = input("Escreva seu nome: ")
        name_non_usable = nome == ""

        if name_non_usable:
            print("Não aceitamos caixas de texto vazias.")
            continue

        idade_atual = ANO_ATUAL - ano_nascimento
        print(f"Seu nome é {nome}")
        print(f"Você tem aproximadamente {idade_atual} anos!")
        print()
    
ano_nome()
