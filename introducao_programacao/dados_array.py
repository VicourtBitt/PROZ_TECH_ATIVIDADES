# A lista tem 15 items, porem ela começa contanto o 1° como se fosse 0
# então, mesmo que o último item seja 15, o número dele sempre é 1 a menos
lista_musicos = [ 
                'Djavan', 'Roberto Carlos', 'Elis Regina',
                'Tom Jobim', 'Milton Nascimento', 'Chico Buarque',
                'Nara Leão', 'Pitty', 'Simonal', 'Moacir Santos',
                'Caetano Veloso', 'Elza Soares', 'Paulinho da Viola',
                'Yamandú Costa', 'Gal Costa'
                ] 

# Uma função para exibir especificamente as informações da lista
def list_info(array= list):

    # Uma função aninhada para exibir cada índice da lista
    def show_index(array= lista_musicos):
        to_show = [2, 9, 14]
        for n in to_show:
            print(f"Presente no índice {n} está {array[n]}.")

    lenght_array = len(array)
    print(f"O tamanho da lista é {lenght_array}")

    show_index()
    

valores = list_info(lista_musicos)
