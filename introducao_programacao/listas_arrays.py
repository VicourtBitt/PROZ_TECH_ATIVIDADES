# Uma lista de string's pelo seguinte motivo: São nomes
lista_produtos = [
    "Abacate",
    "Carne Moída",
    "Feijão",
    "Laranja",
    "Leite"
]

# Outra lita de strings pela data possuir uma formatação.
lista_datas = [
    "03-16-2004",
    "02-15-2004",
    "04-22-2005",
    "01-11-1952",
    "08-13-1962"
]

def listar_arrays(array=list):
    print("Esse é o início da lista selecionada.")
    for item in array:
        print(item)
    print(f"Esse é o fim da lista selecionada.\n")

produtos = listar_arrays(lista_produtos)
datas = listar_arrays(lista_datas)

print(produtos)
print(datas)
