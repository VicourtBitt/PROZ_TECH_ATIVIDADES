import random as rd
from random import randint

lista_de_armas = ["pedra", "papel", "tesoura"]

def tela_de_inicio():
    while True:
        nome = input("Escreva o seu nome: ")
        if len(nome) < 1:
            print("Escreva um nome com mais que duas letras. ")
            continue

        try:
            nro_rodadas = int(input("Escreva o número de rodadas: "))
        except ValueError:
            print("Escreva um número inteiro de rodadas. ")
            continue

        jokenpo(nome, nro_rodadas)

        decisao = input("Quer jogar novamente? [sim] - [nao] ")
        if decisao == "sim":
            continue
        else:
            print("Saindo do jogo.")
            break

def jokenpo(nome=str, nro_rodadas=int, lista=lista_de_armas):
    rodadas = 0
    pnts_pc = 0
    pnts_player = 0

    while rodadas < nro_rodadas:
        pc_choice = randint(0,2)

        print("Escolha sua arma:")
        try:
            arma_escolhida = int(input("Armas: [pedra = 0] - [papel = 1] - [tesoura = 2] "))
        except (ValueError, IndexError):
            print("Escreva um dos valores acima!")
            continue

        print(f"\n======RODADA {rodadas}======\n")
        print(f"Você escolheu {lista[arma_escolhida]}")
        print(f"O computador escolheu: {lista[pc_choice]}")

        if arma_escolhida == 0:
            if pc_choice == 1:
                print("O computador te aniquilou.")
                pnts_pc += 1
                rodadas += 1

            elif pc_choice == 2:
                print("Você aniquilou o computador!")
                pnts_player += 1
                rodadas += 1

            else:
                print("Vocês dois empatam nessa.")
                rodadas += 1


        elif arma_escolhida == 1:
            if pc_choice == 2:
                print("O computador te aniquilou.")
                pnts_pc += 1
                rodadas += 1

            elif pc_choice == 0:
                print("Você aniquilou o computador!")
                pnts_player += 1
                rodadas += 1

            else:
                print("Vocês dois empatam nessa.")
                rodadas += 1


        elif arma_escolhida == 2:
                if pc_choice == 0:
                    print("O computador te aniquilou.")
                    pnts_pc += 1
                    rodadas += 1

                elif pc_choice == 1:
                    print("Você aniquilou o computador!")
                    pnts_player += 1
                    rodadas += 1

                else:
                    print("Vocês dois empatam nessa.")
                    rodadas += 1
        print(f"\n====FIM DA RODADA====\n")

    print(f"O jogador ganhou {pnts_player} vez(es)! Enquanto o computador venceu {pnts_pc} vez(es).")
    if pnts_player > pnts_pc:
        print(f"O jogador foi o campeão da partida. Parabéns {nome}.")

    elif pnts_pc > pnts_player:
        print("O computador foi o campeão, as maquinas reinam!")

    else:
        print("Vocês dois empataram. Não há vencedor digno.")

tela_de_inicio()