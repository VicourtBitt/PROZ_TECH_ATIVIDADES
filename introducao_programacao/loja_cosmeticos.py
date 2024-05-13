lista_produtos = [
                'máscaras faciais', 'batons', 
                'esmaltes', 'perfumes', 
                'loções', 'xampus', 
                'sabonetes', 'delineadores'
                  ]

def each_item(array= list):
    for n_item in range(len(array)):
        print(f"Nós temos {array[n_item]} à venda!")
    return "A seleção de items acabou!"

produtos = each_item(lista_produtos)
print(produtos)
