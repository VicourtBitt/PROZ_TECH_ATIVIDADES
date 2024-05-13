lista_produtos = [
                'máscaras faciais', 'batons', 
                'esmaltes', 'perfumes', 
                'loções', 'xampus', 
                'sabonetes', 'delineadores'
                  ]

def update_list(array= lista_produtos):
    
    for i in range(len(lista_produtos)):
        if array[i] == "batons":
            array[i] = "rímel"

        elif array[i] == "loções":
            array[i] = "cremes hidratantes"

        elif array[i] == "delineadores":
            array.pop()
    
    new_list = list(array)
    new_list.append("Gloss")
    new_list.append("Sombra")
    
    for n, i in enumerate(new_list):
        print(f"Temos: {n+1}°, {i}")

    return "Fim do novo catálogo."

produtos = update_list(lista_produtos)
print(produtos)
